#Legitbot by Dith#8685
import time
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print ("Ready!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name=';info or ;help'))

@bot.command(pass_context = True)
async def purge(ctx, number):
    purge_msg = await bot.say("**I am deleting `{}` messages**".format(number))
    time.sleep(2)
    await bot.delete_message(purge_msg)
    time.sleep(0.1)
    mgs = [] #Empty list to put all the messages in the log
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number): #limit of messages your boi's gonna delete
        mgs.append(x)
    await bot.delete_messages(mgs)
    time.sleep(0.5)
    purge_msg = await bot.say(":arrow_right: I deleted `{}` messages".format(number))
    await bot.add_reaction(message=purge_msg, emoji='❌')
    await bot.wait_for_reaction(user=ctx.message.author, message=purge_msg, emoji='❌')
    await bot.delete_message(message=purge_msg)





#HELP/INFO
@bot.command(pass_context=True)
async def info(ctx):
    await bot.say(":arrow_right: **Information:** `Info` ~~`help`~~ `serverinfo` `userinfo {name}`")
    await bot.say(":arrow_right: **Utility:** `purge {message number}` `ping` ~~`freeze`~~")
    await bot.say(":arrow_right: **Fun:** `coinflip` `eightball`")


#ping
@bot.command(pass_context=True)
async def ping(ctx):
    ping_cmd_msg = await bot.say(":ping_pong: pong")
    print("user has pinged")
    await bot.add_reaction(message=ping_cmd_msg, emoji='❌')
    await bot.wait_for_reaction(user=ctx.message.author, message=ping_cmd_msg, emoji='❌')
    await bot.delete_message(message=ping_cmd_msg)





# USER INFO (finds the info of a discord user in the server)
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="id: {}".format(user.id), description="**Info found on {}**".format(user.name), color=0x00ff00)
    embed.add_field(name="UserStatus", value=user.status, inline=True)
    embed.add_field(name="UserRole", value=user.top_role, inline=True)
    embed.add_field(name="UserServerJoin", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    cancel_userinfo = await bot.say(embed=embed)
    await bot.add_reaction(message=cancel_userinfo, emoji='❌')
    await bot.wait_for_reaction(user=ctx.message.author, message=cancel_userinfo, emoji='❌')
    await bot.delete_message(message=cancel_userinfo)


#-------------------------------------------------------------#
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="server info", color=0x00ff00)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    serverinfo_cmd_msg = await bot.say(embed=embed)
    #cancel#
    await bot.add_reaction(message=serverinfo_cmd_msg, emoji='❌')
    await bot.wait_for_reaction(user=ctx.message.author, message=serverinfo_cmd_msg, emoji='❌')
    await bot.delete_message(message=serverinfo_cmd_msg)




#FUN
@bot.command(pass_context=True)
async def coinflip(ctx):
    coin = random.randint(1,2);
    if coin == 1:
        heads = await bot.say("**Flipping 🌓...**")
        time.sleep(0.5)
        await bot.edit_message(message=heads, new_content="**Flipping 🌑...**")
        time.sleep(0.5)
        await bot.edit_message(message=heads, new_content="**Flipping 🌕...**")
        time.sleep(0.5)
        await bot.edit_message(message=heads, new_content="**Flipping 🌑...**")
        time.sleep(0.5)
        await bot.edit_message(message=heads, new_content="**Heads! 🌕**")
    if coin == 2:
        tails = await bot.say("**Flipping 🌓...**")
        time.sleep(0.5)
        await bot.edit_message(message=tails, new_content= "**Flipping 🌕...**")
        time.sleep(0.5)
        await bot.edit_message(message=tails, new_content="**Flipping 🌑...**")
        time.sleep(0.5)
        await bot.edit_message(message=tails, new_content="**Flipping 🌕...**")
        time.sleep(0.5)
        await bot.edit_message(message=tails, new_content="**Tails! 🌑**")

@bot.command(pass_context=True)
async def eightball(ctx, arg):
    eightball = random.randint(1,4)
    if eightball == 1:
        eightball_cmd_msg = await bot.say("**rolling** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling.** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling..** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.2)
        await bot.edit_message(message=eightball_cmd_msg, new_content="as I see it... yes! :white_check_mark:")

    if eightball == 2:
        eightball_cmd_msg = await bot.say("**rolling** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling.** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling..** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.2)
        await bot.edit_message(message=eightball_cmd_msg, new_content="The answer to your question is... Yes :white_check_mark:")

    if eightball == 3:
        eightball_cmd_msg = await bot.say("**rolling** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling.** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling..** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.2)
        await bot.edit_message(message=eightball_cmd_msg, new_content="No it can not possibly be... :no_entry:")

    if eightball == 4:
        eightball_cmd_msg = await bot.say("**rolling** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling.** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling..** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.5)
        await bot.edit_message(message=eightball_cmd_msg, new_content="**rolling...** :8ball:")
        time.sleep(0.2)
        await bot.edit_message(message=eightball_cmd_msg, new_content="the answer to your question is... no :no_entry:")

    #re-roll#
    await bot.add_reaction(message=eightball_cmd_msg, emoji='↩')
    await bot.wait_for_reaction(user=ctx.message.author, message=eightball_cmd_msg, emoji='↩')
    eightball(ctx)


    #cancel#
    await bot.add_reaction(message=eightball_cmd_msg, emoji='❌')
    await bot.wait_for_reaction(user=ctx.message.author, message=eightball_cmd_msg, emoji='❌')
    await bot.delete_message(message=eightball_cmd_msg)




bot.run("NDMxMjI3NTgzMzQyODM3NzYw.Dabrhw.THK_qrUmPLybTEDKU2Jy1_HOTuw")
