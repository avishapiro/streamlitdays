import pandas as pd
import plotly.express as px
import streamlit as st


st.header('A plotly example')
st.subheader('Sample data:')
df = px.data.iris()
st.dataframe(df, )

st.subheader('Static figure')
fig = px.density_heatmap(df, x="sepal_length", y="sepal_width", marginal_x='histogram', marginal_y='histogram', 
                         facet_row='species')
st.write(fig)

st.subheader('Figure with button')

def subset_species(species):
    return df[df.species == species]
    

option = st.selectbox('Species', df.species.unique())

fig = px.density_heatmap(subset_species(option), x="sepal_length", y="sepal_width", marginal_x='histogram', marginal_y='histogram',
                         title=option)
st.write(fig)


