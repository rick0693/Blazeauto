import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Inicialize o SDK do Firebase com suas credenciais
cred = credentials.Certificate('bancoblaze-firebase-adminsdk-e6pzh-9213df4821.json')
firebase_admin.initialize_app(cred)

# Inicialize o cliente do Firestore
db = firestore.client()

def armazenar_dados_firestore(dados):
    doc_ref = db.collection('dados').document()
    doc_ref.set(dados)
    print("Dados armazenados no Firestore:", dados)
