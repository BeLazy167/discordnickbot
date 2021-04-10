import discord
from discord.ext import commands
import n_return as nk

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('READY')

@client.command(pass_context=True , )
async def chnick(ctx, member: discord.Member):
   name = nk.nicke()
   await member.edit(nick = name)

   await ctx.send(f'Nickname was changed for {member.mention} ')




client.run('DISCORD_BOT_TOKEN_HERE')

