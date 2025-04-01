import React, { useEffect, useState } from "react"

interface Condition {
  text: string
  icon: string
}

interface CurrentWeatherProps {
  last_updated: string
  temp_c: number
  condition: Condition
  feelslike_c: number
  humidity: number
  pressure_mb: number
  wind_kph: number
  wind_dir: string
}

const CurrentWeatherCard: React.FC<{ city: string }> = ({ city }) => {
  const [data, setData] = useState<CurrentWeatherProps | null>(null)

  useEffect(() => {
    const socket = new WebSocket(`ws://localhost:8000/ws/current?city=${encodeURIComponent(city)}`)

    socket.onmessage = (event) => {
      const incoming = JSON.parse(event.data)
      if (incoming && incoming.temp_c) {
        setData(incoming)
      }
    }

    socket.onerror = (error) => {
      console.error("WebSocket error:", error)
    }

    return () => socket.close()
  }, [city])

  if (!data) return null

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "1rem",
        backgroundColor: "#f5f5f5",
        borderRadius: "12px",
        boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
        marginBottom: "2rem",
        gap: "1rem",
        flexWrap: "wrap",
        color: "#000",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
        <img
          src={`https:${data.condition.icon}`}
          alt={data.condition.text}
          style={{ width: 64, height: 64 }}
        />
        <div>
          <div style={{ fontSize: "2rem", fontWeight: "bold", color: "#000" }}>
            {data.temp_c}°C
          </div>
          <div style={{ color: "#000" }}>{data.condition.text}</div>
        </div>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "4px", color: "#000" }}>
        <div>Feels like: {data.feelslike_c}°C</div>
        <div>Humidity: {data.humidity}%</div>
        <div>Pressure: {data.pressure_mb} mb</div>
        <div>
          Wind: {data.wind_kph} km/h ({data.wind_dir})
        </div>
        <div style={{ fontSize: "0.85rem", color: "#444" }}>
          Updated at: {data.last_updated}
        </div>
      </div>
    </div>
  )
}

export default CurrentWeatherCard
