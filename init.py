import dotenv
import logging
import os
import firebase_admin
from firebase_admin import credentials, firestore
from groq import Groq
def init():
    dotenv.load_dotenv()
    logging.basicConfig(level=logging.INFO)
    firebase_auth_path=os.getenv("FIREBASE_AUTH_PATH")
    cred = credentials.Certificate(firebase_auth_path)

    firebase_admin.initialize_app(cred)
    # Initialize the Groq API key
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    return firestore.client(),client

