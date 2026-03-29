import joblib
from sklearn.ensemble import RandomForestClassifier
from dataset_loader import load_data

# Load dataset
X, y = load_data(limit=500)
print("Data loaded:", X.shape, y.shape)

# Train model with 40 features
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model
joblib.dump(model, "../lung_model.pkl")
print("✅ Model trained and saved as lung_model.pkl")