# DriveMind AI

DriveMind AI is a simulation-based Advanced Driver Assistance System (ADAS) prototype developed using Python, OpenCV, YOLO, and Webots.

The project focuses on integrating real-time computer vision with autonomous vehicle control inside a simulated driving environment. It combines lane perception, steering control, simulation-based testing, and autonomous navigation into a unified ADAS workflow.

---

# Features

## Autonomous Lane Assistance
- Real-time lane detection using OpenCV
- Lane center estimation
- Dynamic steering correction
- Curved road handling
- Steering smoothing and stabilization

## Simulation Environment
- Webots-based autonomous driving simulation
- Physics-enabled vehicle environment
- Curved multi-lane highway loop
- Real-time front camera feed
- Simulation debugging and telemetry

## DriveMind HUD
- Live lane visualization
- Steering angle monitoring
- Vehicle telemetry overlay
- Lane offset display
- Autonomous mode indicators

## Computer Vision Pipeline
- Edge detection
- ROI filtering
- Hough line transformation
- Lane center tracking
- Visual feedback rendering

## Object Detection (In Progress)
- YOLOv8 integration
- Forward Collision Warning (FCW)
- NPC traffic experimentation
- Autonomous traffic interaction

---

# Tech Stack

- Python
- OpenCV
- NumPy
- YOLOv8
- Webots
- Computer Vision
- Autonomous Systems Concepts

---

# System Architecture

```text
Front Camera Feed
        ↓
Image Processing
        ↓
Lane Detection
        ↓
Lane Center Estimation
        ↓
Steering Logic
        ↓
Vehicle Control
        ↓
Webots Simulation
```

The system processes the simulated camera feed in real time, detects lane boundaries, estimates lane center offset, and applies steering corrections to maintain autonomous lane following.

---

# Project Structure

```text
DriveMindAI/
│
├── controllers/
│
├── worlds/
│
├── ui/
│
├── vision/
│
├── assets/
│
├── models/
│
├── yolov8n.pt
│
├── main.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# Installation

## 1. Install Webots

Download and install Webots:

https://cyberbotics.com/

---

## 2. Clone Repository

```bash
git clone https://github.com/yourusername/DriveMindAI.git
cd DriveMindAI
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Launch Simulation

1. Open Webots
2. Load the `.wbt` world file from the `worlds/` directory
3. Start simulation
4. Run the ADAS controller

---

# Current Capabilities

- Autonomous lane following
- Curved road navigation
- Real-time camera perception
- Steering stabilization
- Simulation-based ADAS testing
- HUD-based telemetry visualization

---

# Future Improvements

- NPC traffic system
- Forward Collision Warning (FCW)
- YOLO-based vehicle detection
- Time-to-Collision estimation
- PID steering controller
- Adaptive Cruise Control
- Traffic sign recognition
- Weather and night simulation
- Multi-camera perception

---

# Challenges Faced

This project involved debugging and solving several real-world autonomous driving simulation problems including:

- Steering instability
- Curve handling
- Lane estimation noise
- Vehicle physics behavior
- Simulation coordinate systems
- Camera alignment
- Real-time processing latency
- Road boundary handling

---

# Disclaimer

This project is an experimental simulation prototype intended for educational and research purposes only.

---

# Author

Purnapragya Sinha
