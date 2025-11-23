import React, { useState } from 'react';

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);

  const fetchWeather = async () => {
    const res = await fetch(`http://localhost:5000/weather?city=${city}`);
    const data = await res.json();
    setWeather(data);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Weather App</h1>
      <input
        type="text"
        value={city}
        placeholder="Enter city"
        onChange={(e) => setCity(e.target.value)}
      />
      <button onClick={fetchWeather}>Get Weather</button>

      {weather && (
        <div style={{ marginTop: '1rem' }}>
          <p><strong>{weather.area}, {weather.region}, {weather.country}</strong></p>
          <p>Temperature: {weather.temp_F}°F</p>
          <p>Condition: {weather.desc}</p>
        </div>
      )}
    </div>
  );
}

export default App;
