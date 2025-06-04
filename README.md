# 🚗 Real-Time Collision Warning System with YOLOv8

Este projeto implementa um **sistema de alerta de colisão em tempo real** utilizando **visão computacional com YOLOv8**.  
O sistema detecta veículos, pedestres e outros objetos em vídeos de dashcam e emite alertas visuais quando há risco de colisão iminente com base na distância aproximada dos objetos.

---

## 🎯 Funcionalidades

- ✅ Detecção em tempo real com **YOLOv8** (pré-treinado)
- ✅ Upload e análise de vídeos de **dashcam**
- ✅ **Alerta visual dinâmico** quando veículos estão muito próximos
- ✅ **Slider de sensibilidade** para controle do nível de risco
- ✅ Dashboard interativo com:
  - Número de frames processados
  - Número de alertas gerados
  - Porcentagem de risco
- ✅ Interface moderna e limpa feita com **Streamlit**

---

## 🖼️ Demonstração

<img src="https://img.icons8.com/fluency/96/car-crash.png" width="80"/>

> O app processa vídeos e exibe o alerta lateralmente sempre que detecta aproximação perigosa.

---

## 📂 Estrutura do Projeto

real-time-collision-warning/
├── app.py # Código principal do app Streamlit
├── requirements.txt # Bibliotecas necessárias
└── README.md # Este arquivo de documentação


---

## 🧪 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/Coringadev22/real-time-collision-warning.git
cd real-time-collision-warning


pip install -r requirements.txt
streamlit run app.py
```

🎛️ Sensibilidade do Alerta
Você pode ajustar o nível de sensibilidade com um slider na barra lateral.

Valores baixos (ex: 50.000): alerta mais sensível

Valores altos (ex: 200.000): alerta mais conservador (somente em risco real)

👨‍💻 Autor
Lucas Coelho
