import React from "react"

interface DayWeather {
  day: string
  avgTemp: number
  precipitation: number
}

const WeatherTableByDay = () => {
  const weekData: DayWeather[] = [
    { day: "Monday", avgTemp: 14, precipitation: 30 },
    { day: "Tuesday", avgTemp: 16, precipitation: 20 },
    { day: "Wednesday", avgTemp: 15, precipitation: 10 },
    { day: "Thursday", avgTemp: 12, precipitation: 50 },
    { day: "Friday", avgTemp: 13, precipitation: 40 },
    { day: "Saturday", avgTemp: 17, precipitation: 5 },
    { day: "Sunday", avgTemp: 11, precipitation: 60 },
  ]

  return (
    <div
      style={{
        padding: "1rem",
        maxWidth: "800px",
        margin: "0 auto", // ✅ centers horizontally
        boxSizing: "border-box",
      }}
    >
      <h2 style={{ marginBottom: "1rem", textAlign: "center" }}>
        7-Day Forecast
      </h2>
      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
        }}
      >
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
