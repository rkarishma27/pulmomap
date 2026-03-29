import librosa
import numpy as np

def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=16000)

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)

    features = np.mean(mfcc.T, axis=0)

    return features