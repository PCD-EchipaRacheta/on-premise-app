import React, { useEffect, useState } from "react"
import client from "../api/client"
import "./WeatherTable.css"
import WeatherTableByDay from "./WeatherTableByDay"

interface WeatherData {
  city: string
  temperature: number
  timestamp: string
  precipitation?: number
}

const WeatherTable = () => {
  const [data, setData] = useState<WeatherData[]>([])

  useEffect(() => {
    client
      .get("/weather?city=Iași")
      .then((res) => setData(res.data))
      .catch((err) => console.error("API error:", err))
  }, [])

  return (
    <>
    <div className="weather-container">
      <div className="weather-scroll">
        {data.map((entry, index) => {
          const time = new Date(entry.timestamp).toLocaleTimeString("ro-RO", {
            hour: "2-digit",
            minute: "2-digit",
          })

          return (
            <div className="weather-card" key={index}>
              <div className="weather-time">{time} 🕐</div>
              <div className="weather-precipitation">
                ☁️ {entry.precipitation ?? 30}%
              </div>
              <div className="weather-temp">{entry.temperature}°C 🌡️</div>
            </div>
          )
        })}
      </div>
    </div>
    <WeatherTableByDay />
    </>
  )
}

export default WeatherTable