import discord
import os
import requests
import json
import flask
from keep_alive import keep_alive
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
  activity = discord.Game(name="Sucking your Mom ;)", type=3)
  await client.change_presence(status=discord.Status.online, activity=activity)
  print("Ready")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Hello'):
    await message.channel.send('your are not loved.')


keep_alive()
client.run(os.getenv('TOKEN'))