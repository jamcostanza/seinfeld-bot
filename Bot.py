from discord.ext import commands
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from datetime import datetime
from requests import get as request
import random
import discord
import os
import settings
import dotenv
import urllib.request

# Load discord token (API) from env file
load_dotenv()
DISCORD_TOKEN = settings.TOKEN

# Change the !help from no category to commands
help_command = commands.DefaultHelpCommand(
    no_category='Commands'
)

# Load intents
intents = discord.Intents.default()
intents.message_content = True

# Define discord bot and discord client
bot = commands.Bot(command_prefix='!', intents=intents, help_command=help_command)

# Variables
script_directory = os.path.abspath(os.path.dirname(__file__))  # Get script directory


# Command to send random image from images directory


@bot.command(name='seinfeldimage', help='Send random image to chat')
async def seinfeldimages(ctx):
    seasons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    season = random.choice(seasons)
    episode = None

    if season == 1:
        s1_episodes = [1, 2, 3, 4, 5]
        episode = random.choice(s1_episodes)
        if episode in [0, 1, 2, 3, 4, 5]:
            episode = '0' + str(episode)
    elif season == 2:
        s2_episodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        episode = random.choice(s2_episodes)
        if episode in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            episode = '0' + str(episode)
    elif season == 3:
        s3_episodes = list(range(1, 24))
        episode = random.choice(s3_episodes)
        if episode in [15, 16]:
            episode = '15-16'
        if episode in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            episode = '0' + str(episode)
    elif season in [5, 8]:
        s5_episodes = list(range(1, 23))
        episode = random.choice(s5_episodes)
        if episode in [19, 20]:
            episode = '19-20'
        if episode in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            episode = '0' + str(episode)
    elif season in [4, 6, 7, 9]:
        s4_episodes = list(range(1, 25))
        episode = random.choice(s4_episodes)
        if episode in [3, 4]:
            episode = '03-04'
        elif episode in [23, 24]:
            episode = '23-24'
        elif season == 6 and episode in [14, 15]:
            episode = '14-15'
        elif season == 7 and episode in [14, 15]:
            episode = '14-15'
        elif season == 7 and episode in [21, 22]:
            episode = '21-22'
        elif season == 9 and episode in [21, 22]:
            episode = '21-22'
        elif season == 9 and episode in [23, 24]:
            episode = '23-24'
        if episode in [0, 1, 2, 5, 6, 7, 8, 9]:
            episode = '0' + str(episode)

    frame = str(random.randint(1, 1292)).zfill(4)
    imgURL = "https://seinfeld-seinfeld-seinfeld.s3.amazonaws.com/S0{}E{}/screens/{}.jpg".format(season, episode, frame)

    print(imgURL)
    image = urllib.request.urlretrieve(imgURL, "/Users/jam/Desktop/SeinfeldBot/seinfeld.jpg")
    all_files = os.listdir("/Users/jam/Desktop/SeinfeldBot/")
    # Choose random image and add path to it
    random_image = "/Users/jam/Desktop/SeinfeldBot/seinfeld.jpg"

    await ctx.send(file=discord.File(random_image))


@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))

bot.run(settings.TOKEN)