from discord.ext.commands import Bot
import random
import asyncio
import discord

Token = "NDY0NDE2NTI5OTEyNTYxNjc0.Dh-pUg.IhpGaCBnO5BSsQMgb5aSgFVPNrU"
Bot_Prefix = "f!"
client = Bot(command_prefix=Bot_Prefix)
client.remove_command('help')

##printing to the terminal when the bot is ready
@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="a!help to get started"))
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

##When a user joins, assign a role and welcome.
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.server.roles, name="Friends")
	channel = member.server.get_channel("463180233105735681")
	nostalgia = member.server.get_member_named("nostalgia#4307")
	Rules = member.server.get_channel("450514514237194261")
	Assign = member.server.get_channel("453019261137322005")
	memberID = "Welcome to Let's Be Friends {0} , otherwise known as LBF! We advise that you read {2} and go to {3} to assign roles. If you have any further questions, contact {1} i.e. DMs and/or server mention. Thanks for joining!".format(member.mention, nostalgia.mention, Rules.mention, Assign.mention)
	await client.add_roles(member, role)
	await client.send_message(channel, memberID)

##When a users leaves, goodbye
@client.event
async def on_member_remove(member):
	channel = member.server.get_channel("463180233105735681")
	await client.send_message(channel, "{0} has decided to leave.".format(member.mention))
	
##Help Command
@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	thumbnail = "https://i.imgur.com/iLyjQfK.jpg"
	
	embed = discord.Embed (
	colour = discord.Colour.red(),
	description="All Commands And Info For Them."
	)
	
	embed.set_author(name="Help")
	embed.add_field(name="f!help", value="Shows this", inline=False)
	embed.add_field(name="f!eightball", value="Tells the future", inline=False)
	embed.set_thumbnail(url=thumbnail)
	await client.send_message(ctx.message.channel, embed=embed)


##Eightball command
@client.command()
async def eightball():
	responces = [
	'It is quite possible.', 'Yes, it is certain.', 'That\'s a straight no.', 
	'In the near future', 'Possibly', 'Try again, i can\'t tell'
	]
	
	await client.say(random.choice(responces))
	
##Clear x amount of messages 	
@client.command(pass_context = True)
async def clear(ctx, number):
	if ctx.message.author.server_permissions.administrator:
		mgs = [] #Empty list to put all the messages in the log
		number = int(number) #Converting the amount of messages to delete to an integer
		async for x in client.logs_from(ctx.message.channel, limit = number):
			mgs.append(x)
		await client.delete_messages(mgs)

	
client.run(Token)

	