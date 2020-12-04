# bot.py
import os 

import discord 
from dotenv import load_dotenv

# intents
intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has enrolled in {GUILD}!')

@client.event
async def on_member_join(member):
    await member.send(
        f'Congratulations {member.name}, you have been admitted to {GUILD}!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'test!':
        response = "Hi, this is a test."
        await message.channel.send(response)

client.run(TOKEN)
