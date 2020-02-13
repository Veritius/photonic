import discord, asyncio, random, math, string, os, sys
from discord.ext import commands
import assets, config

bot = commands.Bot(command_prefix='/')

class data():
    xyz = "xyz"

class information():
    inviteurl = "https://discordapp.com/oauth2/authorize?client_id=593269743826239491&scope=bot&permissions=8"
    token = config.token
    devtoken = config.devtoken

class utility(commands.Cog):
    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong!")

    @bot.command()
    async def invite(ctx):
        embedMessage = discord.Embed(title="**Invite Photonic**", url=information.inviteurl, color=assets.colour("gold"))
        await ctx.send(embed=embedMessage)

    @bot.command()
    async def topic(ctx, topicType=""):
        colourtouse = assets.colour("blue")
        if topicType in assets.topicTypes:
            choice = random.choice(assets.topicTypes[topicType])
        else:
            choice = "I couldn't find that topic"
            colourtouse = assets.colour("red")
        embedMessage = discord.Embed(title=choice, color=colourtouse)
        await ctx.send(embed=embedMessage)

    @bot.command()
    async def whois(ctx, member: discord.Member):
        useInline = False
        embedMessage = discord.Embed(title=f"Who is `{member.display_name}`?", color=assets.colour("green"))
        embedMessage.add_field(name="ID", value=member.id, inline=useInline)
        embedMessage.add_field(name="Username", value=member.name, inline=useInline)
        embedMessage.add_field(name="Discrim", value=member.discriminator, inline=useInline)
        embedMessage.add_field(name="Is Bot", value=member.bot, inline=useInline)
        embedMessage.add_field(name="Server Join Date", value=member.joined_at, inline=useInline)
        embedMessage.add_field(name="Nickname", value=member.nick, inline=useInline)
        embedMessage.add_field(name="Status", value=member.status, inline=useInline)
        embedMessage.add_field(name="Account Creation Date", value=member.created_at, inline=useInline)
        await ctx.send(embed=embedMessage)



bot.run(information.token)
#information.token = "How about no"
#information.devtoken = "How about no"
