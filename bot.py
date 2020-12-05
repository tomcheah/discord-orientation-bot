# bot.py
import os, random
import discord
from discord.ext import commands

# Token and guild setup
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

# constants
DEFAULT_ROLE = 'undergraduate student'

# bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Events 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="CS Lectures"))
    print(f'{bot.user.name} is ready for classes!')

@bot.event
async def on_member_join(member):
    await member.send(
        f'Congratulations {member.name}, you have been admitted to {GUILD}!'
    )
    try:
        await bot.add_roles(member, discord.utils.get(member.guild.roles, name=DEFAULT_ROLE)) 
    except Exception as e:
        # await ctx.send('Cannot assign role. Error: ' + str(e))
        print(str(e))

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
    
#     if message.content == 'test!':
#         response = "Hi, this is a test."
#         await message.channel.send(response)

# Commmands 
# @bot.command(name='test', pass_context=True)
# async def test(ctx):
#     print("Is this working?")
#     response = "Hi, this is a test."
#     await ctx.send(response)

@bot.command(name='test', pass_context=True)
async def _test(ctx, arg):
    await ctx.send(arg)

bot.run(TOKEN)
