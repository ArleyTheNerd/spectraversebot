import discord
import os
from keep_alive import keep_alive
from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand):

  def __init__(self):
    super().__init__()
 
async def send_bot_help(self, mapping):
  for cog in mapping:
    await self.get_destination().send(f'(cog.qualified_name): {[command.name for command in mapping[cog]]}')

async def send_cog_help(self, cog):
  await self.get_Destination().send(f'(cog.qualified_name): {[command.name for command in cog.get_commands()]}')

async def send_group_help(self, group):
  await self.get_Destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')


async def send_command_help(self, command):
   await self.get_destination().send(command.name)  

   
client = commands.Bot(command_prefix = '>', help_command=commands.MinimalHelpCommand())


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
client.run((token goes here))
