import os
import cv2
import pytesseract
import json
import uuid
from ultralytics import YOLO

# Caminhos
model_path = "runs/detect/train6/weights/best.pt"
image_folder = "pasta_carros"
output_folder = "output_txts"

# Criação de pastas
os.makedirs(output_folder, exist_ok=True)

# Lista de imagens
image_files = [f"car{i}.jpg" for i in range(1, 13)]

# Carregar modelo YOLO
model = YOLO(model_path)

# Matrículas detetadas para HTML
dados_para_html = []

# Loop pelas imagens
for image_name in image_files:
    img_path = os.path.join(image_folder, image_name)
    txt_path = os.path.join(output_folder, image_name.replace(".jpg", ".txt"))

    if not os.path.exists(img_path):
        print(f"Imagem não encontrada: {img_path}")
        continue

    image = cv2.imread(img_path)
    height, width = image.shape[:2]
    results = model.predict(image, conf=0.4)

    license_plate_text = [[]]
    license_plates = [[]]
    car_predictions = []
    placa_detectada = "Não Detetada"

    if results and results[0].boxes.data.numel():
        for box, conf, cls in zip(results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls):
            x1, y1, x2, y2 = map(int, box.tolist())
            w = x2 - x1
            h = y2 - y1
            cx = x1 + w / 2
            cy = y1 + h / 2
            class_id = int(cls)
            class_name = model.names[class_id] if class_id in model.names else "object"

            car_predictions.append({
                "width": w,
                "height": h,
                "x": cx,
                "y": cy,
                "confidence": float(conf),
                "class_id": class_id,
                "class": class_name,
                "detection_id": str(uuid.uuid4()),
                "parent_id": "image"
            })

            # OCR apenas na primeira deteção de "car"
            if class_name == "car" and license_plate_text == [[]]:
                plate_crop = image[y1:y2, x1:x2]
                text = pytesseract.image_to_string(plate_crop, config='--psm 7').strip()
                if text:
                    placa_detectada = text
                    license_plate_text = [[text]]
                    license_plates = [[[x1, y1, x2, y2]]]

    # JSON com estrutura esperada
    output_json = [
        {
            "license_plates": license_plates,
            "license_plate_text": license_plate_text,
            "cars": [
                {
                    "car_model_predictions": {
                        "image": {
                            "width": width,
                            "height": height
                        },
                        "predictions": car_predictions
                    }
                }
            ]
        }
    ]

    # Guardar ficheiro JSON
    with open(txt_path, "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)

    print(f"{image_name}: Guardado em {txt_path}")

    # Adicionar à tabela HTML
    dados_para_html.append((img_path, placa_detectada))

# Criar HTML com os resultados
with open("tabela_comparativa.html", "w", encoding="utf-8") as html_file:
    html_file.write("<html><head><title>Tabela Comparativa</title></head><body>\n")
    html_file.write("<h1>Resultados de Deteção e OCR</h1>\n")
    html_file.write("<table border='1' style='border-collapse: collapse;'>\n")
    html_file.write("<tr><th>Imagem</th><th>Matrícula Detetada</th></tr>\n")

    for caminho, placa in dados_para_html:
        caminho_relativo = caminho.replace("\\", "/")  # Para funcionar bem no HTML
        html_file.write(f"<tr><td><img src='{caminho_relativo}' width='300'></td><td>{placa}</td></tr>\n")

    html_file.write("</table></body></html>")

# Guardar todas as matrículas detetadas num .txt
with open("lista_de_chapas_de_matricula.txt", "w", encoding="utf-8") as f:
    for _, placa in dados_para_html:
        f.write(placa + "\n")


