import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Rosie has logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello') and message.channel.name == 'bot':
        await message.channel.send('Hello!')

client.run(os.environ['BOTKEY'])
