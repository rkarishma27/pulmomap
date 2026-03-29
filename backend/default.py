from db import collection

# Ensure admin exists
collection.update_one(
    {"username": "admin", "role": "admin"},
    {"$set": {"password": "1234", "name": "Admin User", "age": 30, "notes": ""}},
    upsert=True
)

# Ensure patient exists
collection.update_one(
    {"username": "patient", "role": "patient"},
    {"$set": {"password": "1234", "name": "Test Patient", "age": 25, "notes": ""}},
    upsert=True
)

print("Default users are ready!")