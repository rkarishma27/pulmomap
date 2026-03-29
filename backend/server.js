// backend/server.js
const express = require("express");
const { MongoClient, ObjectId } = require("mongodb");

const app = express();
app.use(express.json());

const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);
let collection;

async function initDB() {
    await client.connect();
    const db = client.db("pulmomap");
    collection = db.collection("patients");
}

initDB().catch(console.error);

app.post("/data", async (req, res) => {
    try {
        const data = req.body;  // {username, notes, age, ...}
        console.log("Received:", data);

        // Insert or update patient
        const filter = { username: data.username };
        const update = { $set: data };
        const options = { upsert: true }; // Create if doesn't exist
        await collection.updateOne(filter, update, options);

        res.send("OK");
    } catch (err) {
        console.log("Error:", err);
        res.status(500).send("Server Error");
    }
});

app.listen(5001, "0.0.0.0", () => {
    console.log("Node server running on port 5001");
});