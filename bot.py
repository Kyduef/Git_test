import discord
from discord.ext import commands
from config import token  # Import the bot's token from configuration file
from config import own_id

intents = discord.Intents.default()
intents.members = True  # Allows the bot to work with users and ban them
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start(ctx):
    await ctx.send("Hi! I'm a chat manager bot!")

YOUR_USER_ID = own_id  #change with owner id

@bot.command()
async def ban(ctx, member: discord.Member = None, *, reason: str = "No reason provided"):
    if ctx.author.id != YOUR_USER_ID:
        await ctx.send("❌ Kamu tidak diizinkan menggunakan perintah ini.")
        return

    if not member:
        await ctx.send("Format: `!ban @user [alasan]`")
        return

    if ctx.guild.me.top_role <= member.top_role:
        await ctx.send("⚠️ Saya tidak dapat ban pengguna dengan peran lebih tinggi atau sama.")
        return

    try:
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"✅ Pengguna **{member.name}** telah diblokir. Alasan: {reason}")
    except discord.Forbidden:
        await ctx.send("❌ Saya tidak punya izin untuk melakukan ban.")
    except discord.HTTPException as e:
        await ctx.send(f"❌ Gagal untuk ban pengguna. Error: {e}")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have sufficient permissions to execute this command.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("User not found.")

bot.run(token)t to the user you want to ban. For example: `!ban @user`")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have sufficient permissions to execute this command.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("User not found.")

bot.run(token)
