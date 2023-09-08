import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from scraper import get_build
import constants

# Get token from environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# This represents the connection to discord
# Handle events, states and interacts with Discord API's
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# >>> START Bot as a Bot
bot = commands.Bot(command_prefix='!builder', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='-hi')
async def say_hi(ctx):
    await ctx.send(f'Saludos {ctx.message.author}!')


@bot.command(name='-help')
async def say_help(ctx):
    help_message = """I was made to help you with the builds you may need without going to the browser and pícking some pages.
    
    Builds are obtained from https://probuildstats.com/ .
    
    To use the bot you can use the following commands:
    
        🫵 !builder-hi to say hi to the bot, be nice!
        🫵 !builder-help to display help information like this.
        🫵 !builder-build <champion-name> to look for a build for an specific champion.
        🫵 !builder-build <champion-name> <role> if you want a build for a specific role.
        🫵 !builder-build <champion-name> <role> <enemy-champíon> to look for a build against a specific champion.
    
    Translation to spanish is on work! Thanks for using me!"""

    await ctx.send(help_message)


@bot.command(name='-build')
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

    if champion.lower() not in constants.CHAMPIONS_LIST.lower():
        await ctx.send(f'Champion not found in databases.')
        return

    if counter.lower() not in constants.CHAMPIONS_LIST.lower():
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
        
    Hope that works! Good match."""

    await ctx.send(full_build_message)


bot.run(TOKEN)
# <<< END Bot as a Bot
