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

    
    
    file_path = '1.xlsx'

    display_table(file_path, 'hiragana', 'Hiragana Table')
    display_table(file_path, 'dakuon', 'Da Ku On Table')
    display_table(file_path, 'handakuon', 'Han Da Ku On Table')
    display_table(file_path, 'youon', 'Yo U On Table', height=422)

    display_table(file_path, 'katakana', 'Katakana Table', height=422)
    display_table(file_path, 'kdakuon', 'Katakana Da Ku On Table')    
    display_table(file_path, 'khandakuon', 'Katakana Han Da Ku On Table')
    display_table(file_path, 'kyouon', 'Katakana Yo U On Table', height=422)

    st.write("""
    	The left sidebar contains Options for **Meaning & Grammar**.
    """)
    st.markdown("---")

