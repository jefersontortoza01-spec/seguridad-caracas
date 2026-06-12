import streamlit as st
import cv2
import tempfile
import os
from detection_engine import detect_threats # <-- ¡ESTO DEBE COINCIDIR EXACTAMENTE!

# Y más abajo, cuando usas la función, debe ser:
# resultado = detect_threats(frame)

