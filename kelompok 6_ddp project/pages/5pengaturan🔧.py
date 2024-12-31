import streamlit as st
from datetime import datetime

def pengaturan():

    # Pengaturan tema tampilan
    theme_option = st.selectbox("Pilih Tema Tampilan:", ["Default", "Gelap"])
    
    if theme_option == "Gelap":
        st.markdown(
            """
               <style>
            .stApp {
                background-color: black;
                color: white;
            }
            .stText, .stMarkdown, .stHeader, .stSubheader {
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    # Pengaturan notifikasi
    notification_enabled = st.checkbox("Aktifkan Notifikasi")
    
    if notification_enabled:
        notification_time = st.time_input("Waktu Notifikasi", datetime.now().time())
    
    # Simpan preferensi pengguna (ini hanya simulasi; Anda perlu menyimpan ke file atau database jika diperlukan)
    if st.button("Simpan Preferensi"):
        st.success("Preferensi telah disimpan!")

st.header("Pengaturan Aplikasi :hammer_and_wrench:")
pengaturan()