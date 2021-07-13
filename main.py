import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event 
async def on_message(message):
  if message.content == 'Hi': #auto response for 'Hi'
    await message.channel.send('Hi!')
  await bot.process_commands(message)

@bot.event
async def on_ready():
  print('Bot is active!')
  await bot.change_presence(activity=discord.Game(name="Hi!")) #bot's activity status
  
@bot.command()
async def ping(ctx):
    embed = discord.Embed()
    embed.title = 'Ping:'
    embed.description = f"{round(bot.latency * 1000)}ms" 
    embed.color = ctx.author.color
    await ctx.send(embed=embed) #sends the active ping
    
bot.run('ODYyNzY2NDI2MDI4NzY5MzAw.YOdH2Q.UhUP03gE-s4du4lpaxccP2D_bNg')
