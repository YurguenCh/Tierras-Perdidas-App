import os
import discord
from discord.ext import commands

# Cargar el token desde el archivo .env
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurar los intents
intents = discord.Intents.default()
intents.message_content = True  # Esto permite que el bot pueda leer los mensajes del servidor

# Crear la instancia del bot
botTP = commands.Bot(command_prefix='!', intents=intents)

class Anuncios(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='anuncio')
    @commands.has_role('Founder')
    async def anuncio(self, ctx, *, anuncio):
        channel = self.bot.get_channel(1272176125497446476)
        if channel:
            await channel.send(
                embed=discord.Embed(
                    title="ANUNCIO",
                    description=anuncio,
                    color=discord.Color.green()
                ).set_image(url="https://cdn.discordapp.com/attachments/812737500949774406/1271992980051460116/TierrasPerdidasRP-Logo_1.png")
            )
            await ctx.send("Anuncio enviado!")
        else:
            await ctx.send("Error al obtener la información!")

# Agregar el cog al bot
botTP.add_cog(Anuncios(botTP))

#----------------Comando 2--------------------------#

@botTP.command(name='m')
async def multiplicar(ctx, num1: int, num2: int):
    response = int(num1) * int(num2)
    await ctx.send(f"El resultado es {response}")

botTP.run('MTI3MTg3ODM3NzAxNTQ3NjI4NA.GVqdxF.S75vGwtf0UkXIljZe8pkxXgtI-VDtFU66E1LQk')