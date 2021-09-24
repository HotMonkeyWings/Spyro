import discord
import os
from datetime import datetime
import pytz
from decouple import config

IST = pytz.timezone('Asia/Kolkata')     #Change your timezone here
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.author.guild_permissions.administrator:
        return


    if message.content.startswith("-attend"):
        parts = message.content.split()
        parts.pop(0)
        parts = ''.join(parts)
        parts = parts.split(':')
        if len(parts) < 2:
            await message.channel.send("Correct format: -attend <ChannelName>:<Role>")
            return
        groupName = parts[0]
        role = parts[1]
        present = []
        channels = list(message.guild.channels)

        # Find participants in channel
        for _ in channels:
            if _.name == groupName:
                attend = _.members
                for mem in attend:
                    if role in [role_.name for role_ in mem.roles]:
                        present.append(mem.display_name)

        # Find all members
        members = []
        for mem in message.guild.members:
            if not mem.bot and role in [role_.name for role_ in mem.roles]:
                members.append(mem.display_name)

        # Present List Message Generation
        msg_present = []
        temp = ''
        for name in present:
            if len(temp+name)+40 >= 1024:
                msg_present.append(temp)
                temp = ''
            temp += name + "\n"
        msg_present.append(temp)

        # Check if no one is present
        if len(msg_present[0]) == 0:
            msg_present[0] = "-"

        # Absent List Message Generation
        msg_absent = []
        temp = ''
        for name in members:
            if name not in present:
                if len(temp+name)+40 >= 1024:
                    msg_absent.append(temp)
                    temp = ''
                temp += name + "\n"
        msg_absent.append(temp)

        # Check if no one is absent
        if len(msg_absent[0]) == 0:
            msg_absent[0] = "-"

        today = datetime.now(IST)
        d2 = today.strftime("%H:%M:%S on %B %d, %Y ")
        embed = discord.Embed(
            title="Attendance List",
            description="Attendance recorded at " + d2,
            color = discord.Color.blue()
        )
        await message.channel.send(embed=embed)
        await message.channel.send("**Present**\n")
        for i in range(len(msg_present)):
            await message.channel.send(msg_present[i])

        await message.channel.send("**Absent**\n")
        for i in range(len(msg_absent)):
            await message.channel.send(msg_absent[i])
        #embed.add_field(name="Present", value=msg_present, inline=False)
        #embed.add_field(name="Absent", value=msg_absent, inline=False)

try:
    API_KEY=config('KEY')
    client.run(API_KEY) #Insert key here
except:
    print("Create a .env file with KEY=<Your-API-KEY>")
