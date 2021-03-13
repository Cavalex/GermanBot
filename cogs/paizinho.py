import discord
from discord.ext import commands

class Paizinho(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    #@client.event # já não é assim
    @commands.command()
    async def comida(self, ctx): # * -> multiplos argumentos como 1
        paizinho = "<@636682510188675093>"
        await ctx.send(f"{paizinho} qual é a comida mais logo paizinho?")

def setup(client):
    client.add_cog(Paizinho(client))
