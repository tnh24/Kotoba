import streamlit as st
import pandas as pd

def display_grammar():
    # File and sheet details
    excel_file = '1.xlsx'
    sheet_names = ['Bonpoe1', 'Bonpoe2', 'Bonpoe3']
    subheaders = ['だい １ か 📝', 'だい 2 か 📚', 'だい 3 か 🗒️']

    # Sidebar for navigation
    selected_subheader = st.sidebar.selectbox("Choose Lesson 📘", subheaders)

    selected_sheet_name = sheet_names[subheaders.index(selected_subheader)]
    df = pd.read_excel(excel_file, sheet_name=selected_sheet_name, usecols='A', header=0)

    
    st.markdown("<h2 style='text-align: center;'>📜ぶん　ぽう📜</h2>", unsafe_allow_html=True)

    # Display selected subheader
    st.subheader(selected_subheader)
    
    # Iterate over rows and display content
    for index, row in df.iterrows():
        if pd.isna(row[0]):  # Check if the cell is empty
            st.markdown("<br>", unsafe_allow_html=True)
        else:            
            st.markdown(row[0])
            

    st.markdown("---")
