
import streamlit as st
import cv2
import tempfile
import os
from detection_engine import procesar_deteccion 

st.title("Sistema de Seguridad para Caracas")
st.subheader("Análisis de riesgos mediante video")

# Opción para subir archivo de video
archivo_subido = st.file_uploader("Sube un video para analizar", type=["mp4", "mov", "avi"])

if archivo_subido is not None:
    # Guardar el video temporalmente para procesarlo
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(archivo_subido.read())
    
    cap = cv2.VideoCapture(tfile.name)
    st.write("Analizando video...")
    
    # Contenedor para mostrar el video procesado
    frame_placeholder = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Llamada a tu motor de detección
        frame_procesado = procesar_deteccion(frame)
        
        # Convertir BGR (OpenCV) a RGB (Streamlit)
        frame_rgb = cv2.cvtColor(frame_procesado, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB")
        
    cap.release()
    os.unlink(tfile.name) # Borrar archivo temporal
    st.success("Análisis completado")
