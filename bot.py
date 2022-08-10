import discord
import discord.utils
from discord.utils import get
from discord.ext import commands
from discord import Option
from discord.commands import slash_command
from discord.ext.commands import Bot
import os
import datetime
import configparser
import string
import random
from discord import Option
from pkg_resources import require

database = 'database.ini'
config = configparser.ConfigParser()
config.read(database)


prefix = config['discordbotstuff']['prefix']
adminpassword = config['discordbotstuff']['pass']
token = config['discordbotstuff']['token']
adminrole = int(config['serverrelevent']['adminrole'])
wts_wtb = int(config['serverrelevent']['wts_wtb'])
normalcatid = int(config['serverrelevent']['normalcat'])
premiumcatid = int(config['serverrelevent']['premiumcat'])
topcatid = int(config['serverrelevent']['topcat'])
memberrole = int(config['serverrelevent']['verifiedrole'])
guild = int(config['serverrelevent']['guildid'])
channel = config['serverrelevent']['welcomechannel']
version = '1.2.0'
MPNAME = config['discordbotstuff']['mpname']
date = datetime.datetime.utcnow().strftime('%d-%m-%y-%H:%M')




intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")
server = bot.get_guild(int(guild))



def dateswithdeleay(data):
    standart = datetime.datetime.now()
    top = datetime.datetime.now() + datetime.timedelta(hours=12)
    premium = datetime.datetime.now() + datetime.timedelta(days=1)
    normal = datetime.datetime.now() + datetime.timedelta(days=2)
    if data == 'date':
        return standart.strftime('%y%m%d%H%M%S')
    elif data == 'delaytop':
        return top.strftime('%y%m%d%H%M%S')
    elif data == 'delaypremium':
        return premium.strftime('%y%m%d%H%M%S')
    elif data == 'delaynormal':
        return normal.strftime('%y%m%d%H%M%S')

def expirydate(checkifgoodluck):
    vartempe = 1
    day = datetime.datetime.utcnow().strftime('%d')
    month = datetime.datetime.utcnow().strftime('%m')
    minutes = datetime.datetime.utcnow().strftime('%M')
    hour = datetime.datetime.utcnow().strftime('%H')
    year = datetime.datetime.utcnow().strftime('%Y')
    timea2dded = int(month) + int(vartempe)

    ne5wd2e5la2y = (f'{month}{day}')
    cleanasf = (f'{timea2dded}{day}')
    mycook = (f'{day}.{month}.{year}')
    if checkifgoodluck == 'yes':
        return cleanasf
    elif checkifgoodluck == 'cool':
        return mycook
    else:
        return ne5wd2e5la2y

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def code():
    chars = string.digits
    return ''.join(random.choice(chars) for i in range(4))

def generatelicence():
    licence = MPNAME + '-{}-{}-{}'.format(code(), code(), code())
    return licence


def checkifroles(ctx):
    role = discord.utils.get(ctx.guild.roles, id=adminrole)
    if role in ctx.author.roles:
        return True
    else:
        return False
@bot.event
async def on_member_join(member):
    await bot.get_channel(channel).send(f'Welcome {member.mention} to the {MPNAME}!')


@bot.event
async def on_ready():
    cls()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=MPNAME + ' on TOP')) # you can change this if you want
    print("Logged in as: " + bot.user.name + " - " + str(bot.user.id))
    print("Is in servers: " + str(len(bot.guilds)))
    print(f'Bot is ready. -  Version: {version}')
    print("Made by Mr.Grupr with love.")
    print("")


@bot.event
async def on_message(message):
    server = bot.get_guild(int(guild))
    member = server.get_member(message.author.id)
    for i in config['channel']:
        if message.channel.id == int(config['channel'][i]):
            if message.content.startswith(prefix):
                if message.mention_everyone:
                    await message.delete()
                    await message.channel.send('No one can mention everyone.', delete_after=5)
                else:
                    pass
            elif message.author == bot.user:
                return
            elif message.author.name == 'Dyno':
                return
            elif message.mention_everyone:
                await message.delete()
                await message.channel.send('No one can mention everyone.', delete_after=5)
            elif int(config[i]['expiry']) < int(expirydate('nyoo')):
                channel = server.get_channel(int(i))
                await message.delete()
                await channel.delete()
                await member.send('Your slot is expired. Please contact the owner.')

            else:
                embednorm = discord.Embed(description=f'** Contact: {member.mention} \n \n' + message.content + '**', color=discord.Color.blue())
                print(str(message.author.avatar.url))
                embednorm.set_footer(text="Sent by: " + message.author.name + message.author.discriminator, icon_url=str(message.author.avatar.url))
                embednorm.set_thumbnail(url=str(message.author.avatar.url))
                if message.attachments:
                    embednorm.set_image(url=message.attachments[0].url)
                    await message.channel.send(embed=embednorm)
                    await message.delete()
                else:
                    await message.channel.send(embed=embednorm)
                    await message.delete()



    if message.author == bot.user:
        return
    elif message.author.name == 'Dyno':
        return
    else:
        print("New message: " + message.content + " - " + message.author.name)


    if message.channel.id == wts_wtb:
        server = bot.get_guild(message.guild.id)
        member = server.get_member(message.author.id)
        if message.content.startswith(prefix):
            pass
        elif message.mention_everyone:
            await message.delete()
            await message.channel.send('No one can mention everyone.', delete_after=5)
        else:
            embedforwts = discord.Embed(description=f'** Contact: {member.mention} \n \n' + message.content + '**', color=discord.Color.blue())
            embedforwts.set_footer(text="Sent by: " + message.author.name + message.author.discriminator, icon_url=str(message.author.avatar.url))
            embedforwts.set_thumbnail(url=str(message.author.avatar.url))
            if message.attachments:
                embedforwts.set_image(url=message.attachments[0].url)
                await message.channel.send(embed=embedforwts)
                await message.delete()
            else:
                await message.channel.send(embed=embedforwts)
                await message.delete()

    await bot.process_commands(message)





@bot.command(pass_context = True)
async def clean(ctx, number: str = None):
    await ctx.message.delete()
    if number == None:
        await ctx.send("Please enter a number of messages to delete.", delete_after=5)
    if checkifroles(ctx) is True:
        await ctx.channel.purge(limit=int(number))
    else:
        await ctx.send("You don't have permission to use this command.", delete_after=5)

@bot.slash_command(guild_ids=[guild], name='ping', description='Pings the users.')
async def ping(ctx,
):
    await ctx.respond('Pinging...', ephemeral=True)
    for i in config['channel']:
        if ctx.channel.id == int(config['channel'][i]):
            if config[i]['pingdown'] == '/':
                await ctx.send('@everyone , pinged by ' + ctx.author.mention) 
                if config[i]['type'] == 'top':
                    config[i]['pingdown'] = str(dateswithdeleay('delaytop'))
                    with open(database, 'w') as configfile:
                        config.write(configfile)
                elif config[i]['type'] == 'normal':
                    config[i]['pingdown'] = str(dateswithdeleay('delaynormal'))
                    with open(database, 'w') as configfile:
                        config.write(configfile)
                elif config[i]['type'] == 'premium':
                    config[i]['pingdown'] = str(dateswithdeleay('delaypremium'))
                    with open(database, 'w') as configfile:
                        config.write(configfile)
                else:
                    print("Plan type invalid")

            elif int(dateswithdeleay('date')) > int(config[i]['pingdown']):
                await ctx.send('@everyone , pinged by ' + ctx.author.mention) 
                if config[i]['type'] == 'top':
                    config[i]['pingdown'] = str(dateswithdeleay('delaytop'))
                    with open(database, 'w') as configfile:
                        config.write(configfile)
                elif config[i]['type'] == 'normal':
                    config[i]['pingdown'] = str(dateswithdeleay('delaynormal'))
                    with open(database, 'w') as configfile:
                        config.write(configfile)
                elif config[i]['type'] == 'premium':
                    config[i]['pingdown'] = str(dateswithdeleay('delaypremium'))
                    with open(database, 'w') as configfile:
                        config.write(configfile)
                else:
                    print("Plan type invalid")
            elif int(dateswithdeleay('date')) < int(config[i]['pingdown']):
                await ctx.author.send('Your still on a cooldown to ping ' + ctx.author.mention)
        else:
            pass

@bot.slash_command(guild_ids=[guild], name='genkey', description='Generates a new key for the server.')
async def genkey(
    ctx, 
    keytype: Option(str, "Keytype", choices=["top", "premium", "normal"]),
    ):
    licence = generatelicence()
    await ctx.respond('Generating key...', ephemeral=True)
    if checkifroles(ctx) is True:
        if keytype == 'premium': 
            config['licences'][licence] = 'true'
            config[licence] = {'valid': 'true', 'type': 'premium'}
            await ctx.author.send(f'Licence for type: {keytype} \n Key generated: {licence}')
            with open(database, 'w') as configfile:
                config.write(configfile)
        elif keytype == 'normal':
            config['licences'][licence] = 'true'
            config[licence] = {'valid': 'true', 'type': 'normal'}
            await ctx.author.send(f'Licence for type: {keytype} \n Key generated: {licence}')
            with open(database, 'w') as configfile:
                config.write(configfile)
        elif keytype == 'top':
            config['licences'][licence] = 'true'
            config[licence] = {'valid': 'true', 'type': 'top'}
            await ctx.author.send(f'Licence for type: {keytype} \n Key generated: {licence}')
            with open(database, 'w') as configfile:
                config.write(configfile)
        else:
            await ctx.respond("Invalid keytype.", ephemeral=True)
    else:
        await ctx.respond("You don't have permission to use this command.", ephemeral=True)



@bot.slash_command(guild_ids=[guild], name='usekey', description='Uses a key.')
async def usekey(
    ctx, 
    key: Option(str, "Enter your key", required=True),
    ):
    server = bot.get_guild(int(guild))
    member = server.get_member(ctx.author.id)
    verifiedrole = discord.utils.get(ctx.guild.roles, id=memberrole)
    await ctx.respond('Checking key...', ephemeral=True)
    if key in config['licences']:
        if config[key]['valid'] == 'true':
            config['licences'][key] = 'false'
            with open(database, 'w') as configfile:
                config.write(configfile)

            if 'premium' == config[key]['type']:
                await ctx.respond("You have used a premium key.", ephemeral=True)
                config[key]['valid'] = 'used'
                with open(database, 'w') as configfile:
                    config.write(configfile)
                categorypremi = discord.utils.get(ctx.guild.categories, id=premiumcatid)
                channel = await ctx.guild.create_text_channel(ctx.author.name, category=categorypremi)
                await channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
                await channel.set_permissions(verifiedrole, send_messages=False, view_channel=True)
                await channel.set_permissions(ctx.author, send_messages=True, view_channel=True)
                await ctx.author.send(f'You have been given access to the premium channel {channel.mention}.')
                config[channel.id] = {'type': 'premium', 'key': key, 'userid': str(ctx.author.id), 'pingdown': '/', 'expiry': str(expirydate('yes'))}
                config['channel'][str(channel.id)] = str(channel.id)
                with open(database, 'w') as configfile:
                    config.write(configfile)
                embed5f4ornorm = discord.Embed(title="Premium Slot!", description=f'You have been given access to the TOP slot {member.mention}.', color=0x00ff00)
                embed5f4ornorm.add_field(name="Pings", value="Every 24 Hours.", inline=False)
                embed5f4ornorm.add_field(name="Channel expiry", value=str(expirydate('cool')), inline=False)
                await channel.send(embed=embed5f4ornorm)
                await ctx.author.send(f'You have been given access to the premium channel {channel.mention}.', embed=embed5f4ornorm)

            elif 'normal' == config[key]['type']:
                await ctx.respond("You have used a normal key.", ephemeral=True)
                config[key]['valid'] = 'used'
                with open(database, 'w') as configfile:
                    config.write(configfile)
                categorynor = discord.utils.get(ctx.guild.categories, id=normalcatid)
                channel = await ctx.guild.create_text_channel(ctx.author.name, category=categorynor)
                await channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
                await channel.set_permissions(verifiedrole, send_messages=False, view_channel=True)
                await channel.set_permissions(ctx.author, send_messages=True, view_channel=True)
                await channel.send(f'Welcome to the premium channel {ctx.author.mention}!')
                config[channel.id] = {'type': 'normal', 'key': key, 'userid': str(ctx.author.id), 'pingdown': '/', 'expiry': str(expirydate('yes'))}
                config['channel'][str(channel.id)] = str(channel.id)
                with open(database, 'w') as configfile:
                    config.write(configfile)
                config[channel.id] = {'type': 'normal', 'key': key, 'userid': str(ctx.author.id),'pingdown': '/', 'expiry': str(expirydate('yes'))}
                config['channel'][str(channel.id)] = str(channel.id)
                with open(database, 'w') as configfile:
                    config.write(configfile)
                embed2fornorm = discord.Embed(title="Normal Slot!", description=f'You have been given access to the normal slot {member.mention}.', color=0x00ff00)
                embed2fornorm.add_field(name="Pings", value="Every 48 Hours.", inline=False)
                embed2fornorm.add_field(name="Channel expiry", value=str(expirydate('cool')), inline=False)
                await channel.send(embed=embed2fornorm)
                await ctx.author.send(f'You have been given access to the normal channel {channel.mention}.', embed=embed2fornorm)

            elif 'top' == config[key]['type']:
                await ctx.respond("You have used a top key.", ephemeral=True)
                config[key]['valid'] = 'used'
                with open(database, 'w') as configfile:
                    config.write(configfile)
                categorytop = discord.utils.get(ctx.guild.categories, id=topcatid)
                channel = await ctx.guild.create_text_channel(ctx.author.name, category=categorytop)
                await channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
                await channel.set_permissions(verifiedrole, send_messages=False, view_channel=True)
                await channel.set_permissions(ctx.author, send_messages=True, view_channel=True)
                config[channel.id] = {'type': 'top', 'key': key, 'userid': str(ctx.author.id),'pingdown': '/', 'expiry': str(expirydate('yes'))}
                config['channel'][str(channel.id)] = str(channel.id)
                with open(database, 'w') as configfile:
                    config.write(configfile)
                embedf4ornorm = discord.Embed(title="TOP Slot!", description=f'You have been given access to the TOP slot {member.mention}.', color=0x00ff00)
                embedf4ornorm.add_field(name="Pings", value="Every 12 Hours.", inline=False)
                embedf4ornorm.add_field(name="Channel expiry", value=str(expirydate('cool')), inline=False)
                await channel.send(embed=embedf4ornorm)
                await ctx.author.send(f'You have been given access to the top channel {channel.mention}.', embed=embedf4ornorm)
            else:
                await ctx.respond("Invalid keytype.", ephemeral=True)
        else:
            await ctx.respond("This key has already been used.", ephemeral=True)
    else:
        await ctx.respond('Key not found.', ephemeral=True)

@bot.slash_command(guild_ids=[guild], name='nuke', description='Nukes your shops.')
async def nukes(
    ctx,
):
    if checkifroles(ctx) == True:
        await ctx.respond('Nuking...', ephemeral=True)
        await ctx.channel.purge()
        await ctx.respond('Nuked.', ephemeral=True)
    else:
        try:
            if str(ctx.channel.id) == config['channel'][str(ctx.channel.id)]:
                await ctx.channel.purge()   
                await ctx.respond('Shop nuked.', ephemeral=True)
            else:
                await ctx.respond('You don`t own a shop.', ephemeral=True)
        except:
            await ctx.respond('You don`t own a shop.', ephemeral=True)

@bot.slash_command(guild_ids=[guild], name='remove', description='Removes SHOP.')
async def remove(
    ctx,
    channel: Option(str, "Enter the channel ID", required=True),
):
    server = bot.get_guild(int(guild))
    channel23 = server.get_channel(int(channel))
    await ctx.respond('Channel removing...', ephemeral=True)
    if checkifroles(ctx) is True:
        config.remove_option('channel', channel)
        config.pop(channel) # Remove the channel from the config
        await channel23.delete() # Delete the channel
        with open(database, 'w') as configfile:
            config.write(configfile)
        await ctx.respond('Channel removed.', ephemeral=True)
    else:
        await ctx.respond('You do not have the required roles.', ephemeral=True)

@bot.slash_command(guild_ids=[guild], name='nukeall', description='Nukes all channel`s of the server.')
async def nukeall(
    ctx,
):
    if checkifroles(ctx) is True:
        await ctx.respond('Nuking channel`s.', ephemeral=True)
        server = bot.get_guild(int(guild))
        for channel in server.text_channels:
            channel23 = server.get_channel(int(channel.id))
            await channel23.purge()
        else:
            await ctx.respond('All channels nuked.', ephemeral=True)
    else:
        await ctx.respond('You do not have the required roles.', ephemeral=True)

@bot.slash_command(guild_ids=[guild], name='restore', description='Restores channel accses.')
async def restorechannel(
    ctx,
    key: Option(str, "Enter your key", required=True),
    channel: Option(str, "Enter the channel ID", required=True),
):
    server = bot.get_guild(int(guild))
    channel23 = server.get_channel(int(channel))
    await ctx.respond('Channel acsses restoring...', ephemeral=True)
    try:
        if key == config[channel]['key']:
            await channel23.set_permissions(ctx.author, send_messages=True, view_channel=True)
            await ctx.respond('Channel accses restored.', ephemeral=True)
        else:
            await ctx.respond('You do not own this channel.', ephemeral=True)
    except Exception as e:
        print(e)
        await ctx.respond('Invalid Data.', ephemeral=True)
    

@bot.slash_command(guild_ids=[guild], name='nukeshops', description='Nukes all shops.')
async def nukeshops(
    ctx,
):
    verifiedrole = discord.utils.get(ctx.guild.roles, id=memberrole)
    categorypremi = discord.utils.get(ctx.guild.categories, id=premiumcatid)
    categorynorm = discord.utils.get(ctx.guild.categories, id=normalcatid)
    categorytop = discord.utils.get(ctx.guild.categories, id=topcatid)
    if checkifroles(ctx) is True:
        server = bot.get_guild(int(guild))
        await ctx.respond('Nuking shops...', ephemeral=True)
        for channel in config['channel']:
            print(channel)
            channell = server.get_channel(int(channel))
            member = server.get_member(int(config[channel]['userid']))
            print(channell)
            await channell.delete()
            if config[channel]['type'] == 'premium':
                channel2 = await ctx.guild.create_text_channel(member.name, category=categorypremi)
            elif config[channel]['type'] == 'normal':
                channel2 = await ctx.guild.create_text_channel(member.name, category=categorynorm)
            elif config[channel]['type'] == 'top':
                channel2 = await ctx.guild.create_text_channel(member.name, category=categorytop)
            await channel2.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
            await channel2.set_permissions(verifiedrole, send_messages=False, view_channel=True)
            await channel2.set_permissions(member, send_messages=True, view_channel=True)
            config['channel'][str(channel2.id)] = str(channel2.id)
            config[channel2.id] = {'type': config[channel]['type'], 'key': config[channel]['key'], 'userid': config[channel]['userid'], 'pingdown': config[channel]['pingdown'], 'expiry': config[channel]['expiry']}
            config.remove_option('channel', channel)
            config.pop(channel)
            with open(database, 'w') as configfile:
                config.write(configfile)

            


    else:
        await ctx.respond('You are not an admin.', ephemeral=True)

@bot.slash_command(guild_ids=[guild], name='help', description='Shows the help menu.')
async def help(
    ctx,
):
    ctx.respond('This is the help menu', ephemeral=True)
    embedforsuccses = discord.Embed(title="Helpmenu", color=0xf609e2)
    embedforsuccses.add_field(name="!usekey [Your key]", value="Redeems your key and gives you a slot.", inline=False)
    embedforsuccses.add_field(name="!help", value="Shows this message.", inline=False)
    embedforsuccses.add_field(name="!ping", value="This will ping the users of the Server.!", inline=False)
    embedforsuccses.set_footer(text="[] = required, <> = optional \n Made with love by Mr.Gruppr")
    await ctx.respond(embed=embedforsuccses, ephemeral=True)


@bot.slash_command(guild_ids=[guild], name='shop', description='Shows the Shop menu.')
async def shop(ctx,
):
    ctx.respond('This is the shop menu.', ephemeral=True)
    embedforsuccses = discord.Embed(title= MPNAME + " Shop", description='These are all of our products'  ,color=0xf609e2)
    embedforsuccses.add_field(name="TOP", value="$75.00", inline=False)
    embedforsuccses.add_field(name="Premium", value="$40.00", inline=False)
    embedforsuccses.add_field(name="Normal", value="$25.00", inline=False)
    embedforsuccses.set_footer(text="Made with love by Mr.Gruppr")
    embedforsuccses.set_thumbnail(url=bot.user.avatar_url)
    await ctx.send(embed=embedforsuccses)

@bot.command()
async def stop(ctx):
    await ctx.message.delete()
    print("Bot is stopping...")
    if checkifroles(ctx) is True:
        quit()
    else:
        await ctx.send('You are not allowed to use this command.', delete_after=5)


@bot.command()
async def admin(ctx):
    await ctx.message.delete()
    if checkifroles(ctx) is True:
        embedforsuccses = discord.Embed(title="Help for admins", color=0xf609e2)
        embedforsuccses.add_field(name="/genkey [top / key / normal]", value="Genrates a KEY for a slot.", inline=False)
        embedforsuccses.add_field(name="/shop", value="Shows Shop menu!", inline=False)
        embedforsuccses.add_field(name="/stop", value="Stops the bot.", inline=False)
        embedforsuccses.add_field(name="/help", value="Shows the help menu.", inline=False)
        embedforsuccses.add_field(name="/ping", value="This will ping the users of the Server.!", inline=False)
        embedforsuccses.set_footer(text="Made with love by Mr.Gruppr")
        await ctx.send(embed=embedforsuccses, delete_after=6)
    else:
        await ctx.send("You don't have permission to use this command.", delete_after=5)


@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    if checkifroles(ctx) is True:
        await ctx.channel.purge()
    else:
        await ctx.send('You are not an admin.', delete_after=6)



bot.run(token)
