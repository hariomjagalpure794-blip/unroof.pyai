# day 4

import requests # type: ignore
import logging

logging.basicConfig(
    filename="weather_app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = "YOUR_API_KEY_HERE"   
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


class CityNotFoundError(Exception):
    """Raised when the entered city doesn't exist"""
    pass


def get_weather(city):
    """
    Fetch weather data for a given city.
    Returns a dict with temperature, humidity, and condition.
    Raises CityNotFoundError or requests exceptions on failure.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   
    }
    pass


def display_weather(city, weather):
    """Nicely print the weather details"""

    pass


def menu():
    while True:
        print("\n--- Weather CLI ---")
        city = input("Enter city name (or 'quit' to exit): ").strip()

        if city.lower() == "quit":
            logging.info("Program exited by user.")
            break

        if not city:
            print("⚠️  City name cannot be empty")
            continue

        try:
            weather = get_weather(city)
            display_weather(city, weather)
            logging.info(f"Weather fetched successfully for {city}")

        except CityNotFoundError as e:
            print(f"⚠️  {e}")
            logging.warning(str(e))
        except requests.exceptions.Timeout:
            print("⚠️  Request timed out. Check your connection.")
            logging.error("Request timed out")
        except requests.exceptions.ConnectionError:
            print("⚠️  No internet connection.")
            logging.error("Connection error")
        except requests.exceptions.RequestException as e:
            print(f"⚠️  API error occurred. Check the log for details.")
            logging.error(f"Request exception: {e}")


if __name__ == "__main__":
    menu()