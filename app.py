import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from App.Funciones import activity, streamers

# Cargar el token desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Crear una instancia de intents y activar los permisos necesarios
intents = discord.Intents.default()
intents.message_content = True

# Crear la instancia del bot
botTP = commands.Bot(command_prefix='!', description="BOT AUN EN PRUEBAS", intents=intents)

# Activar la funcionalidad de actualización de actividad (FiveM)
@botTP.event
async def on_ready():
    print(f'Logged in as {botTP.user}'),
    activity.en_linea.start(), # Iniciar la tarea periódica
    streamers.en_vivo.start(), # Iniciar la verificación de streamers
    botTP.load_extension('App.Funciones.commands')

# Ejecutar el bot
botTP.run('MTI3MTg3ODM3NzAxNTQ3NjI4NA.GVqdxF.S75vGwtf0UkXIljZe8pkxXgtI-VDtFU66E1LQk')