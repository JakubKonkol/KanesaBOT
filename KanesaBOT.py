#KanesaBOT v1.0
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import openai
###################################################Setup################################################################
# Load .env files
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv('OPENAI_API_KEY')
# setting up discord bot
intends = discord.Intents.all()
client = commands.Bot(command_prefix='>', intents=intends)
intends.members = True
#set up openai
MODEL = "text-davinci-003"
TEMPERATURE = 0.9
MAX_TOKENS = 4000
#####################################################OpenAI_stuff#######################################################

# asking openai to generate a response
def openai_answer(message):
    completion = openai.Completion().create(model=MODEL, prompt=message, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    response = completion.choices[0].text
    return response
######################################################Bot_stuff##########################################################
#checking if everything is okay
@client.event
async def on_ready():
    print(f'{client.user} Im here!')

# bot command to ask openai and return the answer in the channel
@client.command()
async def ask(ctx, *, message):
    await ctx.send("bro im thinking...")
    try:
        response = openai_answer(message)
    except:
        response = "Theere was an error with the API, not my fault"
    await ctx.send("```"+response+"```")

# command to ask openai and return the answer in the private message
@client.command()
async def askdm(ctx, *, message):
    try:
        response = openai_answer(message)
    except:
        response = "Theere was an error with the API, not my fault"
    await ctx.author.send("```"+response+"```")
########################################################################################################################
#run the bot
client.run(TOKEN)
