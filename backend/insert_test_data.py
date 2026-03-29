from pymongo import MongoClient


MONGO_URL = "mongodb+srv://PULMOMAP:PULMOMAP1@m0.em9az7e.mongodb.net/?appName=M0"


client = MongoClient(MONGO_URL)

db = client["pulmomap"]
collection = db["lung_samples"]

collection.delete_many({})


sample_data = [
    {
        "patient_id": "P001",
        "sensor": "top_left",
        "audio_path": "dataset/audio_and_txt_files/sample.wav",
        "prediction": None
    },
    {
        "patient_id": "P001",
        "sensor": "top_right",
        "audio_path": "dataset/audio_and_txt_files/sample.wav",
        "prediction": None
    },
    {
        "patient_id": "P001",
        "sensor": "bottom_left",
        "audio_path": "dataset/audio_and_txt_files/sample.wav",
        "prediction": None
    },
    {
        "patient_id": "P001",
        "sensor": "bottom_right",
        "audio_path": "dataset/audio_and_txt_files/sample.wav",
        "prediction": None
    }
]

collection.insert_many(sample_data)

print("✅ Test data inserted successfully!")