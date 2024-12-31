import streamlit as st
from task_manager import TaskManager
import pandas as pd
import datetime as datetime

task_manager = TaskManager()

def tampilkan_kalender():
    # # Debug: Tampilkan isi data sebelum pemeriksaan
    # st.write("Isi data tugas saat ini:", task_manager.data)

    if not task_manager.data.empty:
        st.subheader("Kalender Tugas :hourglass_flowing_sand:")
        
        # Mengonversi kolom tanggal jatuh tempo ke datetime
        task_manager.data['Tanggal Jatuh Tempo'] = pd.to_datetime(task_manager.data['Tanggal Jatuh Tempo'], errors='coerce')
        
        # Menghapus baris dengan tanggal jatuh tempo yang tidak valid
        task_manager.data = task_manager.data.dropna(subset=['Tanggal Jatuh Tempo'])
        
        st.write(task_manager.data[['Tugas', 'Tanggal Jatuh Tempo', 'Prioritas', 'Status']])

# Panggil fungsi untuk menampilkan kalender
tampilkan_kalender()