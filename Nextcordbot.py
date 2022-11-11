from nextcord import SlashOption, Interaction
from nextcord.ext import commands
import nextcord

#prefix for normal commands
client = commands.Bot(command_prefix='!')


#slash command base
@client.slash_command(description='say something')
async def say(ctx : Interaction, message : str):
    await ctx.response.send_message(message)


#normal command base
@client.command()
async def ping(ctx : Interaction):
    ctx.send('Pong!')



#put your bot token in here
token = ''
client.run(token)