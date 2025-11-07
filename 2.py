import requests

if __name__ == "__main__":
    city_name = input()
    api_key = input()

    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={5}&appid={api_key}"
    print(geo_url)
    resp = requests.get(url=geo_url)
    print(resp.json())
