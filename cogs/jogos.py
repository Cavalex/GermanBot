import discord
from discord.ext import commands
import random

class Jogos(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    #@client.event # já não é assim
    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question): # * -> multiplos argumentos como 1
        responses = [
            "( ͡° ͜ʖ ͡°)", # A melhor resposta
            'É claro', 
            'É óbvio que sim', 
            'Sem dúvida', 
            'Definitivamente sim!', 
            'Acho que sim', 
            'Os deuses dizem-me que sim.', 
            'Provavelmente', 
            'Parece-me que sim.', 
            'Os sinais dizem que sim', 
            '¯\\_( ͡° ͜ʖ ͡°)_/¯', # A segunda melhor
            'Quem sabe?...', 
            'Os deuses disseram-me que não', 
            'É melhor não te responder por agora...', 
            'Acredita que não queres saber', 
            'Concentra-te e pergunta novamente', 
            'Não contes com isso', 
            'Não', 
            'As minhas fontes dizem que não', 
            'Não me parece...',
            'Muito duvidoso'
            ]
        await ctx.send(f"Pergunta: {question}\nResposta: {random.choice(responses)}")

def setup(client):
    client.add_cog(Jogos(client))