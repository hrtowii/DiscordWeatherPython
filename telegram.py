# write a telegram bot that will send the weather to a telegram channel using the python-telegram-bot package
import telegram
import logging
import asyncio
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

#logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! This script uses the OpenWeatherMap API and Discord Webhooks API. For OpenWeatherMap, please create an account at https://home.openweathermap.org/users/sign_up and find your API key.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="For Discord Webhooks, go to your Discord Server -> Server Settings -> Integrations -> Webhooks, create a webhook, and copy the webhook link.")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="placeholder")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="placeholder")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="placeholder")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="placeholder")
    
async def unknownMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")



#start
if __name__ == '__main__':
    from telegram import Update
    application = ApplicationBuilder().token('5436275337:AAHTw8JvXpqk_vhTp2ODmibrHG9yeDqt0uM').build()
    start_handler = CommandHandler('start', start)
    weather_handler = CommandHandler('weather', weather)
    unknown_handler = MessageHandler(filters.COMMAND, unknownMessage)
    application.add_handler(start_handler)
    application.add_handler(weather_handler)
    application.add_handler(unknown_handler)
    application.run_polling()


# async def main():
#     bot = telegram.Bot(token='5436275337:AAHTw8JvXpqk_vhTp2ODmibrHG9yeDqt0uM')
#     async with bot:
#         print((await bot.get_updates())[0])




    
# def telegram():
#     response = requests.get(base_url.format(cfg["lat"], cfg["lon"], cfg["api_key"]))
#     countryname = requests.get(location_url.format(cfg["lat"], cfg["lon"], cfg["api_key"]))
#     jsonResponse = response.json()
#     bot.send_message(chat_id='', text='Weather right now in {}, {} '.format(str(countryname.json()[0]["name"]), str(countryname.json()[0]["country"])))
#     bot.send_message(chat_id='', text='Temperature: {}℃'.format(str(jsonResponse['main']["temp"])))
#     bot.send_message(chat_id='', text='Feels like: {}℃'.format(str(jsonResponse['main']["feels_like"])))
#     bot.send_message(chat_id='', text='Relative Humidity: {}%'.format(str(jsonResponse['main']["humidity"]))) # magic