from asyncio.tasks import as_completed
import speech # <---- imports 
import discord
import os

print(speech.out)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        #Code
        await message.channel.send('Hello!') 
        # wowowow


client.run('ODE1MjUzMTIyOTQ2Njk1MTk4.YDptow.TSFqFcCulIK4GZ0wkf-GYl7GX_E')

# elif message.content.startswith('!'):
#         #Code