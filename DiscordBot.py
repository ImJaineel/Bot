from email import message
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!ping'):
        await message.channel.send('Pong!')
    
    if message.content.startswith('!bye'):
        await message.channel.send('Bye!')
    
    if message.content.startswith('!help'):
        await message.channel.send("""Available Commands :-
        !hello - To start the bot
        !ping - To end the bot
        !bye - To end the bot""")
    
client.run(os.getenv('DISCORD_BOT_TOKEN'))