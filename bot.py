from asyncio.tasks import as_completed
import speech # <---- imports speech.py
import discord
import os
import schedule
import time
import interval as rep

bOut = "empty" #this is bot.py's version of out, updated using check using speech.py's version
print('[bot.py] bOut.equals(' + bOut + ')')
wake = "False" # set back to false later

# Bot checks whether user input has changed
# text channel id = 815246439860928547
def check(bOut):
    print("[bot.py] entered check() function")
    print('[bot.py] bOut.equals(' + bOut + ')')
    if (bOut != speech.out.lower()):    #Checks to see if out has had any changes
        print("[bot.py] entered if() statement")
        bOut = input()       #Updates bOut with changes
        if ("goodnight" or "good night") in bOut:
            wake = False
            speech.stop_listening(wait_for_stop=False)
            value = "sleep"
            print("[bot.py] Sleeping now")
        elif "type" in bOut:
            print("[bot.py] type is working")

client = discord.Client()

# Runs when the bot is successfully online, prints to console

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    wake = input()

# Bot reacts to user's message
# 
# @param message: discord reader/sender
# 
@client.event
async def on_message(message): 
    #print(message)
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        #Code
        await message.channel.send('Hello!')
    elif message.content.startswith('!wake'):   #Wakes the bot up
        await message.channel.send('I have awoken!')
        out = speech.out
        wake = "True"
        speech.stop_listening(wait_for_stop=True)
    elif message.content.startswith('!sleep'):  #Turns the bot off
        await message.channel.send("I'm taking a nap")
        wake = "False"
        speech.stop_listening(wait_for_stop=False)
        
client.run('')
#wake = input() # "True"
print('[bot.py] wake.equals(' + wake +')')

interval = rep.Interval(1,check(bOut))

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("Stopping...")
        interval.stop()
        break
        
    
#Bot checks whether user input has changed
# if wake == "True":
#     schedule.every(10).seconds.do(check(bOut))


# elif message.content.startswith('!'):
#         #Code