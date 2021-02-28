# What is this?

This bot was created for the 2021 CincyHacks hackathon. It takes in live audio input, then converts it to text through Google's speech API.
Using this text, we control a discord bot, essentially a voice assistant but for discord.

# How to run

1. If you would like to run this bot yourselves, you will need to download all the project files, and create another file to use.

2. The bot token and channel IDs have been implemented in a "safe.py", and so create one following the template below in the same directory as the rest of the project
```python

generalID = 123456789012345678 #<--- channel id of where you want the bot to talk
token = '[your bot token here]'

```
3. Run bot.py, and you should be good to go!