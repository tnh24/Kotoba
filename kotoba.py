import pandas as pd
import streamlit as st
import plotly.express as px

##from PIL import Image

# Set page configuration
st.set_page_config(page_title='Kotoba', layout='wide')

# Set header and initial subheader
st.header('Meaning')


### Load Data
excel_file = '1.xlsx'
sheet_names = ['Data1', 'Data2', 'Data3', 'Data4']
subheaders = ['だい １ か', 'だい 2 か', 'だい 3 か', 'だい 4 か']

# Load data from each sheet
dfs = [pd.read_excel(excel_file, sheet_name=sheet, usecols='B:C', header=0) for sheet in sheet_names]

# Display DataFrames
for subheader, df in zip(subheaders, dfs):
    st.subheader(subheader)
    st.dataframe(df, use_container_width=True)

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
        padding: 0px;
    }
    </style>
    <div class="footer">
        <p>© 2024 Thet Naung Hset. All rights reserved.</p>
    </div>
    """
st.markdown(footer, unsafe_allow_html=True)
