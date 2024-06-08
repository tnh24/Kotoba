import streamlit as st
import pandas as pd

def display_home():


    st.title("Japanese Language for Beginners")
    st.header("Welcome!")
    st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This is a beginner-friendly lessons designed to help you learn the basics of the Japanese language. 
    Here you will find simple lessons, vocabulary, and practice exercises to get you started on your journey to mastering Japanese.
    """)

    def display_table(file_path, sheet_name, header_text, height=None):
	    df = pd.read_excel(file_path, sheet_name, header=0)
	    st.subheader(header_text)
	    st.dataframe(df.reset_index(drop=True), height=height, hide_index=True)

    
    
    file_path = 'sources/1.xlsx'

    display_table(file_path, 'hiragana', 'ひらがな Table')
    display_table(file_path, 'dakuon', 'だくおん Table')
    display_table(file_path, 'handakuon', 'はんだくおん On Table')
    display_table(file_path, 'youon', 'ようおん Table', height=422)

    display_table(file_path, 'katakana', 'かたかな Table', height=422)
    display_table(file_path, 'kdakuon', 'かたかな だくおん Table')    
    display_table(file_path, 'khandakuon', 'かたかな はんだくおん Table')
    display_table(file_path, 'kyouon', 'かたかな ようおん Table', height=422)

    st.write("""
    	The left sidebar contains Options for **Meaning & Grammar**.
    """)
    st.markdown("---")

