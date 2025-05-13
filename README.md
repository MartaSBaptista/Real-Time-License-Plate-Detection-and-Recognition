# Real-Time-License-Plate-Detection-and-Recognition
This project extracts vehicles from video footage and saves them as image files. A trained model then identifies and extracts license plate numbers from the detected vehicles. The system automates vehicle detection and license plate recognition for traffic monitoring, enforcement, and surveillance purposes.

# Vehicle Detection and License Plate Recognition

This project performs vehicle detection and license plate recognition on videos. The system uses the YOLO model for object detection, extracts images of the detected vehicles, and then applies Optical Character Recognition (OCR) to detect license plates.

## Features

- **Vehicle Detection**: The system detects cars, buses, and trucks from a video file using a pre-trained YOLOv5 nano model.
- **Image Extraction**: Detected vehicles are cropped and saved as images in a designated folder (`pasta_carros`).
- **License Plate Recognition**: A custom-trained YOLOv8 model detects license plates from vehicle images, and OCR (via Tesseract) is used to extract the plate text.
- **Output Formats**: 
    - **JSON**: Contains vehicle and license plate detection data.
    - **HTML**: A comparative table of the images and detected license plates.
    - **TXT**: A list of all detected license plates.

## Requirements

- Python 3.x
- `opencv-python` for video and image processing
- `torch` for loading the YOLO model
- `pytesseract` for OCR to detect license plates
- `ultralytics/yolov5` and `ultralytics/yolov8` for vehicle detection and license plate recognition

Install the required dependencies:
```bash
pip install opencv-python pytesseract torch ultralytics




