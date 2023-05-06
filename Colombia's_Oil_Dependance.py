import streamlit as st
import pandas as pd
import numpy as np
import openpyxl

#streamlit run Colombia's_Oil_Dependance.py

st.set_page_config(
    page_title = 'Relation between crude oil statistics and Colombian Peso (COP)',
    page_icon = "https://cdn3.iconfinder.com/data/icons/oil-gas/100/14-512.png",
    layout = 'wide'
)
st.title("COil: A brief introduction")
#st.caption("This page participates in the Streamlit Hackathon Summit")

st.divider()

col_a, col_b, col_c = st.columns(3)

with col_a:

    st.markdown('''
    # Oil in Colombia's economy
    
    The key for Colombian peso's growth and adaptation to globalization from the late XX century 
    to the early XXIs was the full government support to activities related to extraction, such
    as mining and oil extraction, this late one became a huge contributor to the country's GDP, to
    the extent of being dependant of it. But as renewable energies got more appealing, inflation 
    increased, and crude oil barrel price significantly dropped and got unstable, Colombian peso
    have been suffering from devaluation. This is not the single reason for it, but it is a 
    pretty impactful part.
''')

    st.image("https://www.eltiempo.com/files/image_1200_680/uploads/2022/07/02/62c0dbbdd38a9.jpeg")
    

with col_b:
    st.image("https://media.istockphoto.com/id/531537113/photo/oil-platform.jpg?s=612x612&w=0&k=20&c=gRHd_eqKoNsfZcO1Rgm-gepzwe7aIL72A2jtFxWd8bU=")
    st.image("https://media.istockphoto.com/id/502454835/es/foto/pumpjack-en-sunrise.jpg?s=612x612&w=0&k=20&c=0ZTbAPb1J-0G6AosOiJ2gCx8aY3OwwiPOOhmV7cGbwE=")
with col_c:
    st.markdown('''

    # Ecopetrol

    It is a colombian both public-owned and private managed oil company that has the largest 
    scope in the territory and it's the most influential agent in Colombia's macroeconomy,
    their stock value is correlated with Colombian peso's value.   

    "Currently, Ecopetrol S.A. is the largest company in the country with a net income of $15.4 
    billion recorded in 2011 and the main oil company in Colombia. Due to its size, it belongs 
    to the group of the 40 largest oil companies in the world and is one of the four largest in 
    Latin America." -Ecopetrol's official website.
    ''')

    st.image(r"https://caracoltv.brightspotcdn.com/dims4/default/92ec93b/2147483647/strip/true/crop/1280x720+0+0/resize/1200x675!/quality/90/?url=http%3A%2F%2Fcaracol-brightspot.s3.amazonaws.com%2F89%2F64%2F4333fe5843df8b42db0e0cd188a4%2Fecopetrol-logo-foto-ecopetrol-twitter.jpg")

st.divider()
