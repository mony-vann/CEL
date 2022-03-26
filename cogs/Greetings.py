import discord
from discord.ext import commands

COMMANDS = ["```", "1. !cel crRoles with 'roles name' to create roles",
            "2. !cel dlRoles with 'roles name' to delete roles",
            "3. !cel ctrChannel with 'channel_name' @role to create a text channel for specific role",
            "4. !cel ctChannel with 'channel_name' to create text channel",
            "5. !cel dtChannel with 'channe_name' to delete text channel",
            "6. !cel giveRole with 'role_name' @users to assign role for users",
            "7. !cel disRole with @role @users to dismiss role from users",
            "8. !cel vetoBO1 @user1 'team name for user 1' @user2 'team name for user 2' to veto best of one",
            "9. !cel vetoBO2 @user1 'team name for user 1' @user2 'team name for user 2' to veto best of two",
            "10. !cel vetoBO3 @user1 'team name for user 1' @user2 'team name for user 2' to veto best of three",
            "11. !cel vetoBO5 @user1 'team name for user 1' @user2 'team name for user 2' to veto best of five"
            ,"```"
        ]

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cmd(self, ctx):
        cmd_list = ""
        for i in COMMANDS:
            cmd_list += i + "\n"
            
        await ctx.send(cmd_list)

    @commands.command()
    async def desc(self, ctx):
        await ctx.send("```A bot created mainly for CEL discord for veto process. It's still young as of right now it's a version 1.0.1 and will continue to grow overtime :D. Develpoed by Zen様#7756 ```")

def setup(client):
    client.add_cog(Greetings(client))
