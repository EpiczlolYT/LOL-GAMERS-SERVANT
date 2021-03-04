import random
import praw 

reddit = praw.Reddit(client_id = "_oSU2eKnmJbGYw",
	                  client_secret = "OdjV6UM2VG1jYSiUt3pVexRAAyZHDA",
	                  username = "EpiczlolYt",
	                  password = "Edwin2007$",
	                  user_agent = "pythonpraw")
import discord
from discord.ext import commands 
client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command('meme')
async def meme(ctx):
	subreddit = reddit.subreddit("memes")
	all_subs = []

	top = subreddit.top(limit = 50)
	
	for submission in top:
		all_subs.append(submission)

	random_sub = random.choice(all_subs)

	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(title = name)

	em.set_image(url = url)

	await ctx.send(embed= em)


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
	try:
		await member.send("You have been kicked from LOL GAMERS, Because:"+reason)
	except:
		await member.send("The member has their dms closed")
	await member.kick(reason=reason)
      	
@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send(member.name + " has been banned from LOL GAMERS, Because:"+reason)
	await member.ban(reason=reason)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')


	for banned_entry in banned_users:
		user = banned_entry.user

		if(user.name, user.discriminator)==(member_name, member_disc):
			await ctx.guild.unban(user)
			await ctx.send(member_name +" has been unbanned")
			return

	await ctx.send(member+" was not found")

@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member : discord.Member):
	embed = discord.Embed(title =member.name , description = member.mention , color = discord.Colour.red())
	embed.add_field(name = "ID", value = member.id , inline = True)
	embed.set_thumbnail(url = member.avatar_url)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Request by {ctx.author.name}")
	await ctx.send(embed=embed)


client.run("ODAxMDg5MDg2MzMyMDc2MDUz.YAbmWQ.lLDmP0AXY6IvzVAqjWvDMAcH1YE")
