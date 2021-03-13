import discord
from discord.ext import commands
from discord.utils import get

class PingPong(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.pingCount = 0
        self.pongCount = 0

    # Commands
    #@client.event # já não é assim
    @commands.command()
    async def ping(self, ctx):
        responses = [ # Para podermos adicionar mais no futuro
            "pong!",
            "PONG!",
            "PONG CARALHO! QUERES QUE EU REPITA ESTA MERDA MAIS VEZES?",
            "LEVAS UMA LASTÍBIA, COLO-TE A PUTA DA CARA AO CU!"
        ]
        await ctx.send(responses[self.pingCount])
        self.pingCount += 1
        if self.pingCount > 4:
            self.pingCount = 0

    @commands.command()
    async def pong(self, ctx):
        responses = [ # Para podermos adicionar mais no futuro
            "ping!",
            "PING!",
            "PING CARALHO! QUERES QUE EU REPITA ESTA MERDA MAIS VEZES?",
            "LEVAS UMA LASTÍBIA, COLO-TE A PUTA DA CARA AO CU!"
        ]
        await ctx.send(responses[self.pongCount])
        self.pongCount += 1
        if self.pongCount > 4:
            self.pongCount = 0

def setup(client):
    client.add_cog(PingPong(client))
