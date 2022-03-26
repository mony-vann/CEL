import discord
from discord.ext import commands
from apikeys import *
import os

intents = discord.Intents.default()
intents.members - True

client = commands.Bot(command_prefix = '!cel ', Intents = intents)

@client.event
async def on_ready():
    print("WE HAVE LOGGED IN AS {0.user}".format(client))

initial_extention = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extention.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extention in initial_extention:
        client.load_extension(extention)

client.run(TOKEN)