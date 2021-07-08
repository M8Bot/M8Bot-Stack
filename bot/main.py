import os

from discord import Client, Member

client = Client()


@client.event
async def on_member_leave(member: Member):
    await member.send("Your message")


if __name__ == '__main__':
    client.run(os.getenv('DISCORD_TOKEN', "ODYyMzI3NDI0MzMwMjM1OTc0.YOWu_w.Mnei3N_aoEaxt97uUFducG7xVW4"))
