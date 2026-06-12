import streamlit as st
import cv2
import tempfile
import os
from detection_engine import detect_threats

st.title("Sistema de Seguridad para Caracas")
st.subheader("Análisis de Inteligencia Artificial")

archivo_subido = st.file_uploader("Sube un video para analizar", type=["mp4", "mov", "avi"])

if archivo_subido is not None:
    # Gestión del archivo temporal
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(archivo_subido.read())
    
    cap = cv2.VideoCapture(tfile.name)
    st.write("Procesando video con IA...")
    
    frame_placeholder = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Llamamos a nuestro motor de detección actualizado
        frame = detect_threats(frame)
        
        # Convertimos a RGB para mostrar en Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB")
        
    cap.release()
    os.unlink(tfile.name)
    st.success("Análisis completado")
  
