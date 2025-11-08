import requests
import sys

if __name__ == "__main__":
    city_name = input()
    api_key = input()

    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={5}&appid={api_key}"

    try:
        resp = requests.get(url=geo_url)
    except requests.RequestException as e:
        print(f"error: {e}")
        sys.exit(1)

    try:
        data = resp.json()
    except ValueError as e:
        print(f"error: {e}")

    lat = data[0].get("lat")
    lon = data[0].get("lon")

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    try:
        resp = requests.get(url=weather_url)
    except requests.RequestException as e:
        print(f"error: {e}")
        sys.exit(1)
    
    try:
        data = resp.json()
    except ValueError as e:
        print(f"error: {e}")
    
    temp = data.get("main")
    print(temp)