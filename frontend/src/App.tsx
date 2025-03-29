import React from "react"
import WeatherTable from "./components/WeatherTable"
import WeatherTableByDay from "./components/WeatherTableByDay"

function App() {
  return (
    <div style={{ maxWidth: "1920px", margin: "0 auto", padding: "1rem" }}>
      <h1
        style={{
          textAlign: "center",
          marginTop: "1rem",
          marginBottom: "2rem",
        }}
      >
        Weather App
      </h1>
      <WeatherTable />
    </div>
  )
}

export default App
