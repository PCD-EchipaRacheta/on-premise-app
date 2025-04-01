import React, { useState } from "react"
import WeatherTable from "./components/WeatherTable"
import WeatherTableByDay from "./components/WeatherTableByDay"
import CurrentWeatherCard from "./components/CurrentWeatherCard"
import CitySelector from "./components/CitySelector"

function App() {
  const [city, setCity] = useState("Iasi")

  return (
    <div
      style={{
        width: "100%",
        padding: "1rem",
        boxSizing: "border-box",
        display: "flex",
        justifyContent: "center",
      }}
    >

    <CitySelector selectedCity={city} onChange={setCity} />
      <div
        style={{
          width: "100%",
          maxWidth: "1000px",
        }}
      >
        <h1
          style={{
            textAlign: "center",
            marginTop: "1rem",
            marginBottom: "2rem",
          }}
        >
          Weather App
        </h1>
          
        <CurrentWeatherCard city={city} />
        <WeatherTable city={city} />
        <WeatherTableByDay city={city} />
      </div>
    </div>
  )
}

export default App
