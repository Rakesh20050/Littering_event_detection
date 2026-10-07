# 🤖 Smart Monitoring AI

### AI-Based Littering Event Detection, Verification, Identity Recognition & Hotspot Analysis

> **Smart Monitoring AI** is an AI-first computer vision platform that detects littering events, tracks people and waste, identifies registered individuals when confidence is sufficient, reconstructs events over time, routes uncertain cases to a human Control Room, and analyzes historical incidents to predict littering hotspots.

<p align="center">

**Computer Vision · Deep Learning · Multi-Object Tracking · Face Recognition · Temporal AI · Human-in-the-Loop · Predictive Analytics**

</p>

---

## 🚀 Overview

Smart Monitoring AI is designed for environments such as:

* 🏫 Colleges and universities
* 🏙️ Smart cities
* 🌳 Parks and public spaces
* 🚉 Railway and metro stations
* 🏢 Institutional campuses
* 🏘️ Residential communities

The system does more than simply detect garbage.

It attempts to understand:

> **Who was present? What happened? Did the person actually litter? How confident is the AI? What evidence supports the decision? Should the person be notified, or should a human review the case? Where are littering incidents repeatedly occurring?**

The project combines multiple AI components into one pipeline:

```text
Camera
   ↓
Object Detection
   ↓
Multi-Object Tracking
   ↓
Person Identity Recognition
   ↓
Person–Waste Interaction
   ↓
Temporal Event Understanding
   ↓
Confidence & Evidence Analysis
   ↓
Decision Engine
   ↓
┌───────────────────────────────┐
│                               │
│ High Confidence               │ Low / Uncertain Confidence
│                               │
↓                               ↓
Person Notification             Control Room
│                               │
│ "NO" / Dispute                │
↓                               ↓
Control Room Human Review ←─────┘
│
├── Reject
│
└── Verify
      ↓
Incident + Targeted Notification
      ↓
Authority Alert
      ↓
Historical Data
      ↓
Hotspot Analysis / Risk Prediction
      ↓
Human Feedback
      ↓
Future Model Improvement
```

---

# 🎯 Problem Statement

Traditional CCTV systems primarily record video.

They do not automatically understand:

* who interacted with a waste object,
* whether the object was actually discarded,
* whether someone picked it back up,
* whether the person used a proper bin,
* whether the observed person is a registered individual,
* whether the AI is sufficiently confident,
* whether an incident requires human verification,
* or where repeated incidents are forming.

Smart Monitoring AI attempts to transform passive CCTV footage into an **AI-assisted monitoring and decision-support system**.

---

# ✨ Key Features

## 👁️ Real-Time Computer Vision

* Person detection
* Waste/litter detection
* Bin detection
* Real-time object tracking
* Multiple-person tracking
* Camera stream processing

## 🧍 Identity Recognition

* Registered-person enrollment
* Face capture
* Face embeddings
* Identity matching
* Confidence scoring
* Unknown-person rejection
* Track ID ↔ identity association

## 🗑️ Littering Event Understanding

The system does not treat the presence of garbage near a person as proof of littering.

Instead, it attempts to reconstruct the temporal sequence:

```text
Person approaches / holds object
          ↓
Person moves with object
          ↓
Object is released
          ↓
Object reaches ground / unwanted location
          ↓
Person leaves
```

This produces a **littering event candidate**.

The system can also model:

```text
Pickup
   ↓
Object recovered
```

and:

```text
Proper Disposal
   ↓
Object placed into detected bin
```

---

# 🧠 AI Confidence & Human Verification

One of the core design principles is that **identity and event detection are separate AI problems**.

For example:

```text
Track #17
   ↓
Identity: Rahul
Identity confidence: 91%
   ↓
Littering event confidence: 78%
```

The system can therefore reason about:

```text
WHO?
+
WHAT HAPPENED?
+
HOW CONFIDENT IS THE AI?
```

## Current 60% Decision Rule

The project uses a configurable **60% threshold** for preliminary routing.

| Situation                         | Action                                          |
| --------------------------------- | ----------------------------------------------- |
| Identity + event confidence ≥ 60% | Send preliminary notification to matched person |
| Person accepts/acknowledges       | Record response                                 |
| Person says **NO**                | Send case to Control Room                       |
| Identity confidence < 60%         | Control Room review                             |
| Event confidence < 60%            | Control Room review                             |
| Human verifies                    | Verified incident                               |
| Human rejects                     | Incident rejected/closed                        |

### Important

**60% does not mean the AI has proven guilt.**

It is a project decision threshold used to determine whether the system is confident enough to issue a **preliminary notification**.

The threshold should be experimentally validated against the project's own test data.

---

# 🔄 Example Incident Flow

Suppose three people are visible:

```text
Track #17 → Rahul
Track #21 → Priya
Track #25 → Unknown
```

The AI observes:

```text
Track #21
   ↓
Waste interaction
   ↓
Release
   ↓
Waste lands
   ↓
Person leaves
   ↓
Event confidence = 78%
Identity confidence = 91%
```

The system generates:

```text
PRELIMINARY INCIDENT
Person: Priya
Event confidence: 78%
Identity confidence: 91%
```

Priya receives a notification.

If Priya selects:

```text
NO
```

the system does **not automatically punish or escalate the person**.

Instead:

```text
Priya → NO
       ↓
Control Room Alert
       ↓
Evidence Package
       ↓
Human Review
       ↓
VERIFY / REJECT
```

This creates a **Human-in-the-Loop AI system**.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │ Camera / CCTV    │
                    │ Phone Camera     │
                    │ USB Camera       │
                    └────────┬─────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │     AI PIPELINE       │
                 │                       │
                 │ YOLO Detection        │
                 │ ByteTrack             │
                 │ Face Recognition      │
                 │ Pose / Interaction    │
                 │ Event Understanding   │
                 │ Decision Engine       │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   FastAPI Backend     │
                 │   WebSocket Events    │
                 └───────────┬───────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
        ┌────────────┐ ┌────────────┐ ┌────────────┐
        │   Person   │ │   Control  │ │ Authority  │
        │   Screen   │ │    Room    │ │   Screen   │
        └────────────┘ └────────────┘ └────────────┘
                             │
                             ▼
                   ┌──────────────────┐
                   │ PostgreSQL /     │
                   │ PostGIS Database │
                   └────────┬─────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Historical AI      │
                  │ DBSCAN + XGBoost   │
                  └────────────────────┘
```

---

# 🖥️ Four-Device Deployment

The system supports multiple physical devices.

### Device 1 — Camera

Can be:

* CCTV
* USB webcam
* Laptop webcam
* Phone camera
* IP camera

The camera sends video to the AI processing system.

### Device 2 — Person Screen

Multiple people can use this screen/application.

Responsibilities:

* Registration
* Face capture
* Profile
* Personal notifications
* Incident response
* Personal reports

### Device 3 — Control Room

One Control Room device is sufficient for the operational center.

It handles:

* Live camera
* AI analysis
* Person tracking
* Identity
* Evidence
* Incident review
* Human verification
* Historical analytics
* Hotspot analysis
* Cleanup monitoring
* Activity logs
* Reports

### Device 4 — Authority

One Authority device is sufficient.

It receives:

* Important notifications
* Verified incident reports
* Hotspot alerts
* High-level information

---

# 🧩 Project Directory

```text
Smart-Monitoring-AI/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── camera/
│   ├── camera_client.py
│   ├── video_stream.py
│   ├── frame_sender.py
│   ├── camera_config.py
│   └── README.md
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── api/
│   │   ├── incidents.py
│   │   ├── cameras.py
│   │   ├── people.py
│   │   ├── reviews.py
│   │   ├── hotspots.py
│   │   └── reports.py
│   │
│   ├── services/
│   │   ├── incident_service.py
│   │   ├── camera_service.py
│   │   ├── identity_service.py
│   │   ├── notification_service.py
│   │   └── hotspot_service.py
│   │
│   ├── websocket/
│   │   ├── manager.py
│   │   └── events.py
│   │
│   └── migrations/
│       └── README.md
│
├── database/
│   ├── schema.sql
│   ├── seed_data.sql
│   ├── README.md
│   └── backups/
│
├── data/
│   ├── raw/
│   │   ├── waste/
│   │   ├── people/
│   │   ├── littering/
│   │   ├── pickup/
│   │   ├── proper_disposal/
│   │   ├── cleaning_activity/
│   │   └── multi_person/
│   │
│   ├── external/
│   │   ├── TACO/
│   │   ├── COCO/
│   │   ├── TrashNet/
│   │   └── Market-1501/
│   │
│   ├── registered_people/
│   │
│   ├── annotations/
│   │   ├── detection/
│   │   ├── tracking/
│   │   ├── identity/
│   │   ├── littering_events/
│   │   ├── pickup_events/
│   │   └── disposal_events/
│   │
│   ├── processed/
│   ├── splits/
│   │   ├── train/
│   │   ├── validation/
│   │   └── test/
│   │
│   └── feedback/
│       ├── verified/
│       ├── rejected/
│       └── corrected/
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_dataset_preparation.ipynb
│   ├── 03_waste_detection_training.ipynb
│   ├── 04_person_detection_testing.ipynb
│   ├── 05_tracking_experiments.ipynb
│   ├── 06_identity_registration.ipynb
│   ├── 07_face_recognition_testing.ipynb
│   ├── 08_littering_event_training.ipynb
│   ├── 09_pickup_disposal_analysis.ipynb
│   ├── 10_model_evaluation.ipynb
│   ├── 11_human_feedback_analysis.ipynb
│   ├── 12_retraining.ipynb
│   └── 13_hotspot_prediction.ipynb
│
├── models/
│   ├── detection/
│   │   ├── waste_best.pt
│   │   ├── person_best.pt
│   │   └── bin_best.pt
│   │
│   ├── tracking/
│   │   └── reid_model/
│   │
│   ├── identity/
│   │   ├── face_model/
│   │   └── registered_embeddings/
│   │       ├── embeddings.npy
│   │       └── labels.json
│   │
│   ├── event/
│   │   ├── littering_model.pt
│   │   ├── pickup_model.pt
│   │   └── disposal_model.pt
│   │
│   └── hotspot/
│       ├── xgboost_model.pkl
│       └── clustering_model.pkl
│
├── src/
│   ├── detection/
│   │   ├── person_detector.py
│   │   ├── waste_detector.py
│   │   ├── bin_detector.py
│   │   └── detection_utils.py
│   │
│   ├── tracking/
│   │   ├── tracker.py
│   │   ├── track_manager.py
│   │   └── reid.py
│   │
│   ├── identity/
│   │   ├── face_detector.py
│   │   ├── face_encoder.py
│   │   ├── identity_matcher.py
│   │   └── registration.py
│   │
│   ├── event/
│   │   ├── interaction.py
│   │   ├── littering_detector.py
│   │   ├── pickup_detector.py
│   │   ├── disposal_detector.py
│   │   └── event_state_machine.py
│   │
│   ├── decision/
│   │   ├── confidence.py
│   │   ├── context.py
│   │   ├── evidence.py
│   │   └── decision_engine.py
│   │
│   ├── review/
│   │   ├── evidence_package.py
│   │   ├── human_review.py
│   │   └── feedback.py
│   │
│   ├── hotspot/
│   │   ├── feature_engineering.py
│   │   ├── clustering.py
│   │   ├── risk_prediction.py
│   │   └── hotspot_map.py
│   │
│   ├── pipeline/
│   │   ├── camera.py
│   │   ├── ai_pipeline.py
│   │   └── realtime.py
│   │
│   └── utils/
│       ├── config.py
│       ├── logging.py
│       ├── visualization.py
│       └── video_utils.py
│
├── screens/
│   ├── person/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── registration.py
│   │   ├── profile.py
│   │   ├── my_reports.py
│   │   └── notifications.py
│   │
│   ├── control_room/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── command_center.py
│   │   ├── live_monitor.py
│   │   ├── incident_review.py
│   │   ├── evidence_viewer.py
│   │   ├── person_tracking.py
│   │   ├── ai_analysis.py
│   │   ├── hotspot_analysis.py
│   │   ├── historical_analytics.py
│   │   ├── cleanup_monitor.py
│   │   ├── activity_log.py
│   │   └── reports.py
│   │
│   └── authority/
│       ├── __init__.py
│       ├── app.py
│       ├── dashboard.py
│       ├── notifications.py
│       ├── incident_reports.py
│       └── hotspot_alerts.py
│
├── incidents/
│   ├── active/
│   ├── pending_review/
│   ├── verified/
│   ├── rejected/
│   └── resolved/
│
├── outputs/
│   ├── detections/
│   ├── tracking/
│   ├── identity/
│   ├── evidence/
│   ├── evaluations/
│   ├── hotspot_maps/
│   └── reports/
│
├── configs/
│   ├── detection.yaml
│   ├── identity.yaml
│   ├── event.yaml
│   ├── thresholds.yaml
│   ├── camera.yaml
│   ├── database.yaml
│   └── server.yaml
│
└── tests/
    ├── test_detection.py
    ├── test_tracking.py
    ├── test_identity.py
    ├── test_events.py
    ├── test_decision.py
    ├── test_backend.py
    └── test_pipeline.py
```

---

# 🧠 AI / ML Models

| AI Component          | Technology               | Purpose                        |
| --------------------- | ------------------------ | ------------------------------ |
| Person Detection      | **YOLOv8**               | Detect people                  |
| Waste Detection       | **YOLOv8**               | Detect litter/waste            |
| Bin Detection         | **YOLOv8**               | Detect bins                    |
| Multi-Object Tracking | **ByteTrack**            | Maintain Track IDs             |
| Pose Analysis         | **MediaPipe Pose**       | Support interaction analysis   |
| Person Re-ID          | **OSNet / Re-ID model**  | Support person continuity      |
| Face Recognition      | **Face embedding model** | Match registered people        |
| Littering Event AI    | Temporal/event model     | Understand littering sequence  |
| Pickup Detection      | Event model              | Detect recovery/pickup         |
| Disposal Detection    | Event model              | Detect proper disposal         |
| Hotspot Clustering    | **DBSCAN**               | Find spatial incident clusters |
| Risk Prediction       | **XGBoost**              | Predict future hotspot risk    |

---

# 📊 Datasets

## 1. TACO

**TACO — Trash Annotations in Context**

Used for:

* Waste detection
* Litter object detection
* Real-world trash-in-context examples

---

## 2. TrashNet

Used for:

* Waste classification
* Initial waste-category experiments
* Supporting waste model development

---

## 3. COCO

Used as a general computer vision dataset for:

* Person detection
* General object detection
* Pretrained detector support

---

## 4. Market-1501

Used for experimentation around:

* Person Re-ID
* Person appearance features
* Tracking identity support

---

## 5. Campus CCTV Dataset

Project-specific videos are required for the strongest part of the system:

```text
Littering
Pickup
Proper disposal
Cleaning activity
Multiple people
Occlusion
Different camera angles
Different lighting
Different distances
```

These clips should be manually annotated for event understanding.

---

## 6. Registered People Dataset

The project contains:

```text
data/registered_people/
```

Each authorized person can have registration images used to create face embeddings.

Example:

```text
registered_people/
├── person_001/
│   ├── front.jpg
│   ├── left.jpg
│   ├── right.jpg
│   └── profile.txt
│
├── person_002/
│   ├── front.jpg
│   ├── left.jpg
│   ├── right.jpg
│   └── profile.txt
```

For a real deployment, this data must be handled with appropriate authorization, consent and security controls.

---

# 🧪 Training Strategy

The project does **not** require every model to be trained from scratch.

Instead:

```text
Pretrained Model
      +
Project-Specific Dataset
      ↓
Fine-Tuning / Adaptation
      ↓
Evaluation
      ↓
Deployment
```

### Example

YOLO:

```text
Pretrained YOLO
      ↓
Campus / waste dataset
      ↓
Fine-tuning
      ↓
waste_best.pt
```

Identity:

```text
Pretrained Face Encoder
      ↓
Registered Person Images
      ↓
Face Embeddings
      ↓
embeddings.npy + labels.json
```

Event AI:

```text
Campus CCTV clips
      ↓
Temporal annotations
      ↓
Littering / pickup / disposal training
      ↓
Event model
```

Hotspot prediction:

```text
Verified historical incidents
      ↓
Feature engineering
      ↓
DBSCAN + XGBoost
      ↓
Hotspot / risk model
```

---

# 🔁 Human Feedback & Retraining

Smart Monitoring AI is designed to support continuous improvement.

```text
AI Prediction
     ↓
Human Review
     ↓
VERIFY / REJECT / CORRECT
     ↓
Feedback Dataset
     ↓
Retraining
     ↓
New Candidate Model
     ↓
Evaluation
     ↓
Deploy only if performance improves
```

### Important

A new CCTV video does **not** automatically train the AI.

Only verified or trusted examples should become training data.

---

# 🗄️ Database

## PostgreSQL + PostGIS

The operational database is designed around:

```text
PostgreSQL
    +
PostGIS
```

### Main tables

```text
cameras
registered_people
incidents
evidence
reviews
feedback
cleanup_actions
hotspot_data
model_versions
```

### Why PostgreSQL?

Used for:

* Structured incident data
* User/registered-person records
* Review decisions
* AI confidence values
* Notification state
* Model versions
* Historical analytics

### Why PostGIS?

Used for:

* Camera coordinates
* Incident locations
* Spatial analysis
* Hotspot clustering
* Geographic visualization

---

# ⚙️ Backend

The backend provides the communication layer between AI processing, database and user interfaces.

### FastAPI

Responsible for:

```text
Camera APIs
Incident APIs
People APIs
Review APIs
Hotspot APIs
Report APIs
```

### WebSocket

Used for real-time events such as:

```text
New incident
AI alert
Human review request
Camera status
Notification
```

### Supporting services

```text
incident_service.py
camera_service.py
identity_service.py
notification_service.py
hotspot_service.py
```

---

# 🖥️ Application Screens

## 👤 Person Screen

The person-facing application provides:

```text
Registration
Profile
My Reports
Notifications
```

The registration process captures authorized face images and prepares the person for identity recognition.

---

# 🧠 Control Room

The **Control Room is the central intelligence and operational interface**.

It contains:

### Command Center

Overall operational state.

### Live Monitor

Live camera feed and AI monitoring.

### Incident Review

Human review of AI-generated cases.

### Evidence Viewer

Frames, clips and supporting AI evidence.

### Person Tracking

Track IDs, movement and identity associations.

### AI Analysis

AI confidence, detections and reasoning.

### Hotspot Analysis

Spatial clustering and predicted risk.

### Historical Analytics

Previous incidents and trends.

### Cleanup Monitor

Cleanup activity and resolution state.

### Activity Log

System and operational events.

### Reports

Incident and analytical reporting.

---

# 🏛️ Authority Screen

The authority application intentionally remains smaller than the Control Room.

It focuses on:

```text
Dashboard
Notifications
Verified Incident Reports
Hotspot Alerts
```

The Control Room handles detailed investigation.

The Authority receives the important outcomes.

---

# 📷 Camera Architecture

The camera can be:

```text
Laptop Webcam
     OR
USB Camera
     OR
CCTV/IP Camera
     OR
Phone Camera
```

Example:

```text
PHONE CAMERA
     ↓
Wi-Fi Video Stream
     ↓
camera/camera_client.py
     ↓
AI Server
     ↓
YOLO
ByteTrack
Identity
Event AI
     ↓
Backend
     ↓
Control Room
```

For local development, a laptop webcam can be opened using:

```python
cv2.VideoCapture(0)
```

A network camera can use:

```python
cv2.VideoCapture(CAMERA_URL)
```

---

# 🛠️ Technology Stack

## AI / Computer Vision

* Python
* OpenCV
* YOLOv8
* ByteTrack
* MediaPipe
* OSNet / Re-ID
* Face Embeddings
* XGBoost
* DBSCAN
* NumPy

## Backend

* FastAPI
* WebSocket
* PostgreSQL
* PostGIS
* Redis
* Celery
* MinIO / object storage

## Interfaces

* Streamlit-based application screens
* Lightweight person interface
* Central Control Room
* Authority interface

## Development

* Jupyter Notebook
* Git
* GitHub
* Python virtual environment

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
cd Smart-Monitoring-AI
```

Replace the repository URL with the actual GitHub repository.

---

# 🐍 2. Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📥 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# 🔐 4. Configure Environment Variables

Copy:

```text
.env.example
```

to:

```text
.env
```

Then configure values such as:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/smart_monitoring
AI_SERVER_URL=http://127.0.0.1:8000
CAMERA_URL=0
IDENTITY_THRESHOLD=0.60
EVENT_THRESHOLD=0.60
```

Do **not** commit `.env` to GitHub.

---

# 🗄️ 5. Configure PostgreSQL

Create a database:

```sql
CREATE DATABASE smart_monitoring;
```

If PostGIS is available:

```sql
CREATE EXTENSION postgis;
```

Then apply:

```bash
psql -U <username> -d smart_monitoring -f database/schema.sql
```

Optional sample data:

```bash
psql -U <username> -d smart_monitoring -f database/seed_data.sql
```

---

# 🤖 6. Prepare AI Models

Model files belong under:

```text
models/
```

Example:

```text
models/
├── detection/
├── tracking/
├── identity/
├── event/
└── hotspot/
```

Large model files such as:

```text
*.pt
*.pth
*.onnx
```

should generally not be committed directly to a normal Git repository.

Download or train the required models and place them in their expected directories.

---

# ▶️ Running the Project

## Start the FastAPI Backend

Recommended command:

```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's development documentation can be available through its generated API docs depending on project configuration.

---

# 📷 Start Camera Processing

```bash
python camera/camera_client.py
```

For development, the camera can initially be the laptop webcam.

Later, replace the camera source with a phone/CCTV/IP stream.

---

# 👤 Start Person Screen

```bash
streamlit run screens/person/app.py
```

---

# 🧠 Start Control Room

```bash
streamlit run screens/control_room/app.py
```

---

# 🏛️ Start Authority Screen

```bash
streamlit run screens/authority/app.py
```

---

# 🌐 Multi-Device Local Network Setup

To allow another device on the same Wi-Fi network to access a Streamlit screen:

```bash
streamlit run screens/control_room/app.py --server.address 0.0.0.0
```

Find the AI server/laptop's local IP.

Windows:

```powershell
ipconfig
```

Example:

```text
IPv4 Address: 192.168.1.10
```

Another device on the same Wi-Fi can then access:

```text
http://192.168.1.10:8501
```

The same concept can be used for the person and authority screens.

---

# 🔄 Complete Runtime Flow

```text
                         CAMERA
                           │
                           ▼
                  ┌─────────────────┐
                  │ YOLO Detection  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   ByteTrack     │
                  │   Track IDs     │
                  └────────┬────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       Identity AI                 Event AI
              │                         │
              ▼                         ▼
     Registered Person          Littering Candidate
              │                         │
              └────────────┬────────────┘
                           ▼
                  Decision Engine
                           │
                  ┌────────┴────────┐
                  │                 │
                ≥60%              <60%
                  │                 │
                  ▼                 ▼
          Person Notification   Control Room
                  │                 │
             ┌────┴────┐            │
             │         │            │
            YES        NO            │
             │         │            │
             │         └────────────┤
             │                      ▼
             │                Human Review
             │                 ┌────┴────┐
             │                 │         │
             │               REJECT    VERIFY
             │                 │         │
             │                 │         ▼
             │                 │    Incident DB
             │                 │         │
             │                 │    ┌────┴────┐
             │                 │    ▼         ▼
             │                 │ Person    Authority
             │                 │ Notify      Alert
             │                 │
             └─────────────────┘
                           │
                           ▼
                  Historical Incidents
                           │
                           ▼
                 DBSCAN + XGBoost
                           │
                           ▼
                Hotspot / Risk Analysis
                           │
                           ▼
                    Human Feedback
                           │
                           ▼
                    Model Improvement
```

---

# 📈 Evaluation

The project should evaluate each AI layer independently.

## Detection

* Precision
* Recall
* mAP
* FPS
* Inference latency

## Tracking

* Track continuity
* ID switches
* Track consistency

## Identity Recognition

* Top-1 accuracy
* False match rate
* False non-match rate
* Unknown rejection
* Recognition latency

## Littering Event Detection

* Precision
* Recall
* F1-score
* False alarm rate
* Temporal accuracy

## Decision Engine

* Verified precision
* Human review rate
* Dispute rate
* Rejection rate
* Escalation accuracy

## Hotspot Prediction

* Cluster quality
* Prediction precision/recall
* Risk prediction performance

---

# 🔒 Privacy & Security

Smart Monitoring AI includes identity recognition, therefore privacy must be treated as a first-class concern.

Recommended practices:

* Use only authorized/consented registered-person data.
* Do not upload private face images to public repositories.
* Store embeddings securely.
* Protect the database.
* Do not commit `.env` files.
* Do not commit raw CCTV footage.
* Do not commit private registration images.
* Do not expose administrative APIs publicly.
* Maintain model/version logs.
* Keep human verification in the decision loop.

The repository should follow GitHub's general security guidance and keep sensitive data out of source control.

---

# 🚫 What Should NOT Be Committed

The `.gitignore` should exclude files such as:

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
.env
.ipynb_checkpoints/

data/raw/
data/external/
data/processed/
data/registered_people/

outputs/
incidents/

*.mp4
*.avi
*.mov
*.mkv

*.pt
*.pth
*.onnx
```

Private identity information and large datasets should remain outside the public repository.

---

# 🧪 Development Notebooks

The project contains notebooks documenting the AI development process:

```text
01_dataset_exploration
02_dataset_preparation
03_waste_detection_training
04_person_detection_testing
05_tracking_experiments
06_identity_registration
07_face_recognition_testing
08_littering_event_training
09_pickup_disposal_analysis
10_model_evaluation
11_human_feedback_analysis
12_retraining
13_hotspot_prediction
```

These notebooks are primarily for:

* Experiments
* Dataset analysis
* Model training
* Evaluation
* Visualization
* Research
* Retraining

They are **not required for normal runtime inference** once trained models are available.

---

# 🧩 Model vs Dataset

A dataset is not the trained AI model.

The relationship is:

```text
Dataset
   ↓
Annotation
   ↓
Training
   ↓
Learned Parameters
   ↓
Model Weights
   ↓
Inference
```

For example:

```text
TACO / Campus Waste Dataset
          ↓
       Training
          ↓
     waste_best.pt
          ↓
       YOLOv8
          ↓
     Live Detection
```

---

# 🏁 Development Roadmap

### Phase 1 — Camera

* [x] OpenCV setup
* [ ] Laptop webcam
* [ ] Phone camera
* [ ] CCTV/IP camera

### Phase 2 — Perception

* [ ] Person detection
* [ ] Waste detection
* [ ] Bin detection

### Phase 3 — Tracking

* [ ] ByteTrack
* [ ] Track IDs
* [ ] Multi-person tracking
* [ ] Re-ID support

### Phase 4 — Identity

* [ ] Person registration
* [ ] Face embeddings
* [ ] Identity matching
* [ ] Unknown rejection
* [ ] Track ID ↔ identity

### Phase 5 — Event Intelligence

* [ ] Hold detection
* [ ] Release detection
* [ ] Waste landing detection
* [ ] Person departure
* [ ] Pickup detection
* [ ] Proper disposal detection

### Phase 6 — Decision Engine

* [ ] Identity confidence
* [ ] Event confidence
* [ ] 60% routing threshold
* [ ] Preliminary person notification
* [ ] Person dispute / NO
* [ ] Control Room review
* [ ] Human verification

### Phase 7 — Evidence

* [ ] Evidence package
* [ ] Relevant frames
* [ ] Short event clip
* [ ] AI reasoning
* [ ] Confidence records

### Phase 8 — Analytics

* [ ] Historical incident analytics
* [ ] DBSCAN hotspot detection
* [ ] XGBoost risk prediction
* [ ] Hotspot visualization

### Phase 9 — Learning Loop

* [ ] Human feedback
* [ ] Corrected examples
* [ ] Retraining
* [ ] Model evaluation
* [ ] Model versioning

---

# 🧑‍💻 Contributing

Contributions are welcome.

Typical workflow:

```bash
git clone <repository-url>
cd Smart-Monitoring-AI

git checkout -b feature/my-feature

# Make changes

git add .
git commit -m "Add my feature"

git push origin feature/my-feature
```

Then open a pull request.

Keep AI logic separated from UI logic whenever possible.

For example:

```text
src/
    AI logic

screens/
    UI

backend/
    API + services

models/
    trained models

data/
    datasets

notebooks/
    experiments
```

This separation makes the project easier to test, maintain and extend.

---

# 🧭 Design Principles

Smart Monitoring AI follows several important principles.

### 1. AI First

The primary value of the system comes from computer vision and machine learning rather than from the interface.

### 2. Identity ≠ Guilt

Recognizing a person does not prove that the person littered.

### 3. Temporal Understanding

The system should understand a sequence of actions rather than make decisions from a single frame.

### 4. Confidence-Aware AI

The system should know when it is uncertain.

### 5. Human-in-the-Loop

Disputed or uncertain incidents go to the Control Room.

### 6. Evidence-Based Decisions

Every incident should have supporting evidence.

### 7. Continuous Improvement

Verified human feedback can become training data.

### 8. Modular Architecture

Each AI component can be improved independently.

---

# 🏆 What Makes This Project Different?

A basic litter detection project might do:

```text
Camera → YOLO → Garbage Detected
```

Smart Monitoring AI aims to do:

```text
Camera
  ↓
Detect
  ↓
Track
  ↓
Recognize
  ↓
Understand interaction
  ↓
Reconstruct event
  ↓
Calculate confidence
  ↓
Generate evidence
  ↓
Make a decision
  ↓
Notify the correct person
  ↓
Allow dispute
  ↓
Human verification
  ↓
Authority escalation
  ↓
Historical analysis
  ↓
Predict hotspots
  ↓
Learn from feedback
```

The goal is therefore not simply **object detection**.

It is an **AI-assisted event understanding and decision-support system**.

---

# 📌 Current Prototype Architecture

```text
                   SMART MONITORING AI

                         CAMERA
                           │
                           ▼
                    AI PROCESSING
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
    Detection          Identity            Event AI
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                    Decision Engine
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       Person Notification       Control Room
                                        │
                                        ▼
                                  Human Review
                                        │
                              ┌─────────┴─────────┐
                              ▼                   ▼
                           Reject              Verify
                                                  │
                                      ┌───────────┴──────────┐
                                      ▼                      ▼
                                  Person                 Authority
                                 Notification              Alert
                                      │
                                      ▼
                              Historical Database
                                      │
                                      ▼
                            Hotspot / Risk AI
```

---

# 📜 Project Status

> **Development Status: Active AI Prototype**

The project architecture, application screens, camera layer, AI module structure, datasets, model organization, backend design, database design and human-review workflow are defined.

The major remaining implementation work is connecting the individual AI modules into the complete real-time pipeline.

---

# ⚠️ Important Disclaimer

Smart Monitoring AI is a **college/research prototype**.

AI predictions and confidence scores should not be treated as unquestionable proof of wrongdoing.

The system is designed around:

```text
AI Prediction
      +
Evidence
      +
Confidence
      +
Human Review
```

rather than automated punishment.

Before real-world deployment, the system would require appropriate privacy, consent, security, legal, governance and accuracy evaluation.

---

# 📄 License

Add the project's chosen license here before publishing the repository publicly.

Example:

```text
MIT License
```

or another license appropriate for the project.

---

# ⭐ Final Project Vision

> **From passive CCTV to intelligent environmental monitoring.**

Smart Monitoring AI aims to combine:

**Computer Vision + Identity Recognition + Tracking + Temporal AI + Explainable Evidence + Human Review + Predictive Analytics**

to create an intelligent monitoring platform capable of understanding environmental incidents rather than simply detecting objects.

---

## 👥 Built For

**Academic / Research / Smart Campus / Smart City Demonstration**

### Core Domains

`Computer Vision` · `Deep Learning` · `Artificial Intelligence` · `Multi-Object Tracking` · `Face Recognition` · `Temporal Event Detection` · `Predictive Analytics` · `Human-in-the-Loop AI`

---

### 🔗 Repository Setup

After creating the repository, replace:

```text
https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>
```

with the actual GitHub repository URL throughout this README.

GitHub recommends keeping the README at the repository root and using relative links where possible so documentation remains useful when the repository is cloned.
