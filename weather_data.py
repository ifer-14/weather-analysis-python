import requests
import matplotlib.pyplot as plt

class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
        # Location and date information
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year

        # Weather Statistics (calculated in calculate_five_year_stats)
        self.avg_temp = 0
        self.min_temp = 0
        self.max_temp = 0

        self.avg_wind = 0
        self.min_wind = 0
        self.max_wind = 0

        self.sum_precip = 0
        self.min_precip = 0
        self.max_precip = 0

        # Store year-by-year data for visualization
        self.years = []
        self.yearly_temps = []
        self.yearly_winds = []
        self.yearly_precips = []

    def _date_string(self, year):
        return f"{year}-{self.month:02d}-{self.day:02d}"

    def get_temperature_for_year(self, year):
        date = self._date_string(year)
        url = (
            "https://archive-api.open-meteo.com/v1/archive"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            f"&start_date={date}"
            f"&end_date={date}"
            "&daily=temperature_2m_mean"
            "&timezone=auto"
        )
        data = requests.get(url, timeout=20).json()
        temp_c = data["daily"]["temperature_2m_mean"][0]
        return (temp_c * 9 / 5) + 32

    def get_wind_speed_for_year(self, year):
        date = self._date_string(year)
        url = (
            "https://archive-api.open-meteo.com/v1/archive"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            f"&start_date={date}"
            f"&end_date={date}"
            "&daily=wind_speed_10m_max"
            "&timezone=auto"
        )
        data = requests.get(url, timeout=20).json()
        wind_kmh = data["daily"]["wind_speed_10m_max"][0]
        return wind_kmh * 0.621371

    def get_precipitation_for_year(self, year):
        date = self._date_string(year)
        url = (
            "https://archive-api.open-meteo.com/v1/archive"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            f"&start_date={date}"
            f"&end_date={date}"
            "&daily=precipitation_sum"
            "&timezone=auto"
        )
        data = requests.get(url, timeout=20).json()
        precip_mm = data["daily"]["precipitation_sum"][0]
        return precip_mm * 0.0393701

    def calculate_five_year_stats(self):
        self.years = [self.year - i for i in range(1, 6)]

        self.yearly_temps = [self.get_temperature_for_year(y) for y in self.years]
        self.yearly_winds = [self.get_wind_speed_for_year(y) for y in self.years]
        self.yearly_precips = [self.get_precipitation_for_year(y) for y in self.years]

        self.avg_temp = sum(self.yearly_temps) / len(self.yearly_temps)
        self.min_temp = min(self.yearly_temps)
        self.max_temp = max(self.yearly_temps)

        self.avg_wind = sum(self.yearly_winds) / len(self.yearly_winds)
        self.min_wind = min(self.yearly_winds)
        self.max_wind = max(self.yearly_winds)

        self.sum_precip = sum(self.yearly_precips)
        self.min_precip = min(self.yearly_precips)
        self.max_precip = max(self.yearly_precips)

    def plot_five_year_summary(self):
        years_str = [str(y) for y in self.years]

        fig, axes = plt.subplots(1, 3, figsize=(14, 5))
        fig.suptitle(
            f"5-Year Weather Summary — {self.month:02d}/{self.day:02d} "
            f"({self.years[-1]}–{self.years[0]})\n"
            f"Location: ({self.latitude}, {self.longitude})",
            fontsize=13, fontweight="bold"
        )

        # Temperature chart
        bars = axes[0].bar(years_str, self.yearly_temps, color="#4C72B0", edgecolor="white")
        axes[0].axhline(y=self.avg_temp, color="#DD8452", linewidth=2,
                        linestyle="--", label=f"Avg: {self.avg_temp:.1f}°F")
        axes[0].set_title("Temperature (°F)")
        axes[0].set_ylabel("°F")
        axes[0].legend()
        axes[0].set_ylim(0, max(self.yearly_temps) * 1.2)
        for bar, val in zip(bars, self.yearly_temps):
            axes[0].text(bar.get_x() + bar.get_width() / 2,
                         bar.get_height() + 0.5, f"{val:.1f}",
                         ha="center", va="bottom", fontsize=9)

        # Wind speed chart
        bars = axes[1].bar(years_str, self.yearly_winds, color="#55A868", edgecolor="white")
        axes[1].axhline(y=self.avg_wind, color="#DD8452", linewidth=2,
                        linestyle="--", label=f"Avg: {self.avg_wind:.1f} mph")
        axes[1].set_title("Wind Speed (mph)")
        axes[1].set_ylabel("mph")
        axes[1].legend()
        axes[1].set_ylim(0, max(self.yearly_winds) * 1.2)
        for bar, val in zip(bars, self.yearly_winds):
            axes[1].text(bar.get_x() + bar.get_width() / 2,
                         bar.get_height() + 0.2, f"{val:.1f}",
                         ha="center", va="bottom", fontsize=9)

        # Precipitation chart
        bars = axes[2].bar(years_str, self.yearly_precips, color="#C44E52", edgecolor="white")
        axes[2].axhline(y=self.sum_precip / len(self.yearly_precips), color="#DD8452",
                        linewidth=2, linestyle="--",
                        label=f"Avg: {self.sum_precip / len(self.yearly_precips):.2f} in")
        axes[2].set_title("Precipitation (in)")
        axes[2].set_ylabel("inches")
        axes[2].legend()
        axes[2].set_ylim(0, max(self.yearly_precips) * 1.4 + 0.1)
        for bar, val in zip(bars, self.yearly_precips):
            axes[2].text(bar.get_x() + bar.get_width() / 2,
                         bar.get_height() + 0.01, f"{val:.2f}",
                         ha="center", va="bottom", fontsize=9)

        plt.tight_layout()
        plt.savefig("weather_summary.png", dpi=150, bbox_inches="tight")
        plt.show()
        print("Chart saved as weather_summary.png")