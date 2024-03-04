import requests


# https://www.youtube.com/watch?v=baWzHKfrvqw
# print("This is a Weather API App")
# API Key d6d0f72fc1a27093423f960188c5bb11


api_key = "d6d0f72fc1a27093423f960188c5bb11"

user_input = input("Write name of a  City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)


weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']


print(weather,temp)