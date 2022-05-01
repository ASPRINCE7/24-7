import discord
import random


TOKEN='OTY5OTk3NjY2Mzc1MzI3NzU0.Ym1iuQ.gge8tIummfbXIuUaXbyxjusmxGE'

client = discord.Client()
@client.event
async def on_ready():
    print("We have logged you in as {0.user}".format(client))


@client.event
async def on_message(message):
    username=str(message.author).split('#')[0]
    user_message=str(message.content)
    channel=str(message.channel.name)
    print(f'{username}:{user_message}({channel})')

    if message.author==client.user:
        return
    if message.channel.name=="general":
        if user_message.lower()=="hello":
            await message.channel.send(f'Hello {username}')
            return
        if user_message.lower()=="bye":
            await message.channel.send(f'See You Later {username} !!! ')
            return
    if user_message.lower()=="hi":
        await message.channel.send(f"HEY THERE {username} !!!")
        return
    if message.content.startswith("pd"):
        await message.channel.send(f"{username} your drop !!!")
        return




client.run(TOKEN)