import discord
from discord.ext import commands

import json
import requests
import os

with open('config.json') as f:
	json_file = json.load(f)

client = commands.Bot(
    command_prefix=json_file['prefix'],
    intents = discord.Intents.default()
)

@client.event
async def on_ready():
    print('-----------------')
    print('Bot is ready')
    print('-----------------')
    
for filename in os.listdir("./Cogs"):
  if filename.endswith(".py") and filename != "__init.py__":
    client.load_extension(f"Cogs.{filename[:-3]}")
    print(f"Loaded Cogs.{filename[:-3]}")

client.run(json_file['token'])
