from weather_data import WeatherData
from weather_db import insert_weather_record, get_latest_weather_record

def main():
    # Boston, MA - March 17 (St. Patrick's Day)
    weather = WeatherData(
        latitude=42.3601,
        longitude=-71.0589,
        month=3,
        day=17,
        year=2026
    )

    # Calculate five-year statistics (2021-2025)
    weather.calculate_five_year_stats()

    # Insert into SQLite
    insert_weather_record(weather)

    # Query back from SQLite
    record = get_latest_weather_record()

    # Display results (formatted)
    print("----------------------------------------")
    print("Weather Summary (From Database)")
    print("----------------------------------------")
    print(f"Location: ({record.latitude}, {record.longitude})")
    print(f"Event Date: {record.month:02d}-{record.day:02d} (Target Year: {record.year})")
    print("----------------------------------------")
    print(f"Average Temperature (F): {record.avg_temp:.2f}")
    print(f"Minimum Temperature (F): {record.min_temp:.2f}")
    print(f"Maximum Temperature (F): {record.max_temp:.2f}")
    print("")
    print(f"Average Wind Speed (mph): {record.avg_wind:.2f}")
    print(f"Minimum Wind Speed (mph): {record.min_wind:.2f}")
    print(f"Maximum Wind Speed (mph): {record.max_wind:.2f}")
    print("")
    print(f"Total Precipitation (in): {record.sum_precip:.2f}")
    print(f"Minimum Precipitation (in): {record.min_precip:.2f}")
    print(f"Maximum Precipitation (in): {record.max_precip:.2f}")
    print("----------------------------------------")

    # Generate and save visualization
    weather.plot_five_year_summary()


if __name__ == "__main__":
    main()