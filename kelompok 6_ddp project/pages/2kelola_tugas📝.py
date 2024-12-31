import streamlit as st
from task_manager import TaskManager

task_manager = TaskManager()

def kelola_tugas():
    if not task_manager.data.empty:
        
        for i, task in enumerate(task_manager.data['Tugas']):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"{i + 1}. {task} - Status: {task_manager.data.at[i, 'Status']}")
                
            with col2:
                if st.button("Selesai", key=f"selesai_{i}"):
                    task_manager.update_status(i, "Selesai")
                    st.success(f"Tugas '{task}' telah ditandai selesai!")
                    
            with col3:
                if st.button("Hapus", key=f"hapus_{i}"):
                    task_manager.delete_task(i)
                    st.success(f"Tugas '{task}' telah dihapus!")
    else:
        st.write("Tidak ada tugas yang tersedia.")

st.header("Kelola Tugas :seedling:")
kelola_tugas()