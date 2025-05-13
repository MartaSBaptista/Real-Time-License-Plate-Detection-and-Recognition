import cv2
import torch
import os

# === Carregar modelo YOLOv5nano (super leve) ===
model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)
model.conf = 0.5
model.classes = [2, 5, 7]  # car, bus, truck

# === Criar pasta de saída ===
output_dir = "pasta_carros"
os.makedirs(output_dir, exist_ok=True)

# === Leitura do vídeo ===
cap = cv2.VideoCapture("3.mov")
frame_skip = 10
frame_count = 0
car_count = 1
positions = []

def is_valid_box(x1, y1, x2, y2, img_width, img_height):
    w = x2 - x1
    h = y2 - y1
    aspect = w / h if h > 0 else 0
    area = w * h
    # Restrições para evitar falsos positivos
    if area < 3000 or area > img_width * img_height * 0.3:
        return False
    if aspect < 1.2 or aspect > 4.0:
        return False
    return True

def is_far_enough(new_box, previous_boxes, min_dist=70):
    x1, y1, x2, y2 = new_box
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    for (px, py) in previous_boxes:
        if abs(cx - px) < min_dist and abs(cy - py) < min_dist:
            return False
    previous_boxes.append((cx, cy))
    return True

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    height, width = frame.shape[:2]
    results = model(frame)
    detections = results.xyxy[0]

    for *box, conf, cls in detections:
        x1, y1, x2, y2 = map(int, box)

        if not is_valid_box(x1, y1, x2, y2, width, height):
            continue

        if is_far_enough((x1, y1, x2, y2), positions):
            cropped = frame[int(y1):int(y2), int(x1):int(x2)]
            filename = f"car{car_count}.jpg"
            cv2.imwrite(os.path.join(output_dir, filename), cropped)
            print(f"[{car_count}] Guardado {filename}")
            car_count += 1

cap.release()
