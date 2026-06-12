
import streamlit as st
import cv2
import tempfile
import os
# Importamos la función detect_threats tal cual se llama en el otro archivo
from detection_engine import detect_threats

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
            
        # Llamada a tu motor de detección usando el nombre correcto
        resultado = detect_threats(frame)
        
        # Por ahora, solo mostramos el video original 
        # mientras terminamos la lógica de detección
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB")
        
    cap.release()
    os.unlink(tfile.name) # Borrar archivo temporal
    st.success("Análisis completado")
