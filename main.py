import streamlit as st
from sources import home, meaning, kanji, grammar, flashcard

# Set page configuration
st.set_page_config(page_title='Minano Nihongo', layout='wide', page_icon='🇯🇵')

# Set header
st.markdown("<h1 style='text-align: center;'>🧠 みんなの日本語 🧠</h1>", unsafe_allow_html=True)

# Sidebar for navigation
selected_module = st.sidebar.selectbox(
    "Choose Module 🛰️",
    ["Home 🛖", "Meaning 🎑", "Kanji 📚", "Grammar 🎫", "Flash Card Quiz 🧠"]
)

# Display selected module
if selected_module == "Home 🛖":
    home.display_home()
    st.balloons()
elif selected_module == "Meaning 🎑":
    meaning.display_meaning()
    st.balloons()
elif selected_module == "Kanji 📚":
    kanji.display_kanji()
    st.balloons()
elif selected_module == "Grammar 🎫":
    grammar.display_grammar()
    st.balloons()
elif selected_module == "Flash Card Quiz 🧠":
    flashcard.display_flashcard_quiz()

# Sidebar image and developer info
st.sidebar.image("sources/nihon.jpg")
st.sidebar.markdown("Developed By [Thet Naung Hset](https://www.facebook.com/KoHset7k) 💻")
st.sidebar.markdown("© 2024 Thet Naung Hset. All rights reserved. 🚀")

# Footer
footer = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}   
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: blue;
        text-align: center;
        padding: 10px;
    }
    [data-testid="stElementToolbar"] {
        display: none;
    }
    </style>
"""

st.markdown(footer, unsafe_allow_html=True)
