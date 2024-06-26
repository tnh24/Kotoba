import streamlit as st
import pandas as pd

def display_meaning():
    # File and sheet details
    excel_file = 'sources/1.xlsx'
    sheet_names = ['Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7','Data8', 'Data9', 'Data10', 'Data11', 'Data12', 'Data13','Data14','Data15', 'Verb']
    subheaders = ['だい １ か 📝', 'だい 2 か 📚', 'だい 3 か 🗒️', 'だい 4 か 🖋️', 'だい 5 か 📖', 'だい 6 か 📜', 'だい 7 か 📚','だい 8 か 📖', 'だい 9 か 📝', 'だい 10 か 📜', 'だい 11 か 📝', 'だい 12 か 📚', 'だい 13 か 🗒️', 'だい 14 か 📜', 'だい 15 か 📖', 'どうし 🖋️']

    # Load data from each sheet
    dfs = {subheader: pd.read_excel(excel_file, sheet_name=sheet, usecols='B:C', header=0) for subheader, sheet in zip(subheaders, sheet_names)}

    # Sidebar for navigation
    selected_subheader = st.sidebar.selectbox("Choose Lesson 📘", subheaders)

    st.markdown("<h2 style='text-align: center;'>📚ことば📚</h2>", unsafe_allow_html=True)

    st.subheader(selected_subheader)
    st.dataframe(dfs[selected_subheader].reset_index(drop=True), use_container_width=True, height=500, hide_index=True)
    st.markdown("---")
    st.balloons()