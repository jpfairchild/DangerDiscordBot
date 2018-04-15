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
  if message.content.startswith('$spencer'):
    await client.send_message(message.channel, 'SPENCER MEK NOW')
    imageURL = "http://1.bp.blogspot.com/-jjrcg9oIe4M/UhMzgSuHdrI/AAAAAAAABSY/nrEQA4v3OwI/s1600/Dota+2+Mekanism.bmp"
    embed = discord.Embed()
    embed.set_image(url=imageURL)
    await client.send_message(message.channel, embed=embed)
    msg = await client.wait_for_message(timeout=5, content='lol')
    await client.send_message(message.channel, 'Yea, spencer let me die in Dota so many times')

  if message.content.startswith('$notice me senpai'):
    author = message.author
    authorid = message.author.id
    print("@{} user sent a message. (id: {})".format(author, authorid))

    if message.content == "$notice me senpai":
      print('I noticed you @{}!'.format(authorid))
      await client.send_message(message.channel, 'I noticed you @{} !'.format(author))
      imageURL = "https://media2.giphy.com/media/zZOakyWLMzDws/giphy.gif"
      embed = discord.Embed()
      embed.set_image(url=imageURL)
      await client.send_message(message.channel, embed=embed)


# @client.event
# async def on_message(message):
#     if message.content.startswith('$start'):
#         await client.send_message(message.channel, 'Type $stop 4 times.')
#         for i in range(4):
#             msg = await client.wait_for_message(author=message.author, content='$stop')
#             fmt = '{} left to go...'
#             await client.send_message(message.channel, fmt.format(3 - i))

#         await client.send_message(message.channel, 'Good job!')

# @client.command()
# async def ping(*args):

#   await client.say("SPENCER MEK NOW!!")
#   await asyncio.sleep(3)

# hello = "hello"


# async def ping(hello):

#   await client.say("Oh hi")
#   await asyncio.sleep(3)


client.run('NDA3MzA5NDQwMzEyOTM0NDEw.DbRUGw.lL3KVWP_8PDd7Ljou1FTQo-biQU')
