# backend/db.py
from pymongo import MongoClient
import certifi

MONGO_URL = "mongodb+srv://PULMOMAP:PULMOMAP1@m0.em9az7e.mongodb.net/?appName=M0"
client = MongoClient(MONGO_URL, tlsCAFile=certifi.where())

db = client["pulmomap"]
collection = db["patients"]  # Patient collection