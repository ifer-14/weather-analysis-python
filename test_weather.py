# Unit test Run with pytest -q

import random

from weather_data import WeatherData
from weather_db import insert_weather_record, get_latest_weather_record

def test_temperature_method_returns_number():
    w = WeatherData(latitude=42.3601, longitude=-71.0589, month=3, day=17, year=2026)
    temp_f = w.get_temperature_for_year(2023)
    assert isinstance(temp_f, (int, float))

def test_calculate_five_year_stats_populates_fields():
    w = WeatherData(latitude=42.3601, longitude=-71.0589, month=3, day=17, year=2026)
    w.calculate_five_year_stats()
    # Basic sanity checks (should be numbers)
    assert isinstance(w.avg_temp, (int, float))
    assert isinstance(w.avg_wind, (int, float))
    assert isinstance(w.sum_precip, (int, float))

def test_database_insert_and_query_returns_records():
    year = random.choice([2021, 2022, 2023, 2024, 2025])

    w = WeatherData(latitude=42.3601, longitude=-71.0589, month=3, day=17, year=year)
    w.calculate_five_year_stats()

    insert_weather_record(w)
    record = get_latest_weather_record()

    assert record is not None
    assert record.year == year