import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

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
    champion, role, map_type = '', '', 'summoners rift'

    match args_len:
        case 1:
            champion = args[0]
        case 2:
            champion, role = args[:2]
        case 3:
            champion, role, map_type = args[:3]
        case _:
            await ctx.send(f'There is no champion i can look a build for.')
            return

    if champion.lower() not in CHAMPIONS_LIST.lower():
        await ctx.send(f'Champion not found in databases.')
        return

    await ctx.send(f'Looking for a build for {champion} {role} in {map_type}...')


bot.run(TOKEN)
# <<< END Bot as a Bot
