from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime

app = FastAPI()

# Allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
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
