import streamlit as st
import os
import pandas as pd

path = os.path.join(os.getcwd(),"data")

description = """

Whether providing cutting-edge products, seamless services, or industry-leading expertise, Best Company remains committed to driving meaningful impact and long-term value. Guided by a strong mission and core values of integrity, innovation, and collaboration, Best Company is not just a provider—it is a trusted partner in progress.
"""

st.header("Best Company")
st.caption(description)
st.divider()

col1,col2,col3 = st.columns(3)

df = pd.read_csv(path+"/data.csv")

num = 0

for index, row in df.iterrows():

    with col1:
        st.text(row["first name"].title()+" "+row["last name"][0].title()+".")
    with col2:
        st.text(row["first name"].title()+" "+row["last name"][0].title()+".")