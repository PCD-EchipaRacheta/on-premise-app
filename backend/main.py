from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime

from google.cloud import bigquery
import os

# Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "account.json"

# Construct a BigQuery client object.
client = bigquery.Client()

dataset_id = "weatherapp-455117.weather_data"
tables = list(client.list_tables(dataset_id))
table_ids = list(map(lambda x: x.table_id, tables))

app = FastAPI()

# Allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy weather data
weather_data = [
    {"city": "Iași", "temperature": 14, "timestamp": "2025-03-27T12:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "Iași", "temperature": 13, "timestamp": "2025-03-27T11:00:00"},
    {"city": "București", "temperature": 16, "timestamp": "2025-03-27T12:00:00"},
]

@app.get("/weather")
def get_weather(city: str = Query(..., description="City name")):
    results = [entry for entry in weather_data if entry["city"].lower() == city.lower()]
    return results

@app.get("/tables")
def get_tables():
    return table_ids