import os, random
import discord
from discord.ext import commands

# Environment variables setup
TOKEN = os.environ['DISCORD_TOKEN']
DEFAULT_ROLE_ID = int(os.environ['DEFAULT_ROLE_ID'])
GUILD_ID = int(os.environ['GUILD_ID'])

# Constants
BURRITOS_URL_LIST = [
    'https://www.theseasonedmom.com/wp-content/uploads/2018/02/The-Easiest-Burrito-Recipe-7.jpg',
    'https://thegirlonbloor.com/wp-content/uploads/2015/03/Pulled-Chicken-Burrito-2.jpg',
    'https://www.thespruceeats.com/thmb/AAnECK7pIP9DrvVOFlM2CRRndWM=/4048x2696/filters:fill(auto,1)/vegetarian-bean-and-rice-burrito-recipe-3378550-hero-01-40ecbc08fcc84e80b8be853c1b779a13.jpg',
    'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2018/10/16/0/DV2904_Korean-BBQ-Burrito_s4x3.jpg.rend.hgtvcom.826.620.suffix/1539714414867.jpeg',
    'https://www.recipetineats.com/wp-content/uploads/2020/02/Chicken-Burritos_2.jpg',
    'https://www.freshcravings.com/wp-content/uploads/2019/03/FC_recipe-burrito-1480x1480@2x.jpg',
    'https://veganinthefreezer.com/wp-content/uploads/2020/06/slow-cooker-black-bean-burrito-1200-sp.jpg',
    'https://www.cookingclassy.com/wp-content/uploads/2019/08/breakfast-burrito-01-500x500.jpg',
    'https://pinchofyum.com/wp-content/uploads/Mega-Burritos-Feature-3.jpg',
    'https://www.alsothecrumbsplease.com/wp-content/uploads/2018/01/Guacamole-Beef-Burrito-4-500x375.jpg',
    'https://d2wtgwi3o396m5.cloudfront.net/recipe/18ad844d-2449-463e-9f52-7482cacc6a9b.jpeg?d=1408x1120',
    'https://instantpoteats.com/wp-content/uploads/2019/11/instant-pot-burritos-square-4.jpg',
    'https://dinnerthendessert.com/wp-content/uploads/2018/08/Beef-Burrito.jpg',
    'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/2/14/0/FNK_breakfast-burrito_s4x3.jpg.rend.hgtvcom.826.620.suffix/1382542427230.jpeg',
    'https://www.gannett-cdn.com/-mm-/c256be877cb5feb7b087db5c94efb4583aa6062e/c=5-0-1277-719/local/-/media/Phoenix/Phoenix/2014/04/15//1397603744000-chipotle-tofu-burrito.jpg',
    'https://www.godairyfree.org/wp-content/uploads/2017/10/Vegan-Burgers-Burritos-Chipotle-and-Lime-Burrito-feature-1.jpg',
    'https://s3-media0.fl.yelpcdn.com/bphoto/X24hfq87HN_YInOJXp8E_g/l.jpg',
]
DAD_JOKES = [
    '6:30 is my favorite time of day, hands down.',
    "Why shouldn't you wear glasses when you play football? Because it's a contact sport.",
    "I took up origami for a while, but I gave it up because it was too much paperwork.",
    "What does Alexander the Great and Winnie the Pooh have in common? They both have the same middle name.",
    "I love my furniture. My recliner and I go way back.",
    "You know Orion’s Belt? Big waist of space, huh?",
    "I tell dad jokes. Sometimes he laughs.",
    "If a child doesn't want to take a nap, are they guilty of resisting a rest?",
    "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
    "I don't trust stairs. They're always up to something.",
    "Did you hear the rumor about butter? Well, I'm not going to spread it!",
    "Why don't eggs tell jokes? They'd crack each other up.",
    "Why did the math book look so sad? Because of all of its problems!",
    "I'm on a seafood diet. I see food and I eat it.",
    "What’s an astronaut’s favorite part of a computer? The space bar.",
    "I made a pencil with two erasers. It was pointless.",
    "What do you call a fake noodle? An impasta.",
    "I could tell a joke about pizza, but it's a little cheesy.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
]

# Bot setup
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
        f'Congratulations {member.name}, you have been admitted to {member.guild.name}!'
    )
    try:
        default_role = discord.utils.get(member.guild.roles, id=DEFAULT_ROLE_ID)
        await member.add_roles(default_role)
    except Exception as e:
        print('Cannot assign role. Error: ' + str(e))
    else: 
        print('Successfully assigned ' + str(default_role) + ' to ' + str(member.name))

# Commmands 
@bot.command(name='dadjoke', pass_context=True)
async def dad_joke(ctx):
    dad_joke = DAD_JOKES[random.randint(0, len(DAD_JOKES)-1)]
    await ctx.send(dad_joke)

@bot.command(name='echo', pass_context=True)
async def echo(ctx, *, msg):
    await ctx.send(msg)

@bot.command(name='listmembers', pass_context=True)
async def listmembers(ctx, *, role):
    # check if role exists 
    guild_role = discord.utils.get(ctx.guild.roles, name=role)
    if guild_role is None:
        await ctx.send(role + " role doesn't exist. Please try again with an existing role.")
        return

    list_members = []
    for member in ctx.guild.members: 
        if guild_role in member.roles:
            if member.nick is None: 
                list.members.append(member.name)
            else:
                list_members.append(member.nick)
    list_members_string = ', '.join(map(str, list_members))
    await ctx.send("Members who have the " + role + " role: " + list_members_string)

@bot.command(name='megaburrito', pass_context=True)
async def megaburrito(ctx):
    burrito_url = BURRITOS_URL_LIST[random.randint(0, len(BURRITOS_URL_LIST)-1)]
    await ctx.send(burrito_url)

# @bot.command(name='welcome', pass_context=True)
# async def welcome(ctx, arg):
#     # !welcome @cuttles

bot.run(TOKEN)