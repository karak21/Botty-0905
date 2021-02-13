import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

# Imports end

intents = discord.Intents.default()    # Enable all intents except for members and presences
intents.members = True  # Subscribe to the privileged members intent.

client = commands.Bot(
    command_prefix='.',
    intents=intents)


@client.event   
async def on_ready():
    print('Bot is ready!')
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_message(message): #ping command to test if the bot works
    # NEW CODE HERE ##################
    await client.process_commands(message)
    ###################################
    if message.author == client.user:
        return
    if message.content.startswith('.ping'):
        await message.channel.send('pong')
        print('Command ".ping" is working!')

@client.command() #Personalized hello command (WIP)
async def hi(ctx):
  # Switched to a try/except block, told me that this command was never being recognized. Hence the previous addition in on_message. Credits: Seto_Kibah
  try:
    await ctx.send(f"Hello, {ctx.author.name}!")
    print ('Command .hi is working!')
  except:
    print('Command ".hi" could not run...')


keep_alive()
client.run(os.getenv('TOKEN'))
