import streamlit as st
import cv2
import tempfile
import os
from detection_engine import detect_threats

st.title("Sistema de Seguridad para Caracas")

archivo_subido = st.file_uploader("Sube un video", type=["mp4", "mov", "avi"])

if archivo_subido is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(archivo_subido.read())
    
    cap = cv2.VideoCapture(tfile.name)
    frame_placeholder = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = detect_threats(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")
        
    cap.release()
    os.unlink(tfile.name)
