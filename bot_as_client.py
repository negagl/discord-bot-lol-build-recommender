import os
import discord
from dotenv import load_dotenv

# Get token from environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHAMPIONS_LIST = os.getenv('CHAMPIONS_LIST')

# This represents the connection to discord
# Handle events, states and interacts with Discord API's
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# >>> START Bot as Client
client = discord.Client(intents=intents)


# EVENT:: Ready
@client.event
async def on_ready():
    """The client has established a connection to Discord"""
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        print(f'Bot is available in {guild.name} server')

        members = guild.members
        print(f'Users of {guild.name}:')

        for member in members:
            print(f' - {member.name}')


# EVENT:: Member Joined
@client.event
async def on_member_join(member):
    print(f'{member.name} Joined the channel')
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, caremondá')


# EVENT:: Member Left
@client.event
async def on_member_remove(member):
    print(f'{member.name} has left the channel')
    await member.create_dm()
    await member.dm_channel.send(f'Chao hijueputa.')


# EVENT:: Message typed
@client.event
async def on_message(message):
    if message.content.lower() == '!builder':
        await message.channel.send("Hey, que pasa valemía")


client.run(TOKEN)
# <<< END Bot as a Client
