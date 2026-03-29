🫁 PulmoMap – AI-Powered Lung Health Monitoring System
📌 Overview

PulmoMap is an AI-driven healthcare platform that enables real-time lung sound analysis and visualization. The system collects respiratory data from external devices, processes it using machine learning, and presents an intuitive patient dashboard with spatial heatmaps indicating potential abnormalities.

🚀 Features
🔐 Patient Login System (secure authentication)
🧠 AI-Based Lung Sound Classification
Detects: Normal, Crackle, Wheeze
🎯 Confidence-Based Predictions
🗺️ 2×2 Spatial Heatmap Visualization
Represents different lung regions
🔄 Real-Time Data Integration
External device → Node server → Database
🌐 Full Stack Architecture
React Frontend + FastAPI Backend + MongoDB
🏗️ Tech Stack
Frontend
React.js
HTML, CSS (minimal stable UI)
Backend
FastAPI (Python)
Node.js (for real-time data ingestion)
Database
MongoDB
AI/ML
Scikit-learn (Random Forest Classifier)
Librosa (MFCC feature extraction)
🧠 How It Works
📡 Data Collection
Lung sound data is captured via external sensors/device.
📥 Data Transmission
Sent to Node.js server (/data endpoint).
💾 Storage
Stored in MongoDB per patient.
🧠 AI Processing
Audio → MFCC Features → ML Model
Classified into:
Normal
Crackle
Wheeze
📊 Visualization
Confidence scores mapped into a 2×2 lung heatmap:
[ Top Left   | Top Right  ]
[ Bottom Left| Bottom Right ]
👤 Frontend Display
Patient logs in and views AI-generated report.
