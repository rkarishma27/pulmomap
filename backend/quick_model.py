import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Simulated feature vectors (like MFCC features)
X = np.random.rand(200, 40)

# Labels: 0 = Normal, 1 = Crackle, 2 = Wheeze
y = np.random.randint(0, 3, 200)

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "lung_model.pkl")

print("Pretrained model saved!")