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
        print("Hello! This script uses the OpenWeatherMap API and Discord Webhooks API. For OpenWeatherMap, please create an account at https://home.openweathermap.org/users/sign_up and find your API key.\n For Discord Webhooks, go to your Discord Server -> Server Settings -> Integrations -> Webhooks, create a webhook, and copy the webhook link.")
        api_key = input("Please input API key: ")
        discord_api_key = input("Please paste your webhook API link: ")
        lat = input("Please input the latitude of your location: ")
        lon = input("Please input the longtitude of your location: ")
        time = int(input("How many seconds in between each message? (In seconds): "))
        # convert into json and save as config.json
        data = {'api_key': api_key, 'discord_api_key': discord_api_key, 'lat': lat, 'lon': lon, 'interval': time}
        with open('config.json', 'w') as f:
            json.dump(data, f)

cfg = config()

def discordweather(lat, lon, api_key):
    response = requests.get(base_url.format(lat, lon, api_key))
    countryname = requests.get(location_url.format(lat, lon, api_key))
    jsonResponse = response.json()
    
    webhook = DiscordWebhook(url=cfg["discord_api_key"])
    embed = DiscordEmbed(
        title='Weather right now in {}, {} '.format(str(countryname.json()[0]["name"]), str(countryname.json()[0]["country"])),
        color='03b2f8',
        fields=[{
            "name": "Temperature", 
            "value": str(jsonResponse['main']["temp"]) + "℃",
            "inline": False
        },
        {
            "name": "Feels like",
            "value": str(jsonResponse['main']["feels_like"]) + "℃",
            "inline": False
        },
        {
            "name": "Relative Humidity",
            "value": str(jsonResponse['main']["humidity"]) + "%",
            "inline": False
        }],
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    )

    # add embed object to webhook
    webhook.add_embed(embed)

    webhook.execute()

try:
    while True:
        discordweather(cfg["lat"], cfg["lon"], cfg["api_key"])
        time.sleep(cfg["interval"])
except KeyboardInterrupt:
    print("Exiting...")
    
