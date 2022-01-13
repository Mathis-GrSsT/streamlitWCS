#Imports des librairies utilisées 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

#Importer le dataset
cars = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep=',')

st.title("WILD CODE SCHOOL")
st.title("Quête Streamlit")
st.header("Analyse du dataset 'voitures'")
st.write("**Corrélation entre les différentes variables**")
st.markdown("**1)Heatmap**")

#Corrélations
df_corr = cars.corr()
        
#Heatmap : comprendre les corrélations entre les variables
sns.set_theme(style="white")
sns.set(rc={'figure.figsize':(5,3)})
corr = df_corr
cmap = sns.color_palette("mako", as_cmap=True)
heatmap = sns.heatmap(corr, cmap=cmap)
st.pyplot(heatmap.figure)

st.write("(Veuillez attendre quelques secondes que le pairplot s'affiche correctement...)")
st.write("**2) Pairplot**")       
#Pairplot : comprendre les corrélations entre les variables
pairplot = sns.pairplot(cars, hue='continent')
st.pyplot(pairplot.figure)
st.markdown('##')
st.write("**Commentaire :**")
st.write("Après une lecture attentive de la heatmap et du pairplot, les variables miles par gallon(mpg), la puissance en chevaux(hp) et le poids (weight) seront choisies pour la suite de cet exercice.")
st.write("Ces variables sont les plus corrélées entre elles et semblent plus pertinentes pour comparer les caractéristiques des voitures aux USA, Europe et Japon.")

st.markdown('##')
# Page dropdown 
page = st.selectbox("Pour poursuivre l'analyse, veuillez choisir la zone géographique : ", ["USA", "Europe", "Japon"]) 

if page == "USA":
    st.markdown('##')
    st.write("")

    cars_usa = cars[cars['continent'].str.contains('US.')]
    
    #MPG
    fig = px.histogram(cars_usa, x="mpg",
                   marginal="box", 
                   color_discrete_sequence=['lightseagreen'], 
                    width=900, 
                    height=600
                   )           
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig, use_container_width=True)

    #HP
    fig2 = px.histogram(cars_usa, x="hp",
                   marginal="box", 
                   color_discrete_sequence=['tomato'], 
                  width=900, 
                  height=600
                   )

    fig2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown('##')

    #WEIGHT
    fig3 = px.histogram(cars_usa, x="weightlbs",
                   marginal="box", 
                   color_discrete_sequence=['dodgerblue'], 
                  width=900, 
                  height=600
                   )

    fig3.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig3, use_container_width=True)

    st.write("**Commentaire :**")
    st.write("Les voitures nord-américaines ont consommation médiane de 18 miles par gallon, soit 13,1 litres/100km")
    st.write("De plus, la médiane de la puissance par voiture est de 110 chevaux")
    st.write("Enfin, le poids médian est de 3435 livres, soit 1558 kilos")

elif page == "Europe":
    st.markdown('##')
    st.write("")

    cars_europe = cars[cars['continent'].str.contains('Europe.')]
    
    #MPG
    fig4 = px.histogram(cars_europe, x="mpg",
                   marginal="box", 
                   color_discrete_sequence=['lightseagreen'], 
                    width=900, 
                    height=600
                   )           
    fig4.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig4, use_container_width=True)

    #HP
    fig5 = px.histogram(cars_europe, x="hp",
                   marginal="box", 
                   color_discrete_sequence=['tomato'], 
                  width=900, 
                  height=600
                   )

    fig5.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown('##')

    #WEIGHT
    fig6 = px.histogram(cars_europe, x="weightlbs",
                   marginal="box", 
                   color_discrete_sequence=['dodgerblue'], 
                  width=900, 
                  height=600
                   )

    fig6.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig6, use_container_width=True)

    st.write("**Commentaire :**")
    st.write("Les voitures européennes ont une consommation médiane de 26 miles par gallon, soit 9 litres pour 100 km environ")
    st.write("De plus la puissance médiane par voiture est de 77,5 chevaux")
    st.write("Enfin, le poids médian est de 2260 livres, soit 1025 kilos environ")

elif page == "Japon":
    st.markdown('##')
    st.write("")

    cars_japon = cars[cars['continent'].str.contains('Japan.')]
    
    #MPG
    fig7 = px.histogram(cars_japon, x="mpg",
                   marginal="box", 
                   color_discrete_sequence=['lightseagreen'], 
                    width=900, 
                    height=600
                   )           
    fig7.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig7, use_container_width=True)

    #HP
    fig8 = px.histogram(cars_japon, x="hp",
                   marginal="box", 
                   color_discrete_sequence=['tomato'], 
                  width=900, 
                  height=600
                   )

    fig8.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig8, use_container_width=True)

    st.markdown('##')

    #WEIGHT
    fig9 = px.histogram(cars_japon, x="weightlbs",
                   marginal="box", 
                   color_discrete_sequence=['dodgerblue'], 
                  width=900, 
                  height=600
                   )

    fig9.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    st.plotly_chart(fig9, use_container_width=True)

    st.write("**Commentaire :**")
    st.write("Les voitures japonaises ont une consommation médiane de 31,6 mpg, soit 7,44 litres pour 100 km")
    st.write("De plus, la puissance médiane est de 74 chevaux pourles voitures. ")
    st.write("Enfin, le poids médian d'une voiture japonaise est de 2155 livres, soit 977 kilos environ")

st.markdown('##')
st.markdown('##')
st.markdown('##')

#Image LOLCAT
image = Image.open('1fosca.jpeg')
st.image(image)