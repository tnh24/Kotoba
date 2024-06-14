import streamlit as st
import pandas as pd

def display_grammar():
    # File and sheet details
    excel_file = 'sources/1.xlsx' ##sources/
    sheet_names = ['Bonpoe1', 'Bonpoe2', 'Bonpoe3', 'Bonpoe4', 'Bonpoe5', 'Bonpoe6', 'Bonpoe7', 'Bonpoe8']
    subheaders = ['だい １ か 📝', 'だい 2 か 📚', 'だい 3 か 🗒️', 'だい 4 か 🖋️', 'だい 5 か 📖', 'だい 6 か 📜', 'だい 7 か 📚', 'だい 8 か 🖋️']

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
    st.balloons()

if __name__ == '__main__':
    display_grammar()