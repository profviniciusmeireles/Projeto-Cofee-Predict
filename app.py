import streamlit as st

# Apps
st.set_page_config(page_title="App Coffee Predict", page_icon=":☕:", layout="wide")

import page.home as home
import page.analise as analise
import page.resumo as resumo
import page.mapa as mapa
import page.previsao as previsao
import page.sobre as sobre
from PIL import Image

# Style
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from streamlit_option_menu import option_menu



with st.container():
    # Abrir e redimensionar a imagem
    image = Image.open("img/Banner_logo.jpg")
    st.image(image, use_container_width=True)

# Remover espaço em branco no topo da barra de menu
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

selected = "Home"

# Carregar a página com base na seleção
with st.container():
    # Contêiner flex para barra de navegação
    st.markdown("""
        <style>
            .nav-bar-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #fafafa;
                width: 100vw;
                position: fixed;
                top: 0;
                z-index: 1000;
                padding: 0 20px; /* Espaçamento lateral */
            }
            .nav-bar {
                display: flex;
                justify-content: center;
                flex-grow: 1;
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML para o contêiner
    st.markdown("""
        <div class="nav-bar-container">
            <div class="nav-bar">
    """, unsafe_allow_html=True)

    # Menu superior de navegação
    selected = option_menu(
        None,
        ["Home", "Análise", "Resumo", "Mapa", "Previsão", "Sobre"],
        icons=['house', 'bar-chart-line', 'calendar-check', 'map', 'calendar', 'info-circle'],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent",
                "width": "100%",
            },
            "icon": {
                "color": "orange",
                "font-size": "25px",
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#b6d7a8",
                "flex-grow": "1",
            },
            "nav-link-selected": {
                "background-color": "green",
                "color": "white",
            },
        }
    )

    # Fechando a div da barra de navegação
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

# Carregar a página com base na seleção
if selected == "Home":
    home.show()
elif selected == "Análise":
    analise.show()
elif selected == "Resumo":
    resumo.show()
elif selected == "Mapa":
    mapa.show()
elif selected == "Previsão":
    previsao.show()
elif selected == "Sobre":
    sobre.show()