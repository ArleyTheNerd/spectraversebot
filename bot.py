import discord
import os
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('Looking for >announce'))
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

@client.command(pass_context=True)
@commands.has_role('Loudspeaker')
async def announce(ctx, *, message):
  embed=discord.Embed(title=f"Announcement!", description=message,color=0xFF5733)
  embed.set_footer(text="Bot made by Arley#5799")
  await ctx.send(embed=embed)


keep_alive()
client.run(os.getenv('TOKEN'))
