import React from "react"

interface CitySelectorProps {
  selectedCity: string
  onChange: (city: string) => void
}

const cities = ["Iasi", "Bucharest", "Cluj-Napoca", "Timisoara", "Constanta", "Craiova", "Brasov", "Ploiesti", "Suceava", "Galati"]

const CitySelector: React.FC<CitySelectorProps> = ({ selectedCity, onChange }) => {
  return (
    <div style={{ position: "absolute", top: "1rem", left: "1rem" }}>
      <label htmlFor="city" style={{ marginRight: "0.5rem", fontWeight: "bold" }}>
        City:
      </label>
      <select
        id="city"
        value={selectedCity}
        onChange={(e) => onChange(e.target.value)}
        style={{
          padding: "0.4rem 0.6rem",
          borderRadius: "6px",
          border: "1px solid #ccc",
          fontSize: "1rem",
        }}
      >
        {cities.map((city) => (
          <option key={city} value={city}>
            {city}
          </option>
        ))}
      </select>
    </div>
  )
}

export default CitySelector
