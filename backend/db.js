const { MongoClient } = require('mongodb');

const MONGO_URL = "mongodb+srv://PULMOMAP:PULMOMAP1@m0.em9az7e.mongodb.net/?retryWrites=true&w=majority";
const DB_NAME = "pulmomap";
const COLLECTION_NAME = "lung_samples";

let collection;

async function connectDB() {
    try {
        const client = new MongoClient(MONGO_URL, { useNewUrlParser: true, useUnifiedTopology: true });
        await client.connect();
        console.log("✅ MongoDB connected");
        const db = client.db(DB_NAME);
        collection = db.collection(COLLECTION_NAME);
        return collection;
    } catch (err) {
        console.error("❌ MongoDB connection error:", err);
        process.exit(1);
    }
}

module.exports = { connectDB, getCollection: () => collection };