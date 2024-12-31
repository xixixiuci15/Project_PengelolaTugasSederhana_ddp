import streamlit as st
from task_manager import TaskManager

task_manager = TaskManager()

def tampilkan_statistik():
    if not task_manager.data.empty:
        st.bar_chart(task_manager.data['Prioritas'].value_counts())
        
        total_tasks, completed_tasks, pending_tasks = task_manager.get_statistics()
        
        st.write(f"Total Tugas: {total_tasks}")
        st.write(f"Tugas Selesai: {completed_tasks}")
        st.write(f"Tugas Belum Selesai: {pending_tasks}")
    else:
        st.write("Tidak ada tugas yang tersedia.")

st.header("Statistik Tugas :roller_coaster:")
tampilkan_statistik()