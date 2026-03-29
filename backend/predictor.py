from db import collection
from model import predict
from utils import check_critical

def save_and_predict(patient_id, sensor, audio_path, spo2, heart_rate):
    prediction = None
    if audio_path:
        prediction = predict(audio_path)

    critical = check_critical(prediction, spo2, heart_rate)

    collection.insert_one({
        "patient_id": patient_id,
        "sensor": sensor,
        "prediction": prediction,
        "spo2": spo2,
        "heart_rate": heart_rate,
        "critical": critical,
        "created_at": datetime.utcnow()
    })

    return critical