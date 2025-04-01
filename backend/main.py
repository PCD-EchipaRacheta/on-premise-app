from fastapi import FastAPI, WebSocket, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from google.cloud import bigquery
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import asyncio
import random
import httpx
import os

app = FastAPI()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "account.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DAILY_WEATHER_CLOUD_RUN_URL = "https://get-daily-weather-41335490407.europe-west3.run.app"

@app.get("/weather")
async def get_hourly_forecast(city: str = Query("Iași")):
    try:
        credentials = service_account.IDTokenCredentials.from_service_account_file(
            filename="account.json",
            target_audience=DAILY_WEATHER_CLOUD_RUN_URL
        )
        credentials.refresh(Request())

        headers = {
            "Authorization": f"Bearer {credentials.token}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DAILY_WEATHER_CLOUD_RUN_URL}?city={city}", headers=headers)
            response.raise_for_status()
            raw = response.json()

        hourly = raw.get("hour", [])
        formatted = [
            {
                "city": city,
                "temperature": h.get("temp_c"),
                "precipitation": h.get("chance_of_rain", 0),
                "timestamp": h.get("time")
            }
            for h in hourly
        ]

        return formatted

    except Exception as e:
        print("Error fetching hourly weather:", e)
        return []


SEVEN_DAY_FORECAST_URL = "https://get-7day-forecast-41335490407.europe-west3.run.app"

@app.get("/daily")
async def get_daily_forecast(city: str = Query("Iași")):
    try:
        credentials = service_account.IDTokenCredentials.from_service_account_file(
            filename="account.json",
            target_audience=SEVEN_DAY_FORECAST_URL
        )
        credentials.refresh(Request())

        headers = {
            "Authorization": f"Bearer {credentials.token}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{SEVEN_DAY_FORECAST_URL}?city={city}", headers=headers
            )
            response.raise_for_status()
            daily_raw = response.json() 

        formatted = []
        for entry in daily_raw:
            date_str = entry.get("date")
            day_name = datetime.strptime(date_str, "%Y-%m-%d").strftime("%A")

            avg_temp = entry["day"].get("avgtemp_c")
            precipitation = entry["day"].get("daily_chance_of_rain", 0)

            formatted.append({
                "day": day_name,
                "avgTemp": avg_temp,
                "precipitation": precipitation
            })

        return formatted

    except Exception as e:
        print("Error fetching daily forecast:", e)
        return []

CURRENT_CLOUD_RUN_URL = "https://get-weather-41335490407.europe-west3.run.app"

@app.websocket("/ws/current")
async def websocket_current_weather(websocket: WebSocket):
    await websocket.accept()

    city = websocket.query_params.get("city", "Iași")

    try:
        while True:
            try:
                credentials = service_account.IDTokenCredentials.from_service_account_file(
                    filename="account.json",
                    target_audience=CURRENT_CLOUD_RUN_URL 
                )

                request_adapter = Request()
                credentials.refresh(request_adapter)

                headers = {
                    "Authorization": f"Bearer {credentials.token}"
                }

                async with httpx.AsyncClient() as client:
                    response = await client.get(f"https://get-weather-41335490407.europe-west3.run.app?city={city}", headers=headers)
                    response.raise_for_status()
                    current = response.json()

                    await websocket.send_json(current)

            except Exception as e:
                print("Error fetching current weather:", e)
                await websocket.send_json({})

            await asyncio.sleep(10)
    except Exception as e:
        print("WebSocket closed:", e)
        await websocket.close()
