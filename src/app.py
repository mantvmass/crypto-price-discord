import discord
import sys
from keys import tokens_discord
from discord.ext import commands
sys.path.append('/home/mantvmass/Desktop/crypto_price/src/api')
from coinmarketcap_api import *
from coingecko_api import check_push



bot = commands.Bot(command_prefix='!',help_command=None)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    
@bot.command()
async def send(ctx):
    print(ctx.channel)
    await ctx.channel.send('Hello')

@bot.command()
async def price(ctx, symbol):
    print("Coin:",symbol)
    price = check_push()
    usd = list(price.usd(symbol))
    thb = list(price.thb(symbol))
    emBed = discord.Embed(title=f"Symbol: {symbol.upper()}",url="https://media.com", description=f"Current Price: {usd[0]} {usd[1]}\nราคาไทย: {thb[0]} {thb[1]}\nWebSite: ", color=0x42f5a7)
    emBed.set_footer(text='Powered by mantvmass', icon_url='https://avatars.githubusercontent.com/u/32133224?s=96&v=4')
    await ctx.channel.send(embed=emBed)

    

    
    





bot.run(tokens_discord)