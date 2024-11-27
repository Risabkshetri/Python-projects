import requests

def get_weather(city):
    api_key = "b5478d0c09ed029557c7db217ffedb62"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        if "main" in data and "weather" in data:
            main = data["main"]
            weather = data["weather"]
            description = weather[0]["description"]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]

            print(f"City: {city}")
            print(f"Temperature: {temperature}K")
            print(f"Weather: {description}")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
        else:
            print("Weather data not found for the given city.")
    else:
        print("City Not Found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
