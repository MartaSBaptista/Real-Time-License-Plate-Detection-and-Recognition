from ultralytics import YOLO

# Caminho para o arquivo data.yaml
model = YOLO("yolov8n.pt")  # ou yolov8s.pt para melhor precisão
model.train(data="data.yaml", epochs=30, imgsz=640)
