import discord
import os

client = discord.Client()

@client.event

#ni idea
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event 

#help command
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(".help"):
    await message.channel.send("[descripcion del bot]\n\nComandos\n.spam [usuario]") 
    
client.run(os.getenv("token"))
