from fastapi import APIRouter, Form
from utils import save_audio
from predictor import save_and_predict
from db import collection

router = APIRouter()

@router.post("/submit_data")
async def submit_data(
    patient_id: str = Form(...),
    sensor: str = Form(...),
    spo2: float = Form(...),
    heart_rate: float = Form(...),
    audio_base64: str = Form(None)
):
    audio_path = save_audio(patient_id, sensor, audio_base64) if audio_base64 else None
    critical = save_and_predict(patient_id, sensor, audio_path, spo2, heart_rate)
    return {"status": "saved", "critical": critical}

@router.get("/check_alert/{patient_id}/{sensor}")
def check_alert(patient_id: str, sensor: str):
    last_entry = collection.find_one(
        {"patient_id": patient_id, "sensor": sensor},
        sort=[("created_at", -1)]
    )
    return {"critical": last_entry.get("critical", False)} if last_entry else {"critical": False}

@router.get("/patient/{patient_id}")
def get_patient_report(patient_id: str):
    samples = list(collection.find({"patient_id": patient_id}))
    for s in samples:
        s["_id"] = str(s["_id"])
    return {"samples": samples}

@router.get("/admin")
def get_all_patients():
    pipeline = [{"$group": {"_id": "$patient_id", "latest": {"$last": "$$ROOT"}}}]
    patients = list(collection.aggregate(pipeline))
    for p in patients:
        p["latest"]["_id"] = str(p["latest"]["_id"])
    return {"patients": patients}