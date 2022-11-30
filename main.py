import requests
import json
import os.path
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
        

base_url = 'https://api.openweathermap.org/data/2.5/weather?units=metric&lat={}&lon={}&appid={}'
location_url = 'http://api.openweathermap.org/geo/1.0/reverse?lat={}&lon={}&appid={}'

def config():
    if os.path.exists('config.json'):
        return json.load(open('config.json'))
    else:
        print("Hello! This script uses the OpenWeatherMap API. Please create an account at https://home.openweathermap.org/users/sign_up and find your API key.")
        api_key = input("Please input API key: ")
        lat = input("Please input the latitude of your location: ")
        lon = input("Please input the longtitude of your location: ")
        time = int(input("How many seconds in between each message? (In seconds): "))
        # convert into json and save as config.json
        data = {'apikey': api_key, 'lat': lat, 'lon': lon, 'interval': time}
        with open('config.json', 'w') as f:
            json.dump(data, f)
cfg = config()

def discordweather(lat, lon, api_key):
    response = requests.get(base_url.format(lat, lon, api_key))
    countryname = requests.get(location_url.format(lat, lon, api_key))
    jsonResponse = response.json()
    
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1047467591381295154/2q1izZ9xgH3GnMvKlHr6N3h9m26z7rB4G9OWld2-470Y-vxhhPcHJxytpB68EqjIGjZn')
    embed = DiscordEmbed(
        title='Weather right now in ' + str(countryname.json()[0]["name"]) + ", " + str(countryname.json()[0]["country"]),
        description='Temperature: ' + str(jsonResponse['main']["temp"]) + " ℃ \nFeels like: " + str(jsonResponse['main']["feels_like"]) + " ℃ \nHumidity: " + str(jsonResponse['main']["humidity"]) + "%",
        color='03b2f8'
    )

    # add embed object to webhook
    webhook.add_embed(embed)

    webhook.execute()

while True:
    discordweather(cfg["lat"], cfg["lon"], cfg["apikey"])
    time.sleep(cfg["interval"])