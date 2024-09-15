import random
import discord
from discord import Intents
from discord.ext import commands

from config import DISCORD_TOKEN

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents=intents, help_command= None)

#Comando Help
@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title="Help", description="Aqui estão todas as funcionalidades do bot!", color=int("000080", 16))
    MyEmbed.set_thumbnail(url= "https://i.pinimg.com/736x/d0/7f/41/d07f41a90de591a898566fd0fd618115.jpg")
    
    # Linha vazio para espaçamento
    MyEmbed.add_field(name = "\u200b", value = "\u200b", inline = False)

    MyEmbed.add_field(name = "$help", value = 'Meio obvio, né?', inline = False)
    MyEmbed.add_field(name = "$ping", value = 'Comando para test de conexão do bot, bot responde com um "Pong!"', inline = False)
    MyEmbed.add_field(name = "$moeda", value = 'Em duvida dq fazer? Vamos "decidir as coisas no cara ou coroa"', inline = False)
    MyEmbed.add_field(name = "Em breve", value = 'Em breve, mais comandos para vocês!', inline = False)
    
    await ctx.send(embed=MyEmbed)
    
    
#Comando Ping Pong    
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
    
#Comando Cara ou Coroa    
@bot.command()
async def moeda(ctx):
    num = random.randint(1,2)
    
    if num == 1:
        await ctx.send("cara")
    
    if num == 2:
        await ctx.send("coroa")
        
        


    
bot.run(DISCORD_TOKEN)