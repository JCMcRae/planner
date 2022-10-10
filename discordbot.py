import os

import discord
from discord.ext.commands import bot

intents = discord.Intents.default()
intents.message_contents = True
client = discord.Client(intents = intents)

TESTING_CHANNEL = os.getenv('TESTING_CHANNEL')

@client.event
async def on_ready():
    print(f'CYSTech PLNR has started up, running as {client.user}.')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$last'):
#         await message.channel.send('Hello!')

@bot.command()
async def last_post(ctx):
    await ctx.send('Last automated post: https://localhost/wp-content/uploads/2022/08/Test-Post.jpg')

def sendMessageToDiscord(message):
    channel = client.get_channel(TESTING_CHANNEL)
    channel.send(message)

def sendTestMessage():
    channel = client.get_channel(TESTING_CHANNEL)
    channel.send('THIS IS A TEST MESSAGE FROM PLNR.')