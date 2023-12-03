import streamlit as st 
from web_function import load_data
from streamlit_option_menu import option_menu

from Tabs import home, predict, visualise
Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

# Membuat Sidebar

st.sidebar.title ("Navigasi")
## Membuat radio Option
page = st.sidebar.radio ("Pages", list(Tabs.keys()))

## Load Data
df,x,y = load_data ()

## Kondisi call app function
if page in ["Prediction", "Visualisation"] :
    Tabs[page].app(df, x, y)
    
else :
    Tabs[page].app()
