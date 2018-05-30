import time
import random
import asyncio

#-=-#discord#-=-#
import discord
from discord.ext.commands import Bot
from discord.ext import commands
bot = commands.Bot(command_prefix=';')

#-=-#recognition#-=-#
import speech_recognition as sr
#import Pyaudio


# get audio from the microphone
def startlistening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        print("You said " + r.recognize_google(audio))
        global answer
        answer = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
3





@bot.event
async def on_ready():
    print ("Ready!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='voice bot?'))


@bot.command(Pass_Context=True)
async def toggle():
   startlistening()
   await bot.say(answer)




bot.run("NDQ3NDA2NTE0MDEzOTk1MDA5.DeHHUA.gv8bretYcyeM9W-22xbq3HF7hwo")