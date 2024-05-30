import streamlit as st
import pandas as pd

def display_meaning():
    # File and sheet details
    excel_file = '1.xlsx'
    sheet_names = ['Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7','Data8', 'Verb']
    subheaders = ['だい １ か 📝', 'だい 2 か 📚', 'だい 3 か 🗒️', 'だい 4 か 🖋️', 'だい 5 か 📖', 'だい 6 か 📜', 'だい 7 か 📚','だい 8 か 📖', 'どうし 🖋️']

    # Load data from each sheet
    dfs = {subheader: pd.read_excel(excel_file, sheet_name=sheet, usecols='B:C', header=0) for subheader, sheet in zip(subheaders, sheet_names)}

    # Sidebar for navigation
    selected_subheader = st.sidebar.selectbox("Choose Lesson 📘", subheaders)

    st.markdown("<h2 style='text-align: center;'>📚ことば📚</h2>", unsafe_allow_html=True)

    st.subheader(selected_subheader)
    st.dataframe(dfs[selected_subheader].reset_index(drop=True), use_container_width=True, height=500, hide_index=True)
    st.markdown("---")
