# Historical Weather Analysis — Python Application

A Python application that retrieves historical weather data from a public API, calculates multi-year statistics, stores results in a local database, and outputs a formatted analytical summary.

Built to demonstrate end-to-end data pipeline skills: API integration, data processing, database management, and unit testing.

---

## What It Does

- Fetches historical daily weather data for a given location and date using the [Open-Meteo Archive API](https://open-meteo.com/)
- Calculates 5-year average, minimum, and maximum statistics for:
  - Temperature (°F)
  - Wind speed (mph)
  - Precipitation (inches)
- Stores results in a local SQLite database using SQLAlchemy ORM
- Queries and displays a formatted weather summary from the database
- Includes unit tests for API retrieval, calculations, and database operations
- Generates a 3-panel bar chart visualizing year-by-year trends with 5-year averages
---

## Sample Output

```
----------------------------------------
Weather Summary (From Database)
----------------------------------------
Location: (42.3601, -71.0589)
Event Date: 03-17 (Target Year: 2026)
----------------------------------------
Average Temperature (F): 45.10
Minimum Temperature (F): 37.76
Maximum Temperature (F): 52.34

Average Wind Speed (mph): 13.73
Minimum Wind Speed (mph): 6.40
Maximum Wind Speed (mph): 21.50

Total Precipitation (in): 1.83
Minimum Precipitation (in): 0.00
Maximum Precipitation (in): 1.66
----------------------------------------
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| requests | REST API calls |
| SQLAlchemy | ORM and SQLite database management |
| pytest | Unit testing |

---

## Project Structure

```
├── main.py            # Entry point — runs the full pipeline
├── weather_data.py    # WeatherData class — API calls and statistics
├── weather_db.py      # Database schema, insert, and query functions
├── test_weather.py    # Unit tests (pytest)
├── requirements.txt   # Project dependencies
```

---

## Getting Started

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the application:**
```bash
python main.py
```

**Run unit tests:**
```bash
pytest -q
```

---

## Skills Demonstrated

- REST API integration and JSON data parsing
- Object-oriented programming in Python
- Database design and ORM usage with SQLAlchemy
- Statistical calculations (mean, min, max) on real-world data
- Unit testing with pytest
- Clean project structure and documentation
