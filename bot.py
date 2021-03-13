import os
import discord
from botinfo import *
from discord.ext import commands

botPrefix = "."
client = commands.Bot(command_prefix = botPrefix)

@client.event # function decorator, representa que a função é um evento
async def on_ready():
    print("Tou vivo!")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension}.py")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension}.py")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}.py")

# o nome da função é o nome do comando
@client.command()
async def ping2(ctx): # ctx = context
    await ctx.send(f"Pong!! {client.latency * 1000}ms") # ping em milisegundos

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}") # tudo menos a extensão

client.run(token)
