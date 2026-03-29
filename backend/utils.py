import os
from datetime import datetime
import base64

def save_audio(patient_id, sensor, audio_base64):
    audio_bytes = base64.b64decode(audio_base64)
    timestamp = int(datetime.now().timestamp())
    filename = f"audio/{patient_id}_{sensor}_{timestamp}.wav"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        f.write(audio_bytes)
    return filename

def check_critical(prediction, spo2, heart_rate):
    if prediction and prediction["class"] in ["Crackle", "Wheeze"]:
        return True
    if spo2 < 90 or heart_rate > 120:
        return True
    return False