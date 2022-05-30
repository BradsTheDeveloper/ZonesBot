import discord
from secret.config import get_api_token, get_service_key_path

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

service_key_path = get_service_key_path()
cred = credentials.Certificate(service_key_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

client = discord.Client()
api_token = get_api_token()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('z!setup'):
        await message.channel.send('Welcome to ZonesBot!')
        await message.channel.send('Please enter your timezone:')
        #await message.channel.send('Please react to one of the emoji to select your timezone:')
        uid = str(message.author.id) # Getting user's id
        doc_ref = db.collection(u'users').document(uid)
        doc_ref.set({
            u'name': u'Ada',
            u'timezone': u'GMT'
        })

client.run(api_token)
