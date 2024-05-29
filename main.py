import streamlit as st
from meaning import display_meaning
from grammar import display_grammar

# Set page configuration
st.set_page_config(page_title='Kotoba 🌐', layout='wide')

# Set header
#st.header("🧠 みんなの日本語 🧠")
st.markdown("<h1 style='text-align: center;'>🧠 みんなの日本語 🧠</h1>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# Sidebar for navigation
selected_module = st.sidebar.selectbox("Choose Module 📘", ["Meaning", "Grammar"])

#st.sidebar.markdown("---")

# Display selected module
if selected_module == "Meaning":
    display_meaning()
elif selected_module == "Grammar":
    display_grammar()

st.sidebar.image("nihon.jpg",)

# Developer info with an emoji
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
