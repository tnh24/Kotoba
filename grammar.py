import streamlit as st
import pandas as pd

def display_grammar():
    # File and sheet details
    excel_file = '1.xlsx'
    sheet_names = ['Bonpoe']
    subheaders = ['ぶん　ぽう📜']

    # Load data from each sheet
    df = pd.read_excel(excel_file, sheet_name='Bonpoe', usecols='A', header=0)

    # Sidebar for navigation
    selected_subheader = st.sidebar.selectbox("Choose Lesson 📘", subheaders)

    st.subheader(selected_subheader)
    if selected_subheader == 'ぶん　ぽう📜':
        for index, row in df.iterrows():
            if pd.isna(row[0]):  # Check if the cell is empty
                st.markdown("<br>", unsafe_allow_html=True)
            else:
                centered_row = f"<div style='display: inline-block; width: 100%; text-align: left;'>{row[0]}</div>"
                st.markdown(centered_row, unsafe_allow_html=True)
    else:
        st.dataframe(dfs[selected_subheader].reset_index(drop=True), use_container_width=True, height=500, hide_index=True)
    st.markdown("---")
