import discord
from secret.config import get_api_token, get_service_key_path

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

service_key_path = get_service_key_path()
cred = credentials.Certificate(service_key_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

#doc_ref = db.collection(u'users').document(u'alovelace')
#doc_ref.set({
#    u'first': u'Ada',
#    u'last': u'Lovelace',
#    u'born': 1815
#})

users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
