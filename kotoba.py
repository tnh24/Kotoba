import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(page_title='Kotoba', layout='wide')

# Set header
st.header('Meaning')

# File and sheet details
excel_file = '1.xlsx'
sheet_names = ['Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6']
subheaders = ['だい １ か', 'だい 2 か', 'だい 3 か', 'だい 4 か', 'だい 5 か', 'だい 6 か']

# Load data from each sheet
dfs = {subheader: pd.read_excel(excel_file, sheet_name=sheet, usecols='B:C', header=0) for subheader, sheet in zip(subheaders, sheet_names)}

# Sidebar for navigation
selected_subheader = st.sidebar.selectbox("Choose Lesson", subheaders)

st.sidebar.markdown("---")


st.sidebar.markdown("Developed By [Thet Naung Hset](https://www.facebook.com/KoHset7k)")

# Display selected DataFrame
st.subheader(selected_subheader)
st.dataframe(dfs[selected_subheader], use_container_width=True, height=500)
st.markdown("---")

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
    <div class="footer">
        <p>© 2024 Thet Naung Hset. All rights reserved.</p>
    </div>
    """

st.markdown(footer, unsafe_allow_html=True)
