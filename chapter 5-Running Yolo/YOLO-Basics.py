from  ultralytics import YOLO
import cv2
model=YOLO('../Yolo weights/yolov8l.pt')
results=model("Images/1592917468-YolobusTeam-Pic1.jpg",show=True)
cv2.waitKey((0))