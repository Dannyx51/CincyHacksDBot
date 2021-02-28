from asyncio.tasks import as_completed
from asyncio.windows_events import INFINITE
from discord.ext import tasks, commands
import asyncio
import speech # <---- imports speech.py
import discord
import time # < ---- apparently not used?
import interval as rep
import safe

iD = 815383522251374613

# Bot checks whether user input has changed
client = discord.Client() 

@client.event
async def p2D(text):
    global loop
    #await client.wait_until_ready
    channel = client.get_channel(iD)

    try:
        await channel.send(text)                    ###ISSUE WITH bOut!!!!!!! bOut!!!!!!!
    except Exception as e:
        print("----- " + "Error: {0}".format(e) + " -----")

        check.stop()                             # <---- ends processes to prevent spamming the error
        speech.stop_listening(wait_for_stop=False)

s1 , s2 = "", ""

@tasks.loop(seconds = 1)
async def check(): #Checks to see if out has had any changes
    print("Entered check()")
    global s1, s2                         # may cause problems

    bOut = speech.sent.lower()                  #Updates bOut with changes from speech.py
    
    s2 = bOut                                   #s2 declared to check change in sentences !!!DO NOT MOVE

    if s1 != s2: #bOut != speech.sent.lower():
        # Next step: output these commands to discord 
        print("Entered If")

        if ("goodnight" or "good night") in bOut: 
            wake = False
            speech.stop_listening(wait_for_stop=False)
            check.stop()
            value = "sleep"
            try:
                await p2D(bOut)
            except Exception as e:
                print("Error: {0}".format(e))
        elif "test" in bOut:
            print("Entered test")
            await p2D("Testing... Testing...")
        elif "party" in bOut:
            print("Entered party")
            await p2D("It's party time!")
        elif "jump" in bOut:
            print("entered jump")
            await p2D("We're jumping super high!")
        elif "python" in bOut:
            print("Entered python")
            await p2D("Better than js")
    await asyncio.sleep(1)
                            
    s1 = bOut                                   #s1 declared to check change in text !!!DO NOT MOVE

@check.before_loop
async def preCheck():
    await client.wait_until_ready()

# def stop():
#     task.cancel()

@client.event
async def on_ready():
    #global task, loop
    #global interval
    print('We have logged in as {0.user}'.format(client))

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
        #await check()
        await message.channel.send("Hello!")
    elif message.content.startswith('!wake'):   #Wakes the bot up
        # add line to not respond if already awake and vise versa 
        await message.channel.send('I have awoken!')
        wake = "True"
        speech.stop_listening(wait_for_stop=True)
        # loop.run_forever()
        # task = loop.create_task(check())
    elif message.content.startswith('!sleep'):  #Turns the bot off
        await message.channel.send("I'm taking a nap")
        wake = "False"
        speech.stop_listening(wait_for_stop=False)

print("do we get here")

check.start()
client.run(safe.token)
#wake = input() # "True"
print('[bot.py] bot is dead')
#loop.close()

# while True:
#     if wake == True:
        
#         print("Iterating...")
#     elif wake == False:
#         interval.stop()
#         print("Interval Stopping...")

# elif message.content.startswith('!'):
#         #Code