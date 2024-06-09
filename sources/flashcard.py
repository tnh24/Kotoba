import streamlit as st
import pandas as pd
import random

def display_flashcard_quiz():
    # File and sheet details
    excel_file = 'sources/1.xlsx'
    sheet_names = [
        'Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 
        'Data7', 'Data8', 'Data9', 'Data10', 'Data11', 'Data12', 
        'Data13', 'Verb'
    ]
    subheaders = [
        'だい １ か 📝', 'だい 2 か 📚', 'だい 3 か 🗒️', 'だい 4 か 🖋️', 'だい 5 か 📖', 
        'だい 6 か 📜', 'だい 7 か 📚', 'だい 8 か 📖', 'だい 9 か 📝', 'だい 10 か 📜', 
        'だい 11 か 📝', 'だい 12 か 📚', 'だい 13 か 🗒️', 'どうし 🖋️'
    ]

    # Load data from each sheet
    dfs = {subheader: pd.read_excel(excel_file, sheet_name=sheet, usecols='B:C', header=0) for subheader, sheet in zip(subheaders, sheet_names)}

    # Sidebar for navigation
    selected_subheader = st.sidebar.selectbox("Choose Lesson 📘", subheaders)

    # Display header and subheader
    st.markdown("<h2 style='text-align: center;'>📚ことば📚</h2>", unsafe_allow_html=True)
    st.subheader(selected_subheader)
    st.markdown("<br>", unsafe_allow_html=True)

    # Initialize session state variables if not already initialized
    if "question_indices" not in st.session_state:
        st.session_state.question_indices = []

    # Get the selected dataframe
    df = dfs[selected_subheader]

    # CSS for flip card
    flip_card_css = """
    <style>
    .flip-card {
      background-color: transparent;
      width: 100%;
      height: 200px;
      perspective: 1000px;
      margin: 0 auto;
    }

    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
    }

    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border: 5px solid yellow;
      padding: 20px;
      border-radius: 20px;
      box-sizing: border-box;
    }

    .flip-card-front {
      background-color: red;
      color: black;
    }

    .flip-card-back {
      background-color: blue;
      color: white;
      transform: rotateY(180deg);
    }
    </style>
    """

    st.markdown(flip_card_css, unsafe_allow_html=True)

    # Button to generate a question
    question_button = st.button("Generate Question", key="question_button", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Question and answer logic
    if question_button:
        # Randomly select question number
        question_index = random.randint(0, len(df) - 1)
        
        # Ensure the question hasn't been displayed before
        while question_index in st.session_state.question_indices:
            question_index = random.randint(0, len(df) - 1)
        
        st.session_state.question_index = question_index

        # Display the flashcard
        st.markdown(
            f"""
            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <h2>{df.iloc[question_index, 1]}</h2>
                </div>
                <div class="flip-card-back">
                  <h2>{df.iloc[question_index, 0]}</h2>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add the displayed question index to the list
        st.session_state.question_indices.append(question_index)

        # Reset the list if all questions have been displayed once
        if len(st.session_state.question_indices) == len(df):
            st.session_state.question_indices = []

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Hover over Or Tab the card to flip and see the answer.</p>", unsafe_allow_html=True)

    
