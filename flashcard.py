import streamlit as st
import pandas as pd
import random

def display_flashcard_quiz():
    # File and sheet details
    excel_file = '1.xlsx'
    sheet_names = ['Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10', 'Verb']
    subheaders = ['だい １ か 📝', 'だい 2 か 📚', 'だい 3 か 🗒️', 'だい 4 か 🖋️', 'だい 5 か 📖', 'だい 6 か 📜', 'だい 7 か 📚', 'だい 8 か 📖', 'だい 9 か 📝', 'だい 10 か 📜', 'どうし 🖋️']

    # Load data from each sheet
    dfs = {subheader: pd.read_excel(excel_file, sheet_name=sheet, usecols='B:C', header=0) for subheader, sheet in zip(subheaders, sheet_names)}

    # Sidebar for navigation
    selected_subheader = st.sidebar.selectbox("Choose Lesson 📘", subheaders)

    st.markdown("<h2 style='text-align: center;'>📚ことば📚</h2>", unsafe_allow_html=True)
    st.subheader(selected_subheader)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Get the selected dataframe
    df = dfs[selected_subheader]    

    col1, col2 = st.columns(2)
    with col1:
        question_button = st.button(
            "Generate Question", key="question_button", use_container_width=True
        )
    with col2:
        answer_button = st.button(
            "Show Answer", key="answer_button", use_container_width=True
        )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Initialize session state variables if not already initialized
    if "question_indices" not in st.session_state:
        st.session_state.question_indices = []

    # Question and answer logic
    if question_button:
        # Randomly select question number
        question_index = random.randint(0, len(df) - 1)
        # Check if the question index has been previously displayed
        while question_index in st.session_state.question_indices:
            question_index = random.randint(0, len(df) - 1)
        st.session_state.question_index = question_index        
        st.markdown(
            f"""
            <div style='text-align: center; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'>
                <h2>{df.iloc[question_index, 1]}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Add the displayed question index to the list
        st.session_state.question_indices.append(question_index)

        # Reset the list if all questions have been displayed once
        if len(st.session_state.question_indices) == len(df):
            st.session_state.question_indices = []

        st.session_state.show_answer = False

    if answer_button:
        if "question_index" in st.session_state:
            if not st.session_state.show_answer:
                st.markdown(
                    f"""
                    <div style='text-align: center; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'>
                        <h2>{df.iloc[st.session_state.question_index, 0]}</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )               
                st.session_state.show_answer = True
            else:
                st.warning("Answer already shown. Generate a new question.")
        else:
            st.warning("Generate a question first.")
