import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from scraper import get_build

# Get token from environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHAMPIONS_LIST = os.getenv('CHAMPIONS_LIST')

# This represents the connection to discord
# Handle events, states and interacts with Discord API's
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# >>> START Bot as a Bot
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hi')
async def say_hi(ctx):
    await ctx.send(f'Saludos')


@bot.command(name='builder')
async def display_build(ctx, *args):
    args_len = len(args)
    champion, role, counter = '', '', ''

    match args_len:
        case 1:
            champion = args[0]
        case 2:
            champion, role = args[:2]
        case 3:
            champion, role, counter = args[:3]
        case _:
            await ctx.send(f'There is no champion i can look a build for.')
            return

    if champion.lower() not in CHAMPIONS_LIST.lower():
        await ctx.send(f'Champion not found in databases.')
        return

    if counter.lower() not in CHAMPIONS_LIST.lower():
        counter = ''

    role_message = ''
    if role != '':
        role_message = f' {role}'

    counter_message = ''
    if counter != '':
        counter_message = f' vs. {counter}'

    await ctx.send(f'Looking for a build for {champion}{role_message}{counter_message}...')

    build = get_build(champion, role, counter)
    full_build_message = f"""You could build the following items as {champion}{role_message}{counter_message}:
    
        🗿. Summoner Spells: {build['summoners'][0]} and {build['summoners'][1]}.
        🗿. Boots: {build['boots']}.
        🗿. Mythic item: {build['mythic'][0]}.
        🗿. Legendary items: {build['items'][0]}, {build['items'][1]}, {build['items'][2]}, {build['items'][3]}.
        
        Hope that works! Good match.
    """

    await ctx.send(full_build_message)


bot.run(TOKEN)
# <<< END Bot as a Bot
