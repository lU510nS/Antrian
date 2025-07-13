import streamlit as st
from PIL import Image
import os

# Judul aplikasi
st.title("📊 Model Antrian M/M/1 - PT. Barokah")

# Menampilkan gambar jika ada
image_path = "gambar.png"
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption="Ilustrasi Antrian", use_container_width=True)

st.markdown("## 📌 Input Parameter")

# Input user
λ = st.number_input("Tingkat kedatangan (λ - pelanggan/jam)", value=15)
μ = st.number_input("Tingkat pelayanan (μ - pelanggan/jam)", value=20)

if λ >= μ:
    st.error("⚠️ Sistem tidak stabil! Pastikan λ < μ")
else:
    ρ = λ / μ
    L = λ / (μ - λ)
