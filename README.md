# Discord Crypto Price Bot

Discord bot that pulls the latest price of a crypto token from the MEXC exchange and displays it as a status.

![alt text](https://github.com/vmpyre/discord-crypto-price-bot/blob/main/bot_status.PNG)
## Installation

1. Since we are going to run the bot in a docker container so the first thing we are going to do is install docker.
Use the command below to install docker on Linux Ubuntu:

```bash
sudo apt install docker.io
```
2. Download the [source files](https://github.com/vmpyre/crypto-price-bot.git).


## Usage

1. Modify the source file **discord_crypto_price_bot.py** to add your Discord Bot Token (line 6 of the code) and the Crypto Ticker for which you want to pull the price (line 25 of the code).

```python
Line 5:    # ADD DISCORD BOT TOKEN HERE
Line 6:    DISCORD_BOT_TOKEN = {ADD DISCORD BOT TOKEN HERE}
```
```python
Line 23:   # Change the token name below to pull the live price
Line 24:   # Right now, it's set to pull the price of the token 'CHICKS'
Line 25:   current_price = token_price('CHICKS')
```

2. Navigate to the /src directory and build the docker file using the following command:
```bash
sudo docker build -t discord-price-bot .
```

3. Run the docker container with your bot:
```bash
sudo docker run -d discord-price-bot
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.
