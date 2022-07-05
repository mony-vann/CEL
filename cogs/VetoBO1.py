import discord
from discord.ext import commands
from discord.utils import get
import asyncio

from cogs.Admin import flipCoin


class VetoBO1(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        name="vetoBO1",
        description="veto for BO1",
    )
    @commands.has_permissions(kick_members = True)
    async def vetoBO1(self, ctx, user : discord.Member, TEAM, user1 : discord.Member, TEAM1):
        MAPS = ["FRACTURE", "BIND", "ASCENT", "PEARL", "BREEZE", "HAVEN", "ICEBOX"]
        _maps = ["fracture", "bind", "ascent", "pearl", "breeze", "haven", "icebox"]
        SUM = []

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
            
            await ctx.send(f"```{user.display_name} from TEAM {str(TEAM).upper()} is HEAD. \n{user1.display_name} from TEAM {str(TEAM1).upper()} is TAIL. ```")

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
                SUM.append(f"{winner} WON THE COIN FLIP")
                await ctx.send(f'```Flipping coin result is TAIL thus TEAM {TEAM1} has WON!```')

            for i in MAPS:
                maps += str(i) + '\n'

            while ROUND1:
                await ctx.send(f"```MAP BANNING PHASE\nAVAILABLE MAPS TO BAN: \n\n{maps}\nTYPE IN ONLY THE NAME OF THE MAP```")
                await ctx.send(f"```{winner}'s TURN TO BAN: ```")

                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel) #and ctx.author.id == winner.id message.author ==ctx.author
                
                if msg:
                    if msg.author.id == wuser.id:
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
                        
                        else:
                            await ctx.send(f"```Map invalid!```")
                            continue

                    elif msg.author.id == luser.id:
                        await ctx.send(f"```WARNING! PLEASE WAIT FOR YOUR TURN!```")
                        
                    elif msg.author.id == ctx.author.id:
                        if str(msg.content).lower() == "cancel":
                            await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                            break
                    else:
                        await ctx.send(f"```WARNING! {msg.author.name}, YOU ARE NOT IN THIS VETO PROCESS!```")

            while ROUND2:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{loser}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel)

                if msg:
                    if msg.author.id == luser.id:
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

                        else:
                            await ctx.send(f"```Map invalid!```")
                            continue

                    elif msg.author.id == wuser.id:
                        await ctx.send(f"```WARNING! PLEASE WAIT FOR YOUR TURN!```")
                        
                    elif msg.author.id == ctx.author.id:
                        if str(msg.content).lower() == "cancel":
                            await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                            break
                    else:
                        await ctx.send(f"```WARNING! {msg.author.name}, YOU ARE NOT IN THIS VETO PROCESS!```")

            while ROUND3:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{winner}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel)

                if msg:
                    if msg.author.id == wuser.id:
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

                        else:
                            await ctx.send(f"```Map invalid!```")
                            continue

                    elif msg.author.id == luser.id:
                        await ctx.send(f"```WARNING! PLEASE WAIT FOR YOUR TURN!```")
                        
                    elif msg.author.id == ctx.author.id:
                        if str(msg.content).lower() == "cancel":
                            await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                            break
                    else:
                        await ctx.send(f"```WARNING! {msg.author.name}, YOU ARE NOT IN THIS VETO PROCESS!```")

            while ROUND4:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{loser}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel)

                if msg:
                    if msg.author.id == luser.id:
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
                        
                        else:
                            await ctx.send(f"```Map invalid!```")
                            continue
                    
                    elif msg.author.id == wuser.id:
                        await ctx.send(f"```WARNING! PLEASE WAIT FOR YOUR TURN!```")
                        
                    elif msg.author.id == ctx.author.id:
                        if str(msg.content).lower() == "cancel":
                            await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                            break
                    else:
                        await ctx.send(f"```WARNING! {msg.author.name}, YOU ARE NOT IN THIS VETO PROCESS!```")
                    

            while ROUND5:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{winner}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel)

                if msg:
                    if msg.author.id == wuser.id:
                        if str(msg.content).lower() in _maps:
                            maps = ""
                            _maps.remove(str(msg.content).lower())
                            MAPS.remove(str(msg.content).upper())
                            for i in MAPS:
                                maps += '\n' + str(i)
                            await ctx.send(f"```TEAM {winner} BANNED {str(msg.content).upper()}```")
                            SUM.append(winner + " BANNED " + str(msg.content).upper())

                            ROUND6 = True
                            break
                        else:
                            await ctx.send(f"```Map invalid!```")
                            continue

                    elif msg.author.id == luser.id:
                        await ctx.send(f"```WARNING! PLEASE WAIT FOR YOUR TURN!```")
                        
                    elif msg.author.id == ctx.author.id:
                        if str(msg.content).lower() == "cancel":
                            await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                            break
                    else:
                        await ctx.send(f"```WARNING! {msg.author.name}, YOU ARE NOT IN THIS VETO PROCESS!```")
            
            while ROUND6:
                await ctx.send(f"```AVAILABLE MAPS TO BAN:\n{maps}```")
                await ctx.send(f"```{loser}'s TURN TO BAN: ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel)

                if msg:
                    if msg.author.id == luser.id:
                        if str(msg.content).lower() in _maps:
                            maps = ""
                            _maps.remove(str(msg.content).lower())
                            MAPS.remove(str(msg.content).upper())
                            for i in MAPS:
                                maps += '\n' + str(i)
                            await ctx.send(f"```TEAM {loser} BANNED {str(msg.content).upper()}```")
                            SUM.append(loser + " BANNED " + str(msg.content).upper())

                            ROUND7 = True
                            break
                        
                        else:
                            await ctx.send(f"```Map invalid!```")
                            continue

                    elif msg.author.id == wuser.id:
                        await ctx.send(f"```WARNING! PLEASE WAIT FOR YOUR TURN!```")
                        
                    elif msg.author.id == ctx.author.id:
                        if str(msg.content).lower() == "cancel":
                            await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                            break
                    else:
                        await ctx.send(f"```WARNING! {msg.author.name}, YOU ARE NOT IN THIS VETO PROCESS!```")

            while ROUND7:
                await ctx.send(f"```THE LAST REMAINING MAP IS: {maps}```")
                await ctx.send(f"```{winner}'s WILL NOW PICK SIDE (DEFEND|ATTACK): ```")
                msg = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel)

                if msg:
                    if msg.author.id == wuser.id:
                        if str(msg.content).lower() == "defend" or str(msg.content).lower() == "def":
                            await ctx.send(f"```TEAM {winner} CHOSE DEFEND THUS TEAM {loser} WILL ATTACK!```")
                            SUMMARY = True
                            SUM.append("BOTH TEAM WILL PLAY ON " + MAPS[0])
                            SUM.append(winner + " CHOSE DEFEND ON " + MAPS[0])
                            break
                        elif str(msg.content).lower() == "attack" or str(msg.content).lower() == "att":
                            await ctx.send(f"```TEAM {winner} CHOSE ATTACK THUS TEAM {loser} WILL DEFEND!```")
                            SUMMARY = True
                            SUM.append("BOTH TEAM WILL PLAY ON " + MAPS[0])
                            SUM.append(winner + " CHOSE ATTACK ON " + MAPS[0])
                            break
                        else:
                            await ctx.send(f"```Side invalid!```")
                            continue

                    elif msg.author.id == luser.id:
                        await ctx.send(f"```WARNING! THIS IS NOT YOUR TURN!```")
                        
                    elif msg.author.id == ctx.author.id:
                        if str(msg.content).lower() == "cancel":
                            await ctx.send(f"```VETO PROCESS HAS BEEN CANCELED```")
                            break
                    else:
                        await ctx.send(f"```WARNING! {msg.author.name}, YOU ARE NOT IN THIS VETO PROCESS!```")
            
            while SUMMARY:
                temp = ""
                await ctx.send(f"```SUMMARY OF VETO\n```")
                for i in SUM:
                    temp += str(i) + '\n'

                await ctx.send(f"```{temp}```")
                break

    @vetoBO1.error
    async def vetoBO1_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

def setup(client):
    client.add_cog(VetoBO1(client))
