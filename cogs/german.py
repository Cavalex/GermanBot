import discord
from discord.ext import commands
from discord.utils import get
import random

german = "<@203838884608475137>"

class German(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    #@client.event # já não é assim
    @commands.command()
    async def calma(self, ctx):
        responses = [ # Para podermos adicionar mais no futuro
            "CALMA O CARALHO MEU! É SEMPRE A MESMA MERDA, NÃO VOU JOGAR MAIS ISTO, QUE MERDA DA JOGO!"
        ]
        await ctx.send(random.choice(responses))

    @commands.command()
    async def boralol(self, ctx):
        await ctx.send(f"{german} bora LOL pá!")

    @commands.command()
    async def boracs(self, ctx):
        await ctx.send(f"{german} bora CS pá!")
    
    @commands.command()
    async def lol(self, ctx):
        responses = [ # Para podermos adicionar mais no futuro
            "MERDA DE JOGO MEU, PUTA QUE PARIU A RIOT NÃO SABE FAZER CHAMPIONS DE JEITO, É QUE É SEMPRE A MESMA MERDA, UM GAJO QUER-SE DIVERTIR E É SEMPRE ISTO FODA-SE!"
        ]
        await ctx.send(random.choice(responses))

def setup(client):
    client.add_cog(German(client))
