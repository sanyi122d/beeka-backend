import os
import json
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Load Firebase service account JSON from environment variable
firebase_json_str = os.getenv("FIREBASE_SERVICE_ACCOUNT")
if not firebase_json_str:
    raise Exception("FIREBASE_SERVICE_ACCOUNT environment variable not found")

# Parse the JSON string to dict
firebase_credentials_dict = json.loads(firebase_json_str)

# Initialize Firebase app with credentials from dict
cred = credentials.Certificate(firebase_credentials_dict)
firebase_admin.initialize_app(cred)

# Firestore client
firestore_client = firestore.client()

def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception:
        return None
