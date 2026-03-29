import librosa
import numpy as np
import joblib

model = joblib.load("lung_model.pkl")

def extract_features(file_path):
    try:
        audio, sr = librosa.load(file_path, sr=16000)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
        features = np.mean(mfccs.T, axis=0)
        return features.reshape(1, -1)
    except:
        return None

def predict(audio_path):
    features = extract_features(audio_path)
    if features is None:
        return {"class": "error", "confidence": 0}

    pred = model.predict(features)[0]
    prob = model.predict_proba(features).max()
    classes = ["Normal", "Crackle", "Wheeze"]

    return {"class": classes[pred], "confidence": float(prob)}