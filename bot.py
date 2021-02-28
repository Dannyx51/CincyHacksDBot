from asyncio.tasks import as_completed
from discord import channel
import asyncio
import discord.ext
import speech # <---- imports speech.py
import discord
import time # < ---- apparently not used?
import interval as rep
import safe

iD = 815383522251374613

bOut = "empty" #this is bot.py's version of out, updated using check using speech.py's version
print('[bot.py] bOut.equals(' + bOut + ')')
wake = "False" # set back to false later

# Bot checks whether user input has changed
client = discord.Client()

@client.event
async def p2D(text):
    #await client.wait_until_ready
    channel = client.get_channel(iD)

    try:
        await channel.send(text)                    ###ISSUE WITH bOut!!!!!!! bOut!!!!!!!
    except Exception as e:
        print("----- " + "Error: {0}".format(e) + " -----")

        interval.stop()                             # <---- ends processes to prevent spamming the error
        speech.stop_listening(wait_for_stop=False)

s1 , s2 = "", ""
async def check(): #Checks to see if out has had any changes
    global s1, s2                               # may cause problems

    bOut = speech.sent.lower()                  #Updates bOut with changes from speech.py
    
    s2 = bOut                                   #s2 declared to check change in sentences !!!DO NOT MOVE

    if s1 != s2: #bOut != speech.sent.lower():
        # Next step: output these commands to discord 

        if ("goodnight" or "good night") in bOut: 
            wake = False
            speech.stop_listening(wait_for_stop=False)
            value = "sleep"
            try:
                await p2D(bOut)
            except Exception as e:
                print("Error: {0}".format(e))
        
        elif "test" in bOut:
            await p2D(bOut)
                            
    s1 = bOut                                   #s1 declared to check change in text !!!DO NOT MOVE

    


interval = rep.Interval(1,check)
@client.event
async def on_ready():
    #global interval
    print('We have logged in as {0.user}'.format(client))
    interval.start()

# Bot reacts to user's message
# 
# @param message: discord reader/sender
@client.event
async def on_message(message): 
    #print(message)
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        #Code
        #await p2D("YOOOO")
        await check()
    elif message.content.startswith('!wake'):   #Wakes the bot up
        # add line to not respond if already awake and vise versa 
        await message.channel.send('I have awoken!')
        wake = "True"
        speech.stop_listening(wait_for_stop=True)
    elif message.content.startswith('!sleep'):  #Turns the bot off
        await message.channel.send("I'm taking a nap")
        wake = "False"
        speech.stop_listening(wait_for_stop=False)
        
client.run(safe.token)
#wake = input() # "True"
print('[bot.py] bot is dead')
interval.stop()

# while True:
#     if wake == True:
        
#         print("Iterating...")
#     elif wake == False:
#         interval.stop()
#         print("Interval Stopping...")


# elif message.content.startswith('!'):
#         #Code