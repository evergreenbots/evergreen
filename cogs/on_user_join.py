import discord
from datetime import datetime
from discord import Message, TextChannel, Member
from discord.ext import commands


class OnMemberJoin(commands.Cog, name='On Member Join Listeners and Events'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = discord.Embed(colour=0x74ff90, title="InfinityCraft 2.∞ Discord Help", description = "[] = required argument\n<> = optional argument\nThe `|` means you can use either word for the command.\nFor example to submit a ticket you can use `m.ticket` **or** `m.report`,\nwhich is shown below using `|`.")
        embed.add_field(name = "**Ticket Help**",
        value = "`m.ticket|report new [content]` - Create a new ticket or report.\n**Please submit tickets and reports in a direct message to Marvin.**")
        embed.add_field(name = "**Server Info Help**",
                        value = "`m.server status` - Displays whether the server is online with player count.\n`m.server ip` - Displays the server IP.")
        embed.add_field(name = "Other Help",
                        value = "`m.mojang` - Check the status of Mojang & Minecraft services.")
        embed.timestamp=datetime.utcnow()
        embed.set_footer(
            text = "Marvin", icon_url = f'{self.client.user.avatar_url}')
        await member.send(embed = embed)



def setup(client):
    client.add_cog(OnMemberJoin(client))
    print('@EVENT: OnMemberJoin Event loaded \n---------------------')