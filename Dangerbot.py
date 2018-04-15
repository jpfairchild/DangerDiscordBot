# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="DangerBot", command_prefix="$", pm_help=False)


@client.event
async def on_ready():
  print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
  print('--------')
  print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
  print('--------')
  print('Use this link to invite {}:'.format(client.user.name))
  print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
  return await client.change_presence(game=discord.Game(name='v3 please'))  # This is buggy, let us know if it doesn't work.


@client.event
async def on_message(message):
  if message.content.startswith('$hello'):
    await client.send_message(message.channel, 'SPENCER MEK NOW')
    msg = await client.wait_for_message(author=message.author, content='to hello')
    await client.send_message(message.channel, 'plz Hello.')


# @client.command()
# async def ping(*args):

#   await client.say("SPENCER MEK NOW!!")
#   await asyncio.sleep(3)

# hello = "hello"


# async def ping(hello):

#   await client.say("Oh hi")
#   await asyncio.sleep(3)


client.run('NDA3MzA5NDQwMzEyOTM0NDEw.DbRUGw.lL3KVWP_8PDd7Ljou1FTQo-biQU')
