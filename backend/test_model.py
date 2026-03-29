import joblib

model = joblib.load("lung_model.pkl")
print("Loaded:", type(model))