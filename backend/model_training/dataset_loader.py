import os
import librosa
import numpy as np

DATASET_PATH = r"../dataset/audio_and_txt_files"

def extract_label(txt_file):
    try:
        with open(txt_file, "r") as f:
            content = f.read().lower()

        if "crackles" in content:
            return 1
        elif "wheezes" in content:
            return 2
        else:
            return 0
    except:
        return 0


def extract_features(audio_path):
    try:
        audio, sr = librosa.load(audio_path, sr=16000)

        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
        mfccs_mean = np.mean(mfccs.T, axis=0)

        return mfccs_mean
    except:
        return None


def load_data(limit=500):
    X, y = [], []

    count = 0

    for file in os.listdir(DATASET_PATH):
        if file.endswith(".wav") and count < limit:

            wav_path = os.path.join(DATASET_PATH, file)
            txt_path = wav_path.replace(".wav", ".txt")

            features = extract_features(wav_path)
            label = extract_label(txt_path)

            if features is not None:
                X.append(features)
                y.append(label)
                count += 1

    return np.array(X), np.array(y)