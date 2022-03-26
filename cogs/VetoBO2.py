import discord
from discord.ext import commands
from discord.utils import get

from cogs.Admin import flipCoin

MAPS = ["FRACTURE", "BIND", "ASCENT", "SPLIT", "BREEZE", "HAVEN", "ICEBOX"]
_maps = ["fracture", "bind", "ascent", "split", "breeze", "haven", "icebox"]
SUM = []

class VetoBO2(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        name="vetoBO2",
        description="veto for BO2",
    )
    @commands.has_permissions(kick_members = True)
    async def vetoBO2(self, ctx, user : discord.Member, TEAM, user1 : discord.Member, TEAM1):
        guild = ctx.guild
        CHECK = False

        user_role = get(guild.roles, name=str(TEAM))
        user1_role = get(guild.roles, name=str(TEAM1))

        if user_role in user.roles:
            if user1_role in user1.roles:
                CHECK = True
            else:
                await ctx.send(f"```{user1.display_name} is not in TEAM {TEAM1} ```")
        else:
            await ctx.send(f"```{user.display_name} is not in TEAM {TEAM} ```")

        if CHECK:
            maps = ""
            ROUND1 = True
            ROUND2 = False
            ROUND3= False
            ROUND4= False
            ROUND5= False
            ROUND6= False
            ROUND7= False
            SUMMARY = False

            await ctx.send(f"```{user.display_name} from TEAM {str(TEAM).upper()} is HEAD. \n{user1.display_name} from {str(TEAM1).upper()} is TAIL. ```")

            for i in range(0,3):
                await ctx.send(f"```Flipping coin...```")

            result = flipCoin()
            
            if result == "HEAD WON":
                winner, wuser = TEAM, user
                loser, luser = TEAM1, user1
                SUM.append(f"{winner} WON THE COIN FLIP")
                await ctx.send(f'```Flipping coin result is HEAD thus TEAM {TEAM} has WON!```')
            else:
                winner, wuser = TEAM1, user1
                loser, luser = TEAM, user
                SUM.append(f"{loser} WON THE COIN FLIP")
                await ctx.send(f'```Flipping coin result is TAIL thus TEAM {TEAM1} has WON!```')

            for i in MAPS:
                maps += str(i) + '\n'

            while ROUND1:
                await ctx.send(f"```MAP BANNING PHASE\nAVAILABLE MAPS TO BAN: \n\n{maps}```")
                await ctx.send(f"```{winner}'s TURN TO BAN: ```")
                
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == wuser.id) #and ctx.author.id == winner.id message.author ==ctx.author

                if msg:
                    if str(msg.content).lower() in _maps:
                        maps = ""
                        _maps.remove(str(msg.content).lower())
                        MAPS.remove(str(msg.content).upper())
                        for i in MAPS:
                            maps += '\n' + str(i)
                            
                        await ctx.send(f"```TEAM {winner} BANNED {str(msg.content).upper()}```")
                        SUM.append(winner + " BANNED " + str(msg.content).upper())

                        ROUND2 = True
                        break
                    elif str(msg.content).lower() == "cancel":
                        await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                        break
                    else:
                        await ctx.send(f"```Map invalid!```")
                        continue

            while ROUND2:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{loser}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == luser.id)

                if msg:
                    if str(msg.content).lower() in _maps:
                        maps = ""
                        _maps.remove(str(msg.content).lower())
                        MAPS.remove(str(msg.content).upper())
                        for i in MAPS:
                            maps += '\n' + str(i)
                        await ctx.send(f"```TEAM {loser} BANNED {str(msg.content).upper()}```")
                        SUM.append(loser + " BANNED " + str(msg.content).upper())

                        ROUND3 = True
                        break
                    elif str(msg.content).lower() == "cancel":
                        await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                        break
                    else:
                        await ctx.send(f"```Map invalid!```")
                        continue

            while ROUND3:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{winner}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == wuser.id)

                if msg:
                    if str(msg.content).lower() in _maps:
                        maps = ""
                        _maps.remove(str(msg.content).lower())
                        MAPS.remove(str(msg.content).upper())
                        for i in MAPS:
                            maps += '\n' + str(i)
                        await ctx.send(f"```TEAM {winner} BANNED {str(msg.content).upper()}```")
                        SUM.append(winner + " BANNED " + str(msg.content).upper())

                        ROUND4 = True
                        break
                    elif str(msg.content).lower() == "cancel":
                        await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                        break
                    else:
                        await ctx.send(f"```Map invalid!```")
                        continue

            while ROUND4:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{loser}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == luser.id)

                if msg:
                    if str(msg.content).lower() in _maps:
                        maps = ""
                        _maps.remove(str(msg.content).lower())
                        MAPS.remove(str(msg.content).upper())
                        for i in MAPS:
                            maps += '\n' + str(i)
                        await ctx.send(f"```TEAM {loser} BANNED {str(msg.content).upper()}```")
                        SUM.append(loser + " BANNED " + str(msg.content).upper())

                        ROUND5 = True
                        break
                    elif str(msg.content).lower() == "cancel":
                        await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                        break
                    else:
                        await ctx.send(f"```Map invalid!```")
                        continue

            while ROUND5:
                await ctx.send(f"```AVAILABLE MAPS TO PICK:\n{maps}```")
                await ctx.send(f"```{winner}'s TURN TO PICK: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == wuser.id)

                if msg:
                    if str(msg.content).lower() in _maps:
                        maps = ""
                        _maps.remove(str(msg.content).lower())
                        MAPS.remove(str(msg.content).upper())
                        for i in MAPS:
                            maps += '\n' + str(i)
                        await ctx.send(f"```TEAM {winner} PICKED {str(msg.content).upper()}```")
                        SUM.append(winner + " PICKED " + str(msg.content).upper())

                        await ctx.send(f"```{loser} WILL NOW PICK SIDE (DEFEND|ATTACK) : ```")
                        msg1 = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == luser.id)

                        if msg1:
                            if str(msg1.content).lower() == "defend":
                                await ctx.send(f"```TEAM {loser} CHOSE DEFEND THUS TEAM {winner} WILL ATTACK!```")
                                SUM.append(loser + " CHOSE DEFEND ON " + str(msg.content).upper())
                            elif str(msg1.content).lower() == "attack":
                                await ctx.send(f"```TEAM {loser} CHOSE ATTACK THUS TEAM {winner} WILL DEFEND!```")
                                SUM.append(loser + " CHOSE ATTACK ON " + str(msg.content).upper())
                            else:
                                _maps.append(str(msg.content).lower())
                                MAPS.append(str(msg.content).upper())
                                maps += '\n' + str(msg.content).upper()
                                await ctx.send(f"```Side invalid!```")
                                continue

                        ROUND6 = True
                        break
                    elif str(msg.content).lower() == "cancel":
                        await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                        break
                    else:
                        await ctx.send(f"```Map invalid!```")
                        continue
            
            while ROUND6:
                await ctx.send(f"```AVAILABLE MAPS TO PICK:\n{maps}```")
                await ctx.send(f"```{loser}'s TURN TO PICK: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == luser.id)

                if msg:
                    if str(msg.content).lower() in _maps:
                        maps = ""
                        _maps.remove(str(msg.content).lower())
                        MAPS.remove(str(msg.content).upper())
                        for i in MAPS:
                            maps += '\n' + str(i)
                        await ctx.send(f"```TEAM {loser} PICKED {str(msg.content).upper()}```")
                        SUM.append(loser + " PICKED " + str(msg.content).upper())

                        await ctx.send(f"```{winner} WILL NOW PICK SIDE (DEFEND|ATTACK) : ```")
                        msg1 = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author.id == wuser.id)

                        if msg1:
                            if str(msg1.content).lower() == "defend":
                                await ctx.send(f"```TEAM {winner} CHOSE DEFEND THUS TEAM {loser} WILL ATTACK!```")
                                SUMMARY = True
                                SUM.append(winner + " CHOSE DEFEND ON " + str(msg.content).upper())
                            elif str(msg1.content).lower() == "attack":
                                await ctx.send(f"```TEAM {winner} CHOSE ATTACK THUS TEAM {loser} WILL DEFEND!```")
                                SUMMARY = True
                                SUM.append(loser + " CHOSE ATTACK ON " + str(msg.content).upper())
                            else:
                                _maps.append(str(msg.content).lower())
                                MAPS.append(str(msg.content).upper())
                                maps += '\n' + str(msg.content).upper()
                                await ctx.send(f"```Side invalid!```")
                                continue

                        ROUND7 = True
                        break
                    elif str(msg.content).lower() == "cancel":
                        await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                        break
                    else:
                        await ctx.send(f"```Map invalid!```")
                        continue

            while ROUND7:
                await ctx.send(f"```THE LAST REMAINING MAP IS: {maps}```")
                await ctx.send(f"```{maps} WILL BE DISCARDED```")
                SUM.append(MAPS[0] + " HAS BEEN DISCARDED" )
                break

            while SUMMARY:
                temp = ""
                await ctx.send(f"```SUMMARY OF VETO\n```")
                for i in SUM:
                    temp += str(i) + '\n'

                await ctx.send(f"```{temp}```")
                break
    
    @vetoBO2.error
    async def vetoBO2_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")
def setup(client):
    client.add_cog(VetoBO2(client))