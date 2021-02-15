import discord
from discord.ext import commands
from discord import File

client = commands.Bot(command_prefix='>' , help_command = None)
token = "TOKEN HERE"
@client.event
async def on_ready():
    activity = discord.Game(name="بيض", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

@client.command()
async def server(ctx):
  embed = discord.Embed(title = f'Server Info')
  embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.add_field(name="Info", value=f'**Owner** : <@{ctx.guild.owner_id}> | `{ctx.guild.owner_id}` \n**Name** : {ctx.guild.name} | `{ctx.guild.id}` \n**Banned Member** : {len(await ctx.guild.bans())}\n**Region** : {ctx.guild.region}\n**Created at** : {ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S")} \n**Roles** : {len(ctx.guild.roles)}\n**Emojis** : {len(ctx.guild.emojis)}',inline=False)
  embed.add_field(name="Members",value=f'**Members** : {len(ctx.guild.members)} \n**Humans** : {len(list(filter(lambda m: not m.bot, ctx.guild.members)))}\n**Bots** : {len(list(filter(lambda m: m.bot, ctx.guild.members)))}',inline=False)
  embed.add_field(name="Channel",value=f'**Text channels** : {len(ctx.guild.text_channels)}\n**Voice channels** : {len(ctx.guild.voice_channels)}\n**Categories** : {len(ctx.guild.categories)}\n**System Channel** : {ctx.guild.system_channel}\n**Afk Channel** : {ctx.guild.afk_channel}')
  embed.set_footer(text=f"{ctx.author} | بطلب من ", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)



@client.command()
async def userinfo(ctx, member: discord.Member = None):
  member = ctx.author if not member else member
  roles = [role for role in member.roles]

  embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
  embed.set_author(name=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name="Info", value=f'**User Name** : {member} \n**ID** : {member.id} \n**Nick Name** : {member.display_name}\n**Created At** : {member.created_at.strftime("%d/%m/%Y %H:%M:%S")}\n**Status** : {str(member.status).title()}\n**Bot?** : {member.bot}',inline=False)
  embed.add_field(name="Member", value=f'**Joined at** : {member.joined_at.strftime("%d/%m/%Y %H:%M:%S")}\n**Top role** : {member.top_role.mention}')
  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]) , inline=False)
  embed.set_footer(text=f"{ctx.author} | بطلب من ", icon_url=ctx.author.avatar_url)

  await ctx.send(embed=embed)

client.run(token)