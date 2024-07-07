import streamlit as st
import pandas as pd

def display_kanji():
    # File and sheet details
    excel_file = 'sources/1.xlsx'
    sheet_names = ['Kanji', 'Kanji2', 'Kanji3', 'Kanji4', 'Kanji5']
    subheaders = ['感じ 50 📝', '感じ 100 📝', '感じ 150 📝', '感じ 200 📝', '感じ 250 📝']

    # Load data from each sheet
    dfs = {subheader: pd.read_excel(excel_file, sheet_name=sheet, usecols='B:D', header=0) for subheader, sheet in zip(subheaders, sheet_names)}

    # Sidebar for navigation
    selected_subheader = st.sidebar.selectbox("Choose Lesson 📘", subheaders)

    st.markdown("<h2 style='text-align: center;'>📚　感じ　📚</h2>", unsafe_allow_html=True)

    st.subheader(selected_subheader)
    st.dataframe(dfs[selected_subheader].reset_index(drop=True), use_container_width=True, height=500, hide_index=True)
    st.markdown("---")
    st.balloons()

if __name__ == '__main__':
    display_kanji()