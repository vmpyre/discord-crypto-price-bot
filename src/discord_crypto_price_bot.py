import requests
import discord
from discord.ext import tasks

# ADD DISCORD BOT TOKEN HERE
DISCORD_BOT_TOKEN = "ADD DISCORD BOT TOKEN HERE"

client = discord.Client()

# Function that fetches live crypto token price from the MEXC exchange.
def token_price(ticker):
    mrkt_url = 'http://mexc.com/open/api/v2/market/ticker'
    ticker1 = ticker
    ticker2 = 'USDT'
    response = requests.get(url=mrkt_url, params={'symbol':ticker1+'_'+ticker2})
    response_json = response.json()
    last_price = response_json['data'][0]['last']
    return last_price

# Runs the token_price() function and updates the price as the bot status every 5 seconds.
@tasks.loop(seconds = 5)
async def switch_presence():
    # Change the token name below to pull the live price
    # Right now, it's set to pull price of the token 'CHICKS'
    current_price = token_price('CHICKS')
    
    activity = discord.Game(name='$'+ current_price, type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_ready():
    switch_presence.start()

client.run(DISCORD_BOT_TOKEN)
