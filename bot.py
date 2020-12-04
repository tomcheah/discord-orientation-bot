# bot.py
import os, random
import discord 
from discord.ext import commands

# Token and guild setup
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

# bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Events 
@bot.event
async def on_ready():
    print(f'{bot.user.name} has enrolled in {GUILD}!')

@bot.event
async def on_member_join(member):
    await member.send(
        f'Congratulations {member.name}, you have been admitted to {GUILD}!'
    )
    # set user role to undergraduatestudent

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'test!':
        response = "Hi, this is a test."
        await message.channel.send(response)

# Commmands 
@bot.command(name='test')
async def test(ctx):
    response = "Hi, this is a test."
    await message.channel.send(response)

bot.run(TOKEN)
