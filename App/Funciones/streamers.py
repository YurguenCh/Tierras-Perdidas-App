import requests
import discord
from discord.ext import tasks


client_id = 'z136a7slm5gp99x84wgh6kl6eusdan'
client_secret = 'gi2tqadpuor5rump6dko9fbiccfr6q'

# Solicitar un token de acceso
url = 'https://id.twitch.tv/oauth2/token'
params = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

response = requests.post(url, params=params)
access_token = response.json()['access_token']

headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {access_token}'
}

def check_stream_status(username):
    url = f'https://api.twitch.tv/helix/streams?user_login={username}'
    response = requests.get(url, headers=headers)
    data = response.json()

    if data['data']:
        return True  # El streamer está en vivo
    else:
        return False  # El streamer no está en vivo



# Define los intents
intents = discord.Intents.default()
intents.messages = True  # Habilita la intención de mensajes

botTP = discord.Client(intents=intents)

# Diccionario para llevar el seguimiento del estado de los streamers
streamer_status = {
    'MrNexor': False,
    'TioChinoVo': False,
    'Zokrex_': False,
    'Mari_92': False,
    'Yeyaberry': False
}

@botTP.event
async def on_ready():
    print(f'Logged in as {botTP.user}')
    en_vivo.start()

@tasks.loop(seconds=2)  # Verificar cada 2 minutos
async def en_vivo():
    channel = botTP.get_channel(1271905986294317157) #ID TP:1215846505085276198    #ID PRUEBAS:1271905986294317157
    for username in streamer_status:
        is_live = check_stream_status(username)
        if is_live and not streamer_status[username]:
            await channel.send(f'¡{username} está en vivo en Twitch!\n¡Míralo aquí: https://www.twitch.tv/{username}\n ||@here||')
            streamer_status[username] = True
        elif not is_live and streamer_status[username]:
            streamer_status[username] = False


botTP.run('MTI3MTg3ODM3NzAxNTQ3NjI4NA.GVqdxF.S75vGwtf0UkXIljZe8pkxXgtI-VDtFU66E1LQk')

