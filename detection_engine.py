from ultralytics import YOLO
import cv2
import numpy as np

# Cargamos el modelo pre-entrenado de detección
model = YOLO('yolov8n.pt') 

def detect_threats(frame):
    # Procesamos la imagen con el modelo
    results = model(frame, conf=0.5) 
    
    # Dibujamos las detecciones
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Obtenemos las coordenadas
            b = box.xyxy[0].to('cpu').detach().numpy().astype(int)
            # Detectamos si es una persona (clase 0 en YOLO)
            cls = int(box.cls[0])
            if cls == 0:
                cv2.rectangle(frame, (b[0], b[1]), (b[2], b[3]), (0, 255, 0), 2)
                cv2.putText(frame, "Persona Detectada", (b[0], b[1]-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
  
