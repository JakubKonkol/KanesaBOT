#KanesaBOT v1.0.0
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import Bot.commands

PREFIX = ">"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intends = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, intents=intends)
intends.members = True

@client.event
async def on_ready():
    print(f'{client.user} Im here!')
if __name__ == '__main__':
    Bot.commands.botCommands(client)
    client.run(TOKEN)
