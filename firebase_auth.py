import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import firestore

cred = credentials.Certificate("/firebase_service_account.json")
firebase_admin.initialize_app(cred)

# Firestore client
firestore_client = firestore.client()

def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        return None
