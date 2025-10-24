# Car-Counter

#  Vehicle Detection and Counting using YOLOv8 + SORT

This project is a **real-time vehicle detection and counting system** that uses **YOLOv8 (You Only Look Once)** for object detection and **SORT (Simple Online and Realtime Tracking)** for tracking objects across frames.  
It detects and counts vehicles such as **cars, trucks, buses, and motorbikes** passing through a specified region in a video.

---

## 📸 Demo

The system processes a video feed (e.g., traffic footage), detects vehicles, tracks their movement, and counts how many cross a predefined line.

![Demo Image](mask.png)


##  Features

-  Detects multiple vehicle types (car, truck, bus, motorbike)
-  Real-time tracking using **Kalman Filter + SORT**
-  Counts vehicles crossing a specific line
-  Uses **YOLOv8n** model for efficient inference
-  Region masking to detect only in areas of interest

---

#  Project Structure

├── Car-Counter.py # Main script for detection, tracking & counting
├── sort.py # SORT tracking algorithm implementation
├── mask.png # Region mask (defines area of interest)
├── Videos/ # (Add your input videos here)
│ └── cars.mp4
└── Yolo weights/
└── yolov8n.pt # YOLOv8 pretrained weights


---

## ⚙️ Requirements

Install dependencies using pip:


pip install ultralytics opencv-python cvzone filterpy matplotlib scikit-image
How to Run
Clone this repository:
git clone https://github.com/<your-username>/Car-Counter.git
cd Car-Counter
Add your YOLOv8 model weights (yolov8n.pt) inside a folder named Yolo weights.

Place your input video (e.g., cars.mp4) inside the Videos/ folder.

Run the main script:

bash
Copy code
python Car-Counter.py
Code Overview
Car-Counter.py
Loads the YOLO model.

Reads the mask image (mask.png).

Performs detection on the region of interest.

Tracks detected objects using SORT.

Counts vehicles that cross the counting line.

sort.py
Implements the SORT algorithm using a Kalman Filter to maintain unique IDs for each detected vehicle across frames.

Key Components
Component	Description
YOLOv8	Detects vehicles in each frame
SORT	Tracks vehicles over time using Kalman filter
mask.png	Restricts detection area
counting line	Defines where vehicles are counted
cvzone	Displays bounding boxes, text overlays, and counts

 Output
A live window showing:

Bounding boxes around detected vehicles

Unique IDs for each vehicle

Total vehicle count displayed on screen

Author
Kodurupaka Bhanu Teja
B.Tech Mechanical Engineering | MGIT Hyderabad
bunnykodurupaka@gmail.com

License
This project includes the SORT algorithm licensed under GPL v3.

Future Improvements
Add speed estimation

Store count data in a CSV file

Integrate with live CCTV feeds

Implement detection for pedestrians or bicycles

If you like this project, consider giving it a star on GitHub!
