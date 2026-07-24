import requests
from config import API_KEY, BASE_URL, DEFAULT_CITY, UNITS

def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": UNITS
    }
    response = requests.get(BASE_URL, params=params)
    print("Request URL:", response.url)  # Debugging: Print the full request URL    
    if response.status_code == 200:
        return response.json()
    else:
        print("API request failed with status code:", response.status_code)
        print("Response:", response.text)
        return None

def extract_weather_details(data):
    if data:
        weather_details = {
            "city": data.get("name"),
            "temperature": data.get("main", {}).get("temp"),
            "humidity": data.get("main", {}).get("humidity"),
            "weather": data.get("weather", [{}])[0].get("description")
        }
        return weather_details
    else:
        return None

def main():
    city=input(f"Enter city name or press Enter for default ({DEFAULT_CITY}): ") or DEFAULT_CITY
    weather_data = get_weather_data(city)
    weather_details = extract_weather_details(weather_data)

if __name__ == "__main__":
    main()