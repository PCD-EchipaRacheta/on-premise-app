import React, { useEffect, useState } from "react"
import client from "../api/client"

interface DayWeather {
  day: string
  avgTemp: number
  precipitation: number
}

const WeatherTableByDay: React.FC<{ city: string }> = ({ city }) => {
  const [weekData, setWeekData] = useState<DayWeather[]>([])

  useEffect(() => {
    client
      .get(`/daily?city=${encodeURIComponent(city)}`)
      .then((res) => setWeekData(res.data))
      .catch((err) => console.error("API error:", err))
  }, [city])

  return (
    <div
      style={{
        padding: "1rem",
        maxWidth: "800px",
        margin: "0 auto",
        boxSizing: "border-box",
      }}
    >
      <h2 style={{ marginBottom: "1rem", textAlign: "center" }}>
        7-Day Forecast for {city}
      </h2>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th style={th}>Day</th>
            <th style={th}>Avg Temp</th>
            <th style={th}>Precipitation</th>
          </tr>
        </thead>
        <tbody>
          {weekData.map((entry, i) => (
            <tr key={i}>
              <td style={td}>{entry.day}</td>
              <td style={td}>{entry.avgTemp}°C</td>
              <td style={td}>{entry.precipitation}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

const th = {
  textAlign: "left",
  padding: "12px 8px",
  borderBottom: "1px solid #ccc",
  fontWeight: "bold",
} as React.CSSProperties

const td = {
  textAlign: "left",
  padding: "12px 8px",
  borderBottom: "1px solid #eee",
  whiteSpace: "nowrap",
} as React.CSSProperties

export default WeatherTableByDay
