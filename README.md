# AI-Based Intelligent Traffic Management System

An AI-powered Intelligent Traffic Management System developed as a Artificial Intelligence and Machine Learning project. The system combines Artificial Intelligence, Computer Vision, Traffic Simulation, and a Digital Twin environment to optimize traffic signal timings based on real-time vehicle density.

The project utilizes SUMO for traffic simulation, Unity 3D as the digital twin, YOLOv8 for vehicle detection, Python for backend processing, Streamlit for dashboard visualization, and TraCI for communication between SUMO and Python.

---

# Features

## Implemented

- AI-Based Adaptive Traffic Signal Control
- SUMO Traffic Simulation
- Unity 3D Digital Twin
- Four Virtual CCTV Cameras
- Live Vehicle Detection using YOLOv8
- Lane-wise Vehicle Counting
- Adaptive Traffic Signal Timing
- Minimum and Maximum Green Time Control
- Unity-SUMO Synchronization
- Python-TraCI Communication
- Streamlit Live Dashboard
- Real-Time JSON Data Exchange
- Git & GitHub Version Control

## Currently Under Development

- Region of Interest (ROI) Based Lane Detection
- Red Light Violation Detection
- Automatic Number Plate Recognition (ANPR)
- Vehicle Database Integration
- Insurance Verification
- Pollution Certificate Verification
- Automatic Fine Generation
- Traffic Analytics and Reports

---

# Current Project Status

## Completed

- SUMO Traffic Simulation
- Unity Digital Twin
- Python Bridge
- Adaptive AI Controller
- YOLO Vehicle Detection
- Four Virtual CCTV Cameras
- Lane-wise Vehicle Counting
- Live Dashboard
- GitHub Repository

Current Progress: Approximately 90%

---

# Technologies Used

- Python 3.12
- C#
- SUMO 1.25.0
- Unity 6
- YOLOv8
- OpenCV
- PyTorch CUDA
- Streamlit
- SQLite
- TraCI
- JSON
- Git
- GitHub

---

# Hardware Requirements

## Minimum

- Windows 10/11 (64-bit)
- Intel Core i5 10th Gen / AMD Ryzen 5
- 16 GB RAM
- NVIDIA GTX 1650 (4 GB VRAM)
- 20 GB SSD Storage

## Recommended

- Windows 11 (64-bit)
- AMD Ryzen 7 7840HS / Intel Core i7
- 32 GB DDR5 RAM
- NVIDIA RTX 3050 (6 GB VRAM) or Higher
- NVMe SSD
- Full HD Display

---

# Software Requirements

- Microsoft Windows 11
- Python 3.12
- Unity Hub
- Unity 6 (6000.0.5f1)
- SUMO 1.25.0
- Git
- Visual Studio Code
- NVIDIA Graphics Driver
- CUDA Enabled PyTorch

---

# Python Libraries

Install the required libraries:

```bash
pip install ultralytics torch torchvision opencv-python numpy pillow streamlit
```

Built-in Modules Used:

- os
- json
- shutil
- sqlite3
- time

---

# Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/termux37/AI-Traffic-System.git
```

---

## 2. Enter Project Directory

```bash
cd AI-Traffic-System
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install ultralytics torch torchvision opencv-python numpy pillow streamlit
```

---

## 5. Install SUMO

Install SUMO Version 1.25.0 and ensure SUMO is added to the system PATH.

---

## 6. Install Unity

Install Unity Hub and Unity 6 Editor.

Open the Unity project located inside the repository.

---

## 7. Download YOLO Model

The project uses

```
yolov8n.pt
```

It will automatically download during the first execution if it is not already available.

---

# Running the Project

## Step 1

Open the Unity Project.

Press Play.

---

## Step 2

Run the AI Vision System

```bash
python backend/vision_ai.py
```

---

## Step 3

Run the Unity Bridge

```bash
python backend/unity_bridge.py
```

---

## Step 4

Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Step 5

Observe

- SUMO Simulation
- Unity Digital Twin
- Live CCTV Cameras
- Vehicle Detection
- AI Traffic Signal Control
- Dashboard

---

# Project Architecture

```
Unity CCTV Cameras
          │
          ▼
YOLOv8 Vehicle Detection
          │
          ▼
Lane-wise Vehicle Counting
          │
          ▼
Adaptive AI Traffic Controller
          │
          ▼
SUMO Traffic Simulation
          │
          ▼
Unity Digital Twin
          │
          ▼
Streamlit Dashboard
```

---

# Adaptive AI Algorithm

1. Capture images from four virtual CCTV cameras.

2. Detect vehicles using YOLOv8.

3. Count vehicles in each lane.

4. Calculate traffic density for:

- North + South
- East + West

5. Apply Adaptive Signal Control:

- Maintain Minimum Green Time.
- Prevent frequent switching.
- Switch signals based on traffic density.
- Enforce Maximum Green Time.

6. Update traffic lights in SUMO.

7. Synchronize Unity.

8. Update Dashboard.

9. Repeat continuously.

---

# Project Directory

```
AI-Traffic-System/

backend/
    vision_ai.py
    unity_bridge.py
    ai_controller.py

dashboard/
    app.py

sumo/

unity/

camera_feed/

vision_input/

detections/

data/

README.md
```

---

# Future Improvements

- ROI-Based Vehicle Detection
- Automatic Number Plate Recognition
- Vehicle Registration Database
- Insurance Verification
- Pollution Certificate Verification
- Automatic Challan/Fine Generation
- Emergency Vehicle Priority
- Cloud Dashboard
- Real CCTV Integration
- Multi-Junction Traffic Management

---

# Author

**Nithin John Regi**

---

## License

Copyright © 2026 Nithin John Regi

All Rights Reserved.

This repository is provided for viewing and academic demonstration purposes only.

No permission is granted to copy, modify, distribute, or reuse the source code without prior written permission from the author.