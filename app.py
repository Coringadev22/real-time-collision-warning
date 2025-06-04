import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile

# 🎨 Estilo da página
st.set_page_config(page_title="Alerta de Colisão com IA", layout="wide", page_icon="🚗")
st.markdown("""
    <style>
        .main { background-color: #f4f6fa; }
        .big-alert {
            font-size:28px;
            font-weight:bold;
            color:red;
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Título
st.markdown("<h1 style='text-align: center;'>🚗 Sistema de Prevenção de Colisão com YOLOv8</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Detecção em tempo real com alertas visuais baseados em bounding boxes</h4>", unsafe_allow_html=True)
st.markdown("---")

# 📘 Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/car-crash.png", width=100)
    st.subheader("ℹ️ Sobre o projeto")
    st.write("""
    - Detecta veículos e pedestres
    - Estima proximidade visual
    - Gera alerta quando risco de colisão é detectado
    """)
    
    # NOVO: controle de sensibilidade
    area_threshold = st.slider("📏 Sensibilidade do Alerta (área mínima)", 
                               min_value=50000, 
                               max_value=300000, 
                               step=10000, 
                               value=150000,
                               help="Quanto maior o valor, menos sensível será o alerta.")

    st.caption("👨‍💻 Desenvolvido por Lucas Coelho · IntelTech 🤖")

# 📤 Upload
uploaded_video = st.file_uploader("🎥 Envie seu vídeo de dashcam (.mp4)", type=["mp4"])

if uploaded_video:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_video.read())
    video_path = tfile.name

    # Modelo
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Layout
    col1, col2 = st.columns([1, 2])
    alert_box = col1.empty()
    stframe = col2.empty()
    progress_bar = st.progress(0)

    # Métricas
    total_alerts = 0
    current_frame = 0

    col1.markdown("### 📊 Métricas em tempo real:")
    met1 = col1.empty()
    met2 = col1.empty()
    met3 = col1.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, conf=0.4, verbose=False)
        boxes = results[0].boxes
        alerta = False

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            area = (x2 - x1) * (y2 - y1)
            if area > area_threshold:
                alerta = True

        # Alerta de colisão (lado esquerdo)
        if alerta:
            total_alerts += 1
            alert_box.markdown('<div class="big-alert">⚠️ ALERTA DE COLISÃO DETECTADO</div>', unsafe_allow_html=True)
        else:
            alert_box.markdown('<div style="color:green;">✔️ Nenhum risco de colisão detectado</div>', unsafe_allow_html=True)

        # Vídeo com bounding boxes
        annotated = results[0].plot()
        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        stframe.image(annotated, channels="RGB", use_column_width=True)

        current_frame += 1
        percent = int((current_frame / total_frames) * 100)
        progress_bar.progress(percent)

        # Atualiza métricas
        risk_pct = round((total_alerts / current_frame) * 100, 1) if current_frame else 0
        met1.metric("🎬 Frames", f"{current_frame}")
        met2.metric("🚨 Alertas", f"{total_alerts}")
        met3.metric("💥 Risco (%)", f"{risk_pct}%")

    cap.release()
    st.success("✅ Processamento concluído com sucesso!")
