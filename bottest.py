# from asyncio.tasks import as_completed
# from discord import channel
# import asyncio
# import discord.ext
# import speech # <---- imports speech.py
# import discord
# import time # < ---- apparently not used?
# import interval as rep
# import safe

# iD = 815246439860928547

# #For sending the values through
# value = ""
# send = False

# bOut = "empty" #this is bot.py's version of out, updated using check using speech.py's version
# print('[bot.py] bOut.equals(' + bOut + ')')
# wake = "False" # set back to false later

# # Bot checks whether user input has changed
# # text channel id = 815246439860928547
# s1 , s2 = "", ""
# async def check(): #Checks to see if out has had any changes
#     global s1, s2                               # may cause problems

#     bOut = speech.sent.lower()                  #Updates bOut with changes from speech.py
    
#     s2 = bOut                                   #s2 declared to check change in sentences !!!DO NOT MOVE

#     if s1 != s2: #bOut != speech.sent.lower():

#         # Next step: output these commands to discord 

#         if ("goodnight" or "good night") in bOut: 
#             wake = False
#             speech.stop_listening(wait_for_stop=False)
#             value = "sleep"
#             send = True
#             # asyncio.run(p2D("[bot.py] Sleeping now"))
        

#         elif "type" in bOut:
#             print("!!!!!")
#             print(iD)
#             channel = client.get_channel(iD)
#             value = "Typing"
#             send = True
#             #await p2D(bOut)                  # await = *sob*
#     s1 = bOut                                   #s1 declared to check change in text !!!DO NOT MOVE

# client = discord.Client()

# async def p2D(text):
#     await client.wait_until_ready
#     channel = client.get_channel(iD)
#     await channel.send(text)

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# # Bot reacts to user's message
# # 
# # @param message: discord reader/sender
# # 
# @client.event
# async def on_message(message): 
#     print(message)
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hello'):
#         #Code
#         # asyncio.run(p2D("YOOOO"))
#         await p2D("asdhjaksjdhas")
#     elif message.content.startswith('!wake'):   #Wakes the bot up
#         await message.channel.send('I have awoken!')
#         speech.stop_listening(wait_for_stop=True)
#     elif message.content.startswith('!sleep'):  #Turns the bot off
#         await message.channel.send("I'm taking a nap")
#         wake = "False"
#         speech.stop_listening(wait_for_stop=False)
        
# client.run(safe.token)
# #wake = input() # "True"
# print('[bot.py] wake.equals(' + wake +')')

# interval = rep.Interval(1,check)
# interval.start()
