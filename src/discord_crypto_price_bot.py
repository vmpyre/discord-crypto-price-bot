import requests
import discord
from discord.ext import tasks

# ADD DISCORD BOT TOKEN HERE
DISCORD_BOT_TOKEN = "ADD DISCORD BOT TOKEN HERE"

client = discord.Client()

# Function that fetches live crypto token price from the MEXC exchange.
def token_price(ticker = 'CHICKS'):
    mrkt_url = 'http://mexc.com/open/api/v2/market/ticker'
    ticker1 = ticker
    ticker2 = 'USDT'

    try:
        response = requests.get(url=mrkt_url, params={'symbol':ticker1+'_'+ticker2})
	
        if response.status_code == 200:
            response_json = response.json()
            last_price = response_json['data'][0]['last']
            return last_price

        else:
            print("Status code: " + str(response.status_code))  

    except IndexError as error:
        print("IndexError: " + str(error))

# Runs the token_price() function and updates the price as the bot status every 5 seconds.
@tasks.loop(seconds=5)
async def switch_presence():
    current_price = token_price()
    if current_price is not None: 
        try:
            activity = discord.Game(name='$'+ current_price, type=3)
            await client.change_presence(status=discord.Status.online, activity=activity)

        except Exception as e:
            print("ERROR LOGGING - Status change fail: " + str(e))
    
    else:
        print("ERROR LOGGING - current_price is NoneType")

@client.event
async def on_ready():
    try:
        switch_presence.start()
    except Exception as e:
        print("ERROR LOGGING - Status change fail: " + str(e))

client.run(DISCORD_BOT_TOKEN)
