import discord
from random import choice

client = discord.Client()

ben_answers = [ "Yes." , "No." , "Hohoho" , "Eugh..." ]

@client.event
async def on_ready():
    print('Ben is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ben') or message.content.startswith('Ben'):
        await message.channel.send(choice(ben_answers))

client.run('BOT_TOKEN')
