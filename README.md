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


### Installation

Install the required dependencies using the following command:
```bash
pip install opencv-python pytesseract torch ultralytics
```



### How to Run

#### Step 1: Download Models
1. Download the YOLOv5 and YOLOv8 model weights (pre-trained or custom).
2. Extract the `.zip` files into the project root directory.

#### Step 2: Prepare Files & Folders
1. Place your input video (e.g., `video.mov`) in the root directory.
2. Ensure the folder structure aligns with the example provided in this repository.

#### Step 3: Extract Vehicles from Video
Run the vehicle detection script to identify and crop vehicle images from the video:
```bash
python vehicle_detection.py
```












This script saves cropped vehicle images for further processing.

#### Step 4: Prepare Dataset for Training
1. Place the `data.yaml` configuration file in the root directory.
2. Organize annotated images for training. **Note**: The model used in this project was trained with over 7,000 license plate samples. A large dataset is critical for effective machine learning model training to ensure high accuracy and generalizability.
3. For optimal performance, use larger models and a GPU during training.

#### Step 5: Train the YOLOv8 Model
Initiate training of the YOLOv8 model with the following command:
```bash
python train_model.py
```
Upon completion, the training process generates model weights in a folder such as `runs/detect/train6/weights/best.pt`.

#### Step 6: Run License Plate Detection and OCR
Execute the detection and OCR script to process the cropped images:
```bash
python license_plate_recognition.py
```
This script automatically generates:
- `tabela_comparativa.html`: A comparative table of detection results.
- `lista_de_chapas_de_matricula.txt`: A list of detected license plates.
- JSON files in the `output_txts/` directory containing detailed detection information.

#### Step 7: Fallback Option
If the detection and OCR script fails, use the alternative script to process existing detection data:
```bash
python independent.py
```
This generates the same outputs as Step 6 using previously saved detection data.

### Notes
- The machine learning models used in this project were **pre-trained** on a large dataset, emphasizing the importance of extensive training data. For custom training, ensure a dataset with thousands of annotated images (e.g., over 7,000 license plate samples) to achieve comparable performance.
- Training on a GPU significantly improves efficiency, especially for larger models.
- Refer to the repository’s example folder structure to avoid configuration errors.
