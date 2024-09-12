import discord
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    if msg.content == "opa":
        await msg.channel.send("salve, " + username + "!")
        
@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    
    if emoji == "🙄" and message_id == 1283807706855247913:
        role = discord.utils.get(guild.roles, name = "competitive player")
        await member.add_roles(role)
        
    if emoji == "💀" and message_id == 1283807719996002345:
        role = discord.utils.get(guild.roles, name = "enjoys life player")
        await member.add_roles(role)
            
@bot.event
async def on_raw_reaction_remove(payload):
    user_id = payload.user_id
    emoji = payload.emoji.name
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(user_id)
    
    if emoji == "🙄" and message_id == 1283793254047023195:
        role = discord.utils.get(guild.roles, name = "competitive player")
        await member.remove_roles(role)
        
    if emoji == "💀" and message_id == 1283795485072691331:
        role = discord.utils.get(guild.roles, name = "enjoys life player")
        await member.remove_roles(role)
        
    

bot.run(DISCORD_TOKEN)
