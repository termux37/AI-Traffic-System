# AI-Based Intelligent Traffic Management System

> **Research & Development Project**
>
> An AI-powered intelligent traffic management system utilizing Computer Vision, Digital Twin technology, and Adaptive Traffic Signal Control for smart city applications.

The AI-Based Intelligent Traffic Management System is designed to optimize traffic flow by integrating Artificial Intelligence, Computer Vision, Traffic Simulation, and Digital Twin technology. The system dynamically adjusts traffic signal timings based on real-time vehicle density, improving traffic efficiency while reducing congestion.

The project utilizes SUMO for traffic simulation, Unity 3D as the Digital Twin environment, YOLOv8 for real-time vehicle detection, Python for backend processing, Streamlit for dashboard visualization, and TraCI for communication between the simulation and the AI controller.

> **Notice**
>
> This repository is published solely for academic demonstration and portfolio purposes.
>
> The source code, algorithms, software architecture, documentation, models, and associated files are protected under an **All Rights Reserved** license.
>
> No permission is granted to copy, reproduce, modify, distribute, compile, execute, or use this software, in whole or in part, without prior written permission from the author.

---

# Project Overview

This project demonstrates the implementation of an intelligent traffic management system capable of:

- Detecting vehicles using Artificial Intelligence
- Estimating traffic density in real time
- Dynamically controlling traffic signals
- Simulating a smart city intersection
- Visualizing traffic flow using a Digital Twin
- Displaying live traffic information through a dashboard

---

# Features

## Implemented

- AI-Based Adaptive Traffic Signal Control
- SUMO Traffic Simulation
- Unity 3D Digital Twin
- Four Virtual CCTV Cameras
- Real-Time Vehicle Detection using YOLOv8
- Lane-wise Vehicle Counting
- Adaptive Traffic Signal Timing
- Minimum and Maximum Green Time Control
- Unity-SUMO Synchronization
- Python-TraCI Communication
- Streamlit Dashboard
- Live Traffic Monitoring
- JSON-based Data Exchange
- Git Version Control
- GitHub Repository

---

# Current Project Status

## Completed Modules

- Traffic Simulation Environment
- Unity Digital Twin
- Python-SUMO Communication
- Adaptive AI Controller
- YOLO Vehicle Detection
- Four Virtual CCTV Cameras
- Lane-wise Vehicle Counting
- Live Dashboard
- GitHub Repository

## Development Status

✔ Functional Prototype Completed

✔ Adaptive AI Signal Controller Implemented

✔ Active Development Continues

---

# Technologies Used

## Programming Languages

- Python
- C#

## Artificial Intelligence

- YOLOv8
- PyTorch
- OpenCV

## Simulation

- SUMO
- TraCI

## Visualization

- Unity 3D
- Streamlit

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# Hardware Requirements

## Minimum

- Windows 10/11 (64-bit)
- Intel Core i5 (10th Generation) or AMD Ryzen 5
- 16 GB RAM
- NVIDIA GTX 1650 (4 GB VRAM)
- SSD Storage

## Recommended

- Windows 11 (64-bit)
- AMD Ryzen 7 / Intel Core i7
- 32 GB DDR5 RAM
- NVIDIA RTX 3050 (6 GB VRAM) or Higher
- NVMe SSD
- Full HD Display

---

# Software Used

- Microsoft Windows 11
- Python 3.12
- Unity 6
- SUMO 1.25.0
- Visual Studio Code
- Git
- GitHub
- CUDA Enabled PyTorch

---

# System Architecture

```
Virtual CCTV Cameras
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
Live Dashboard
```

---

# Adaptive AI Algorithm

1. Capture images from four virtual CCTV cameras.

2. Detect vehicles using YOLOv8.

3. Count vehicles present in each lane.

4. Calculate traffic density for:
   - North–South Direction
   - East–West Direction

5. Apply Adaptive Traffic Signal Logic:
   - Maintain minimum green time.
   - Prevent unnecessary signal switching.
   - Compare traffic density.
   - Switch signals only when required.
   - Enforce maximum green time to avoid starvation.

6. Update traffic signals in SUMO.

7. Synchronize signal state with Unity.

8. Update dashboard with live information.

9. Repeat continuously.

---

# Project Modules

- AI Traffic Signal Controller
- Vehicle Detection Module
- Unity Digital Twin
- SUMO Traffic Simulator
- Dashboard Module
- Data Communication Module
- Traffic Analytics Module

---

# Future Scope

- Region of Interest (ROI) Based Lane Detection
- Automatic Number Plate Recognition (ANPR)
- Traffic Violation Detection
- Automatic Fine Generation
- Vehicle Registration Database
- Insurance Verification
- Pollution Certificate Verification
- Emergency Vehicle Priority
- Cloud-Based Monitoring
- Multi-Intersection Traffic Management
- Smart City Integration

---

# Author

**Nithin John Regi**

Bachelor of Technology (B.Tech)

Robotics and Automation Engineer

Artificial Intelligence | Machine Learning | Computer Vision | Robotics | Autonomous Systems

GitHub: https://github.com/termux37

---

# License

Copyright © 2026 Nithin John Regi

**All Rights Reserved.**

This repository is published exclusively for academic evaluation, research demonstration, and portfolio purposes.

The source code, software architecture, algorithms, documentation, images, models, datasets, and all associated files remain the intellectual property of the author.

Without prior written permission from the copyright holder, **no individual or organization is permitted to:**

- Copy or reproduce this project
- Modify the source code
- Redistribute any part of this repository
- Publish this project elsewhere
- Create derivative works
- Use the implementation commercially
- Re-upload or mirror this repository
- Use any portion of the code in another project

Unauthorized use, reproduction, modification, or distribution may constitute copyright infringement and may result in legal action.

For licensing, collaboration, or permission requests, please contact the author.

---

**© 2026 Nithin John Regi. All Rights Reserved.**