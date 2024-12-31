
import streamlit as st
from task_manager import TaskManager

# Set konfigurasi halaman
st.set_page_config(page_title="Aplikasi Pengelola Tugas", page_icon="📝")

# Judul aplikasi
st.title("Pengelola Tugas Sederhana")
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f5;
    }
    h1 {
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Menampilkan gambar header
st.image('header_image.jpg', width=800)  # Pastikan path gambar benar

# Menambahkan penjelasan aplikasi
st.write("""
    Aplikasi ini dirancang untuk membantu Anda mengelola tugas-tugas Anda dengan lebih efisien.
    Anda dapat melihat daftar tugas yang harus diselesaikan, termasuk deskripsi, tanggal jatuh tempo, 
    prioritas, dan status masing-masing tugas.
""")


task_manager = TaskManager()

st.subheader("Daftar Tugas :clipboard:")
st.dataframe((task_manager.data))

# Inisialisasi session state untuk menyimpan data tugas
if "tasks" not in st.session_state:
    st.session_state.tasks = []
