import discord
import os
import requests
import json
import flask
import random
from keep_alive import keep_alive
from discord.utils import get

client = discord.Client()

ella_words = ["joke", "joking", "jk", "fat second", "let us in the penthouse", "stfu", "quirky", ]

ella_responses = [
  "Kys",
  "no"
]


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
    await message.channel.send('Welcome. BTW your are adopted.')

  if message.content.startswith('github-repo'):
    await message.channel.send('My repo is https://github.com/Charmander1011/ConeCock-Bot now go kys.')
  
  if any(word in message.content for word in ella_words):
    await message.channel.send(random.choice(ella_responses))
  
  if message.content.startswith('kys'):
    await message.channel.send('no you')


keep_alive()
client.run(os.getenv('TOKEN'))