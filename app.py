import streamlit as st

#streamlit run Colombia's_Oil_Dependance.py


st.set_page_config(
    page_title = 'Relation between crude oil statistics and Colombian Peso (COP)',
    page_icon = "https://cdn3.iconfinder.com/data/icons/oil-gas/100/14-512.png",
    layout = 'wide'
)
st.title("COil: A brief introduction")
#st.caption("This page participates in the Streamlit Hackathon Summit")

st.divider()

col_a, col_b = st.columns(2)

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

    st.image("https://www.ecopetrol.com.co/wps/wcm/connect/cb44af1f-5db0-41e3-99c3-764dbc0517ce/eco_uso5.png?MOD=AJPERES&CACHEID=ROOTWORKSPACE-cb44af1f-5db0-41e3-99c3-764dbc0517ce-oa9BuxW")

with col_b:
    st.write('''⠀
    
    
    
    
    
    
    
    Extractor Machines⠀''')
    st.image("https://www.eltiempo.com/files/image_1200_680/uploads/2022/07/02/62c0dbbdd38a9.jpeg")

    st.markdown('''

    # Ecopetrol

    It is a colombian both public-owned and private managed oil company that has the largest 
    scope in the territory and it's the most influential agent in Colombia's macroeconomy,
    their stock value is correlated with Colombian peso's value.   
    ''')

st.divider()

