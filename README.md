# Discord Crypto Price Bot

Discord bot that pulls the latest price of a crypto token from the MEXC exchange and displays it as a status.

![image](https://user-images.githubusercontent.com/29526472/146332301-a3aa3423-9d5f-40c6-a12f-d09413f52c12.png)

## Installation

1. Install Python 3
```bash
sudo apt-get install python3
```

2. Since we are going to run the bot in a docker container so the first thing we are going to do is install docker.
Use the command below to install docker on Linux Ubuntu:

```bash
sudo apt install docker.io
```
2. Download the [source files](https://github.com/vmpyre/crypto-price-bot.git).


## Usage

1. Modify the source file **discord_crypto_price_bot.py** in the /src directory to add your Discord Bot Token (line 6 of the code) and the Crypto Ticker for which you want to pull the price (line 25 of the code).

```python
Line 5:    # ADD DISCORD BOT TOKEN HERE
Line 6:    DISCORD_BOT_TOKEN = "ADD DISCORD BOT TOKEN HERE"
```
```python
Line 28:   # Change the token name below to pull the live price
Line 29:   # Right now, it's set to pull the price of the token 'CHICKS'
Line 30:   current_price = token_price('CHICKS')
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

## Support
If you have any questions or feedback, feel free to message me on discord *Vmpyre#0505*
