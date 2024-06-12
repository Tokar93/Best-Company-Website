import streamlit as st
import pandas as pd

folder = 'The-Best-Company-Website'

st.set_page_config(layout='wide')
st.header('The Best Company')
description = """Nvidia Corporation[a][b] (/ɛnˈvɪdiə/, en-VID-ee-ə) is an American multinational corporation and technology company headquartered
 in Santa Clara, California, and incorporated in Delaware. It is a software and fabless company which designs and supplies graphics processing 
 units (GPUs), application programming interfaces (APIs) for data science and high-performance computing, as well as system on a chip units (SoCs) 
 for the mobile computing and automotive market. Nvidia is also a dominant supplier of artificial intelligence (AI) hardware and software.
 """
st.write(description)

st.subheader('Our Team')

df = pd.read_csv(f'{folder}/data.csv')

col1, empty1, col2, empty2, col3, empty3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        full_name = f'{row['first name'].title()} {row['last name'].title()}'
        st.subheader(full_name)
        st.write(row['role'])
        st.image(f"{folder}/images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        full_name = f'{row['first name'].title()} {row['last name'].title()}'
        st.subheader(full_name)
        st.write(row['role'])
        st.image(f"{folder}/images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        full_name = f'{row['first name'].title()} {row['last name'].title()}'
        st.subheader(full_name)
        st.write(row['role'])
        st.image(f"{folder}/images/{row['image']}")


