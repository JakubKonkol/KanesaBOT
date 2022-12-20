from modules.openAI import *

def botCommands(client):
    @client.command()
    async def ask(ctx, *, message):
        await ctx.send("bro im thinking...")
        try:
            response = openai_answer(message)
        except:
            response = "There was an error with the API, not my fault"
        await ctx.send("```"+response+"```")

    # command to ask openai and return the answer in the private message
    @client.command()
    async def askdm(ctx, *, message):
        try:
            response = openai_answer(message)
        except:
            response = "There was an error with the API, not my fault"
        await ctx.author.send("```"+response+"```")
