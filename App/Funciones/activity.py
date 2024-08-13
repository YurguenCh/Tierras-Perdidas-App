import discord
from discord.ext import commands, tasks
import subprocess
import json

# Crear una instancia de intents y activar los permisos necesarios
intents = discord.Intents.default()
intents.message_content = True  # Esto permite que el bot pueda leer los mensajes del servidor

botTP = commands.Bot(command_prefix='!', intents=intents)

# Variable global para almacenar la referencia al mensaje
message_reference = None

@tasks.loop(minutes=5)  # Cambia el intervalo aquí (en minutos)
async def en_linea():
    global message_reference
    server_info = get_fivem_server_info()
    if server_info:
        server_status = server_info.get('serverStatus', {})
        players = server_info.get('players', 0)
        maxplayers = server_info.get('maxClients', 30)
        activity_message = f"jugar a {players} / 120 "
        status_message = f"Hay {players} jugadores conectados | Estado: {'Online' if server_status.get('online') else 'Offline'}"
        # Configurar la actividad personalizada (Rich Presence simulada)
        activity = discord.Activity(
            name=activity_message,
            # Tipo de actividad (PLAYING, STREAMING, COMPETING, WATCHING, LISTENING)# El texto que quieres mostrar
            type=discord.ActivityType.watching 
        )
        await botTP.change_presence(activity=activity)
        
        # Enviar o actualizar el mensaje en el canal
        channel = botTP.get_channel(1271905986294317157)  # Reemplaza con el ID del canal donde quieres enviar el mensaje
        if channel:
            if message_reference is None:
                # Enviar el mensaje inicial
                message_reference = await channel.send(
                    content=status_message,
                    embed=discord.Embed(
                        title="Información de Tierras Perdidas",
                        description=status_message,
                        color=discord.Color.blue()
                    ).set_image(url="https://cdn.discordapp.com/attachments/812737500949774406/1271992980051460116/TierrasPerdidasRP-Logo_1.png?ex=66b95b46&is=66b809c6&hm=743ca1309ef6374152f3bebc65cf1edec0ffd619c08b93fed0feddc9fe004de3&")  # Reemplaza con la URL de la imagen del servidor
                )
            else:
                # Actualizar el mensaje existente
                await message_reference.edit(
                    content=status_message,
                    embed=discord.Embed(
                        title="Información de Tierras Perdidas",
                        description=status_message,
                        color=discord.Color.green()
                    ).set_image(url="https://cdn.discordapp.com/attachments/812737500949774406/1271992980051460116/TierrasPerdidasRP-Logo_1.png?ex=66b95b46&is=66b809c6&hm=743ca1309ef6374152f3bebc65cf1edec0ffd619c08b93fed0feddc9fe004de3&")  # Reemplaza con la URL de la imagen del servidor
                )
    else:
        print("No se pudo obtener la información del servidor de FiveM.")

def get_fivem_server_info():
    try:
        result = subprocess.run(['node', 'App/Funciones/api.js'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("JavaScript Output:", result.stdout)
        
        if result.returncode != 0:
            print("Error executing the JavaScript file:", result.stderr)
            return None
        
        output_lines = result.stdout.splitlines()
        json_output = output_lines[-1]  # Suponiendo que la última línea es el JSON
        server_info = json.loads(json_output)
        return server_info
    except json.JSONDecodeError:
        print("Error decoding JSON from JavaScript output.")
        print("Received output:", result.stdout)
        return None
    except Exception as e:
        print("An error occurred while getting server info:", e)
        return None


@botTP.event
async def on_ready():
    print(f'Logged in as {botTP.user}')
    # Iniciar la tarea periódica
    en_linea.start()

            
# Ejecutar el bot
botTP.run('MTI3MTg3ODM3NzAxNTQ3NjI4NA.GVqdxF.S75vGwtf0UkXIljZe8pkxXgtI-VDtFU66E1LQk')