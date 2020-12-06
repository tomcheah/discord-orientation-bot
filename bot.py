# bot.py
import os, random
import discord
from discord.ext import commands

# Token and guild setup
TOKEN = os.environ['DISCORD_TOKEN']
GUILD_NAME = os.environ['DISCORD_GUILD']

# constants
DEFAULT_ROLE = 'undergraduate student'
BOT_ID = 784307177203433482
GUILD_ID = 189037684423917569

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
        f'Congratulations {member.name}, you have been admitted to {GUILD_NAME}!'
    )
    try:
        role = discord.utils.get(member.server.roles, id="322178691134128139")
        await bot.add_roles(member, role)
    except Exception as e:
        # await ctx.send('Cannot assign role. Error: ' + str(e))
        print(str(e))

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
