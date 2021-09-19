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
  activity = discord.Game(name="with your Mom ;)", type=3)
  await client.change_presence(status=discord.Status.online, activity=activity)
  print("Ready")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Hello'):
    await message.channel.send('your are not loved.')
  
  if message.content.startswith('hello'):
    await message.channel.send('your are not loved.')

  if message.content.startswith('thank you'):
    await message.channel.send('Welcome. BTW Your are adopted.')


keep_alive()
client.run(os.getenv('TOKEN'))