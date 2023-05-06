from snowflake.snowpark import Session
import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import os

st.set_page_config(
    page_title = 'Relation between crude oil statistics and Colombian Peso (COP)',
    page_icon = "https://cdn3.iconfinder.com/data/icons/oil-gas/100/14-512.png",
    layout = 'wide'
)

st.title("COil: graphs")
root_dir = os.getcwd()

#For snowflake's tables
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()
session = create_session()

@st.cache_data
def load_data(table_name):
    table = session.table(table_name)
    table = table.collect()
    return table
table_name = "COLCOV_V3.PUBLIC.MACANCAN"
covcol = load_data(table_name)

#database import
df_covcol = pd.DataFrame(covcol, columns = ["date", "cases", "deaths"])
df_covcol = df_covcol.rename(columns = {'date' : 'Date'})
cop2usd_dataset = pd.read_csv(os.path.join(root_dir, r"banrep_cop2usd.csv"), usecols= ["Date", "Dollar in COP"])
ecopetrol_stock_dataset = pd.read_csv(os.path.join(root_dir, r"ECOPETROL.CL.csv"), usecols = ["Date", "Close"])
brent_dataset = pd.read_csv(os.path.join(root_dir, r"brent.csv"), usecols= ["Date", "Close"])

#date formatting
df_covcol['Date'] = pd.to_datetime(df_covcol['Date']).dt.date
cop2usd_dataset['Date'] = pd.to_datetime(cop2usd_dataset['Date']).dt.date
ecopetrol_stock_dataset['Date'] = pd.to_datetime(ecopetrol_stock_dataset['Date']).dt.date
brent_dataset['Date'] = pd.to_datetime(brent_dataset['Date']).dt.date

#non-scaled
ns_df_covcol = df_covcol.copy()
ns_cop2usd_dataset = cop2usd_dataset
ns_ecopetrol_stock_dataset = ecopetrol_stock_dataset
ns_brent_dataset = brent_dataset

#scaling
df_covcol['cases'] = df_covcol['cases']/3
df_covcol['deaths'] = df_covcol['deaths']/3
brent_dataset['Close'] = brent_dataset['Close']*30

#renaming
brent_dataset = brent_dataset.rename(columns = {'Close' : 'Brent Crude'})
df_covcol = df_covcol.rename(columns = {'cases' : 'Covid-19 Cases', 'deaths' : 'Covid-19 Deaths'})
ecopetrol_stock_dataset =  ecopetrol_stock_dataset.rename(columns={'Close': 'Ecopetrol\'s Stock'})

st.divider()

#options
choice = st.selectbox(
    'What would you like to see?',
    ('Graph.', 'Dataframes.', 'The developer\'s cat.'))

st.divider()

#shows the graph with all databases' values
if choice == 'Graph.':
    original_currency_mode = st.checkbox('If you want to see the actual value of 1 USD to COP, select this box, otherwise, a scaled COP value will be plotted.')

    if not original_currency_mode:
        cop2usd_dataset = cop2usd_dataset.rename(columns= {'Dollar in COP' : '1 COP -> Dollar'})
        #scaling
        cop2usd_dataset['1 COP -> Dollar'] = (1/cop2usd_dataset['1 COP -> Dollar'])*1e7

        #merge of all databases
        pre_merge = pd.merge(ecopetrol_stock_dataset, cop2usd_dataset, on='Date', how='left')
        merge = pd.merge(pre_merge, brent_dataset, on='Date', how='left')
        final_merge = pd.merge(merge, df_covcol, on='Date', how='left')

        #plot
        st.line_chart(final_merge,
        x = 'Date',
        y = ['1 COP -> Dollar', 'Ecopetrol\'s Stock', 'Brent Crude', 'Covid-19 Cases', 'Covid-19 Deaths'])

        st.markdown('''
        # Values

        - 1 COP to Dollar (1:1e7)

        - Ecopetrol\'s Stock Price

        - Global Brent Crude Price (30:1)

        ## Courtesy of Snowflake

        -Covid-19 Cases and Deaths in Colombia throughout 2020 (1:3)

        ''')

    else:
        #merge of all databases
        pre_merge = pd.merge(ecopetrol_stock_dataset, cop2usd_dataset, on='Date', how='left')
        merge = pd.merge(pre_merge, brent_dataset, on='Date', how='left')
        final_merge = pd.merge(merge, df_covcol, on='Date', how='left')

        #plot
        st.line_chart(final_merge,
        x = 'Date',
        y = ['Dollar in COP', 'Ecopetrol\'s Stock ', 'Brent Crude', 'Covid-19 Cases', 'Covid-19 Deaths'])

#show the raw dataframes
elif choice == 'Dataframes.':
    st.caption("You may need to slide the dataframes to see the values")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("COP-Dollar Conversion")
        st.dataframe(ns_cop2usd_dataset)

        st.markdown('''
        Ecopetrol's
        Stock Value''')
        st.dataframe(ns_ecopetrol_stock_dataset)

    with col_b:
        st.markdown("Global Brent Crude Price")
        st.dataframe(ns_brent_dataset)

        st.markdown("Covid-19 Cases and Deaths in Colombia (2020)")
        st.dataframe(ns_df_covcol)

#shows my cat
elif choice == 'The developer\'s cat.':
    st.image("cat.png")
    st.balloons()
st.divider()

st.markdown('''

# Conclusions

- It is visible that there is a correlation between Ecopetrol's stock value and the brent oil price.

- On 2020, when Covid-19 peaked at deaths and causes, there was a hard drop in all values, and after that year
they slowly began to go up.

- 2000s Colombian Peso has enjoyed stability when Ecopetrol's stock value is high.

''')

st.divider()

st.markdown('''
### Sources

- [Republic of Colombia's Bank](https://www.banrep.gov.co/es/estadisticas/trm)

- [Yahoo Finance Database](https://finance.yahoo.com)

- [Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org)

''')
