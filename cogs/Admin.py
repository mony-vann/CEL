from dis import disco
from http import client
from random import randint, random
from unicodedata import category
import discord
from click import pass_context
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord import Guild

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # GIVE ROLE TO USERS
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def giveRole(self, ctx, role, users: commands.Greedy[discord.Member]):
        guild = ctx.guild
        perms = discord.Permissions(view_channel=True)
        
        if not get(guild.roles, name=role):
            await guild.create_role(name = role,  permissions = perms, reason = 'reason')
            await ctx.send(f"```You have created role for {role}```")
        
        _role = get(guild.roles, name=role)

        for user in users:
            if _role in user.roles:
                await ctx.send(f"```{user} already has the role: {role}```")
            else:
                await user.add_roles(_role)
                await ctx.send(f"```{user} successfuly added role: {role}```")

    @giveRole.error
    async def giveRole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

    # DISMISS ROLE FROM USERS
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def disRole(self, ctx, role : discord.Role, users: commands.Greedy[discord.Member]):
        for user in users:
            if role in user.roles:
                await user.remove_roles(role)
                await ctx.send(f"```{user} successfuly removed role: {role}```")
            else:
                await ctx.send(f"```{user} does not have the role: {role}```")

    @disRole.error
    async def disRole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

    # FLIP COIN
    @commands.command(pass_context = True)
    async def flipCoin(self, ctx):
        result = flipCoin()
        
        await ctx.send(f"```The result of the coin flip: {result}```")

    # CREATE ROLES
    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members = True)
    async def crRoles(self, ctx, *, names):
        guild = ctx.guild
        perms = discord.Permissions(view_channel=True)

        rnames = str(names).split()
        for name in rnames:
            if not get(guild.roles, name=name):
                await guild.create_role(name = name,  permissions = perms, reason = 'reason')
                await ctx.send(f"```You have created role for {name}```")
            else:
                await ctx.send(f"```Role {name} is already created```")
    
    @crRoles.error
    async def crRoles_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

    # DELETE ROLES
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def dlRoles(self, ctx, *, roles):
        guild = ctx.guild
        _roles = str(roles).split()

        for role in _roles:
            if get(guild.roles, name=role):
                _role = get(guild.roles, name=role)
                await discord.Role.delete(_role)
                await ctx.send(f"```{str(role)} has been deleted!```")
            else:
                await ctx.send(f"```Role {str(role)} does not exist!```")
    
    @dlRoles.error
    async def dlRoles_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

    # CREATE TEXT CHANNEL FOR SPECIFIC ROLE
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True, manage_channels = True)
    async def ctrChannel(self, ctx, ch_name, role : discord.Role, role1 : discord.Role):
        await ctx.send(f"```Enter a category ID: ```")
        cate_id = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author == ctx.author)

        if cate_id:
            guild = ctx.guild
            exist = False
            admin_role = get(guild.roles, name="admin")
            bot_role = get(guild.roles, name="CEL BOT")
            category = discord.utils.get(ctx.guild.categories, id=int(cate_id.content))
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                role: discord.PermissionOverwrite(read_messages=True),
                role1: discord.PermissionOverwrite(read_messages=True),
                admin_role: discord.PermissionOverwrite(read_messages=True),
                bot_role: discord.PermissionOverwrite(read_messages=True)
            }
            
            if get(category.channels, name=ch_name) in category.channels:
                await ctx.send(f"```Text channel called {ch_name} is already existed!```")
            else:
                await guild.create_text_channel(name = ch_name, overwrites=overwrites, category=category)
                await ctx.send(f"```You have created a text channel called {ch_name} assigned to {role} and {role1} under category of {category}```")

    @ctrChannel.error
    async def ctrChannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

    # CREATE TEXT CHANNEL
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True, manage_channels = True)
    async def ctChannel(self, ctx, *, ch_names):
        await ctx.send(f"```Enter a category ID: ```")
        cate_id = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author == ctx.author)

        if cate_id:
            guild = ctx.guild
            admin_role = get(guild.roles, name="admin")
            bot_role = get(guild.roles, name="CEL BOT")
            category = get(ctx.guild.categories, id=int(cate_id.content))

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=True),
                admin_role: discord.PermissionOverwrite(read_messages=True),
                bot_role: discord.PermissionOverwrite(read_messages=True)
            }
            _channels = ch_names.split()
            
            for channel in _channels:
                if get(category.channels, name=channel) in category.channels:
                    await ctx.send(f"```Text channel called {channel} is already existed!```")
                else:
                    await guild.create_text_channel(name = channel, overwrites=overwrites, category=category)
                    await ctx.send(f"```You have created a text channel called {channel} under category of {category}```")
                    
                
    @ctChannel.error
    async def ctChannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

    # DELETE TEXT CHANNEL
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_channels = True)
    async def dtChannel(self, ctx, *, ch_names):
        guild = ctx.guild
        _channels = ch_names.split()
        
        for channel in _channels:
            existing_channel = get(guild.text_channels, name=channel)

            if existing_channel is not None:
                await existing_channel.delete()
                await ctx.send(f"```Text channel called {existing_channel} is deleted!```")
            else:
                await ctx.send(f"```Text channel called {channel} is not exist!```")

    @dtChannel.error
    async def dtChannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

    # CREATE VOICE CHANNEL
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True, manage_channels = True)
    async def cvChannel(self, ctx, *, ch_names):
        await ctx.send(f"```Enter a category ID: ```")
        cate_id = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author == ctx.author)

        if cate_id:
            guild = ctx.guild
            admin_role = get(guild.roles, name="admin")
            bot_role = get(guild.roles, name="CEL BOT")
            category = get(guild.categories, id=int(cate_id.content))

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=True),
                admin_role: discord.PermissionOverwrite(read_messages=True),
                bot_role: discord.PermissionOverwrite(read_messages=True)
            }
            _channels = ch_names.split()
            
            for channel in _channels:
                if get(category.channels, name=channel) in category.channels:
                    await ctx.send(f"```Text channel called {channel} is already existed!```")
                else:
                    await category.create_voice_channel(name = channel, overwrites=overwrites)
                    await ctx.send(f"```You have created a voice channel called {channel} under category of {category}```")
    
    @cvChannel.error
    async def cvChannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")
        
    # CREATE VOICE CHANNEL FOR SPECIFIC ROLE
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True, manage_channels = True)
    async def cvrChannel(self, ctx, ch_name, role : discord.Role, role1 : discord.Role):
        await ctx.send(f"```Enter a category ID: ```")
        cate_id = await self.client.wait_for('message', check=lambda message: message.channel == ctx.channel and message.author == ctx.author)

        if cate_id:
            guild = ctx.guild
            exist = False
            admin_role = get(guild.roles, name="admin")
            bot_role = get(guild.roles, name="CEL BOT")
            category = discord.utils.get(ctx.guild.categories, id=int(cate_id.content))
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                role: discord.PermissionOverwrite(read_messages=True),
                role1: discord.PermissionOverwrite(read_messages=True),
                admin_role: discord.PermissionOverwrite(read_messages=True),
                bot_role: discord.PermissionOverwrite(read_messages=True)
            }

            if get(category.channels, name=ch_name) in category.channels:
                await ctx.send(f"```Text channel called {ch_name} is already existed!```")
            else:
                await guild.create_voice_channel(name = ch_name, overwrites=overwrites, category=category)
                await ctx.send(f"```You have created a voice channel called {ch_name} assigned to {role} and {role1} under category of {category}```")

    @cvrChannel.error
    async def cvrChannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")
    
    # DELETE VOICE CHANNEL
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_channels = True)
    async def dlvChannel(self, ctx, *, ch_names):
        guild = ctx.guild
        _channels = ch_names.split()
        
        for channel in _channels:
            existing_channel = get(guild.voice_channels, name=channel)

            if existing_channel is not None:
                await existing_channel.delete()
                await ctx.send(f"```Voice channel called {existing_channel} is deleted!```")
            else:
                await ctx.send(f"```Voice channel called {channel} is not exist!```")
    
    @dlvChannel.error
    async def dlvChannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You do not have the permission to use this command```")

def get_role(user : discord.Member):
        return user._roles

def isCaptain(user : discord.Member, role : discord.Role):
    if (str(role).lower() + "captain") in [y.name.lower() for y in user.roles]:
        return True
    else:
        return False

def flipCoin():
    if randint(0,10) > 5:
        result = "HEAD WON"
    else:
        result = "TAIL WON"
    
    return result

def setup(client):
    client.add_cog(Admin(client))
