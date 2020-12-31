import discord
import os
import time
from web_server import keep_running
from discord.ext import commands
import random


adjetivos = ['MASIVO','EXORBITANTE','TITAN','UNIDAD ABSOLUTA','COLOSO','TANQUE','MONSTRO', 'NUNCA ENTRA', 'HEREJE', 'MANATI', 'MORSA', 'MARMOTA', 'GRASOSO', 'MUSICOTE', 'NO SE BANCA', 'GARRAFA', 'CALEFON', 'GIL', 'NABO']

game = discord.Game(".ayuda")
bot = commands.Bot(command_prefix='.')

@bot.command()
async def ayuda(ctx):
  await ctx.send("__**Comandos:**__")
  await ctx.send(".spam [usuario]")

@bot.command()
async def spam(ctx, user):
  for i in range(5):
    await ctx.send(user)
    time.sleep(2)


@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  await bot.change_presence(status=discord.Status.online , activity=game)


@bot.event 
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith("Jesus"):
    adj = random.randint(0,len(adjetivos)-1)
    await message.channel.send(adjetivos[adj])
  
  await bot.process_commands(message) #permite que los comandos se puedan "escuchar" 

keep_running()
bot.run(os.getenv("token"))
