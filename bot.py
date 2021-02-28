from discord.ext import tasks, commands
import asyncio
import speech # <---- imports speech.py
import discord
import time # < ---- apparently not used?
import safe

genID = safe.generalID
hydraID = safe.hydraID

client = discord.Client() 


@client.event
async def p2D(text, ID):
    channel = client.get_channel(ID)

    try:
        await channel.send(text)
    except Exception as e:
        print("----- " + "Error: {0}".format(e) + " -----")

        check.stop()                             # <---- ends processes to prevent spamming the error
        speech.stop_listening(wait_for_stop=False)

s1 , s2 = "", ""

@tasks.loop(seconds = 1)
async def check(): #Checks to see if out has had any changes
    # print("Entered check()")
    global s1, s2                               # the change check vars

    bOut = speech.sent.lower()                  #Updates bOut with changes from speech.py

    s2 = bOut                                   #s2 declared to check change in sent    ences !!!DO NOT MOVE

    if s1 != s2:
        if ("good night") in bOut: 
            wake = False
            speech.stop_listening(wait_for_stop=False)
            check.stop()
            value = "sleep"
            try:    
                await p2D("Sleeping", genID)
            except Exception as e:
                print("Error: {0}".format(e))
        
        elif ("goodnight") in bOut: 
            wake = False
            speech.stop_listening(wait_for_stop=False)
            check.stop()
            value = "sleep"
            try:    
                await p2D("Sleeping", genID)
            except Exception as e:
                print("Error: {0}".format(e))

        elif ("hello buddy" in bOut):
            # print("Entered test")
            await p2D("Hey! How are you doing?", genID)

        elif "weather" in bOut:
            # print("Entered party")
            await p2D("It's nice outside!", genID)
        
        elif "what do you do" in bOut:
            # print("entered jump")
            await p2D("I am a speech to text bot. I can recognize what you say, when you say it and push what you say to Discord!", genID)
        
        elif "python" in bOut:
            # print("Entered python")
            await p2D("Python: Better than js", genID)
        
        elif "javascript" in bOut:
            # print("Entered python")
            await p2D("Javascript: Better than py", genID)
        
        # play user inputted song with hyrda -- to be removed ?
        elif "help" in bOut:
            await p2D("I'm here to help! Just speak normally -- when I hear a keyword I will act accordingly!", genID)

        # elif "lo-fi" in bOut:
        #     await p2D("!clear 100", genID)
    
    await asyncio.sleep(1)
                            
    s1 = bOut                                   #s1 declared to check change in text !!!DO NOT MOVE

#Waits until bot is ready to start loop testing check()
@check.before_loop
async def preCheck():
    await client.wait_until_ready()

#Bot has successfully logged in and is ready to go!
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your voices"))


# Bot reacts to user's message
# 
# @param message: discord reader/sender
@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send("Hello!")

    elif message.content.startswith('!wake'):        #Wakes the bot up
        await message.channel.send('I have awoken!')
        wake = "True"
        speech.stop_listening(wait_for_stop=True)

    elif message.content.startswith('!sleep'):       #Turns the bot off
        await message.channel.send("I'm taking a nap")
        wake = "False"
        speech.stop_listening(wait_for_stop=False)

check.start()
client.run(safe.token)