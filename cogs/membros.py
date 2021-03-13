import discord
from discord.ext import commands

class Membros(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # Events
    #@client.event # já não é assim
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} juntou-se ao servidor!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} saiu do servidor!")

def setup(client):
    client.add_cog(Membros(client))