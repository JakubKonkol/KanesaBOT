import shutil
from modules.LolController import *
import requests

from modules.openAI import *

def botCommands(client):
    @client.command()
    async def ask(ctx, *, message):
        await ctx.send("🧠 I'm thinking...")
        try:
            response = openai_answer(message)
        except:
            response = "There was an error with the API, not my fault"
        await ctx.send("```"+response+"```")

    @client.command()
    async def askdm(ctx, *, message):
        try:
            response = openai_answer(message)
        except:
            response = "There was an error with the API, not my fault"
        await ctx.author.send("```"+response+"```")

    @client.command()
    async def image(ctx, *, message):
        await ctx.send("⚙ Generating image...")
        try:
            image_url = generate_image(message)
        except:
            image_url = "There was an error with the API, not my fault"
        await ctx.send(image_url)

    @client.command()
    async def stats(ctx, *, summonerName):
        summoner = Summoner(summonerName)
        await ctx.send("```"+summoner.getSummonerStats()+"```")

