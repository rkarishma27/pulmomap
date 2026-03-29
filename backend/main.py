# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bson import ObjectId
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["pulmomap"]
collection = db["patients"]

# FastAPI app
app = FastAPI()

# CORS (React frontend on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Pydantic model for login
class LoginRequest(BaseModel):
    username: str
    password: str

# Ensure at least one default patient
def ensure_default_patient():
    if collection.count_documents({}) == 0:
        collection.insert_one({
            "username": "patient",
            "password": "1234",
            "name": "Default Patient",
            "age": 30,
            "notes": "",
        })

ensure_default_patient()

# Login endpoint
@app.post("/login")
def login(req: LoginRequest):
    user = collection.find_one({"username": req.username})
    if not user:
        return {"success": False, "message": "User not found"}
    if user["password"] != req.password:
        return {"success": False, "message": "Incorrect password"}
    return {"success": True, "user_id": str(user["_id"]), "name": user["name"]}

# Get patient report
@app.get("/heatmap/{patient_id}")
def heatmap(patient_id: str):
    # For simplicity, generate dummy 2x2 heatmap
    patient = collection.find_one({"_id": ObjectId(patient_id)})
    if not patient:
        return [[0, 0], [0, 0]]
    return [[0.7, 0.2], [0.1, 0.9]]  # Replace with real AI data