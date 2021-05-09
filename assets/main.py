import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()

client = commands.Bot(
    command_prefix=os.environ['PREFIX'],
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

client.run(os.environ['TOKEN'])
