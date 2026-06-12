import streamlit as st
import cv2
import numpy as np

st.title("Sistema de Seguridad para Caracas")
st.write("Monitoreo en tiempo real y análisis de riesgos.")

run = st.checkbox('Activar Cámara')
FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)
    while run:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
