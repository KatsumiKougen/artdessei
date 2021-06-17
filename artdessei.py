import os,discord,time,ultrastring as us,random as r,pekofy as pkf
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")
GUILD=os.getenv("DISCORD_GUILD")

# --- BOT INITIALISATION SECTION ---

bot=commands.Bot(command_prefix="`")

@bot.event
async def on_ready():
	print(f"Today is {time.asctime()}. Artdessei has logged in.")

# --- END OF BOT INITIALISATION SECTION ---

# --- BOT COMMANDS SECTION ---

@bot.command(name="date")
async def getdate(ctx):
	day={
		"Sun":"Sunday",
		"Mon":"Monday",
		"Tue":"Tuesday",
		"Wed":"Wednesday",
		"Thu":"Thursday",
		"Fri":"Friday",
		"Sat":"Saturday"
	}
	timeunit=time.asctime().split(" ")
	while "" in timeunit:
		timeunit.remove("")
	timeformat=f"{day[timeunit[0]]}, {timeunit[2]}. {timeunit[1]} {timeunit[4]}"
	await ctx.send(f"Today is:\n```{timeformat}```\n***Stay fresh!***")

@bot.command(name="list")
async def getlist(ctx):
	with open("list.md","r") as f:liststring=f.read()
	e=discord.Embed(
		title="List of commands",
		description=liststring,
		color=r.randrange(0x1000000)
	)
	await ctx.send(embed=e)

@bot.command(name="credit")
async def botcredit(ctx):
	with open("credit.md","r") as f:credit=f.read()
	e=discord.Embed(
		title="Credits",
		description=credit,
		color=r.randrange(0x1000000)
	)
	await ctx.send(embed=e)

@bot.command(name="pekofy")
async def pekofy(ctx,string:str):
	await ctx.send(pkf.pekofy(string))

@pekofy.error
async def pekofy_error(ctx,error):
	if isinstance(error,commands.ExpectedClosingQuoteError):
		e=discord.Embed(
			title=r.choice((
				"This ain't game-peko, boy.",
				"You do not do that, you know-peko?",
				"You really have problems-peko.",
				"Nope-peko. Not in a million years-peko.",
				"Fun fact: your command syntax is broken-peko.",	
			)),
			description="**Expecting `closing quotes`-peko**.\nYou might wanna add a closing quote-**peko**. :rabbit:\n\n*- Artdessei Exception Detector*",
			color=0x070a24
		)
		await ctx.reply(embed=e)
	print("Command error: pekofy")

@bot.command(name="ultra")
async def ultra(ctx,string:str):
	await ctx.send(us.UltraFormat(string))

@ultra.error
async def ultra_error(ctx,error):
	e=discord.Embed(
		title=r.choice((
			"This ain't Ultra-game, boy.",
			"You do not Ultra-do that, you know?",
			"You really have Ultra-problems.",
			"Nope. Not in a million Ultra-years.",
			"Fun fact: your Ultra-command syntax is broken.",	
		)),
		description="**Expecting `Ultra-closing quotes`.**\nYou might wanna **Ultra**-add a **Ultra**-closing quote.\n\n*- Artdessei Exception Detector*",
		color=0x070a24
	)
	await ctx.reply(embed=e)
	print("Command error: ultra")

@bot.command(name="baltan")
async def baltan(ctx):
	with open("baltan.png","rb") as f:
		await ctx.send(file=discord.File(f))

@bot.command(name="shuwatch")
async def shuwatch(ctx):
	with open("shuwatch.md","r") as f:
		await ctx.send(f.read())

@bot.command(name="instance_domination")
async def instdom(ctx):
	with open(r.choice(("idjuuga.png","idonija.png","idsizumu.png","idmujina.png")),"rb") as f:
		await ctx.send(file=discord.File(f))

@bot.command(name="good_bot")
async def goodbot(ctx):
	await ctx.reply(f"Thank you {str(ctx.author.mention)}",mention_author=True)

@bot.command(name="afk")
async def toggle_afk(ctx):
	afk=discord.utils.get(ctx.guild.roles,name="AFK")
	if afk in ctx.author.roles():
		await ctx.send(f"Hey, would you look at that!\n{ctx.author.name} is back.",mention_author=True)
		await ctx.author.remove_roles(afk)
	else:
		await ctx.send(f"Don't worry!:sweat_smile:\n{ctx.author.name} is not banned (yet) or anything.\nHe/she is just taking a break! He/she'll be right back... hopefully.",mention_author=True)
		await ctx.author.add_roles(afk)

"""
@bot.command(name="thankyou")
async def talk(ctx):
	e=discord.Embed(
		description="**Thanks to the people at Python Discord for helping my creator :hugging:**",
		color=r.randrange(0x1000000)
	)
	await ctx.send(embed=e)
"""

@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		e=discord.Embed(
			title=r.choice((
				"What the f**k is that?",
				"Bullsh**!",
				"Excuse me, but is it a real command or you just made that up?",
				"Sorry, not a real command.",
				"I like your attitude, but this - not an actual command.",
				"Holy sh\*\*! What the f\*\*k, man?",
				"Woah woah... just stop and read this.",
				"Not gonna work~",
			)),
			description=f"**Invalid command**\nNice try out there.\n\n*- Artdessei Exception Detector*",
			color=0x070a24
		)
		await ctx.reply(embed=e)
	print(f"{ctx.author} has entered the {chr(34)}{ctx.command}{chr(34)} command, which is not a valid command...")

# --- END OF BOT COMMANDS SECTION ---

@bot.event
async def on_command_completion(ctx):
	print(f"{ctx.author} has entered the {chr(34)}{ctx.command}{chr(34)} command.")

bot.run(TOKEN)
# Thanks to my brothers and sisters at Python Discord for helping me build the bot _-(^U^)-"
