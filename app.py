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

# Responsividade CSS
st.markdown("""
<style>
/* Responsividade */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }
    .nav-bar-container {
        flex-direction: column;
        align-items: flex-start;
    }
    .nav-bar {
        flex-direction: column;
        width: 100%;
    }
}

/* Customização da barra de navegação */
.nav-bar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #fafafa;
    width: 100%;
    position: fixed;
    top: 0;
    z-index: 1000;
    padding: 0 20px;
}

.nav-bar {
    display: flex;
    justify-content: center;
    flex-grow: 1;
}
</style>
""", unsafe_allow_html=True)

# Banner
with st.container():
    image = Image.open("img/Banner_logo.jpg")
    st.image(image, use_container_width=True)

# Remover espaço em branco
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

selected = "Home"

# Navegação
with st.container():
    st.markdown("""
        <div class="nav-bar-container">
            <div class="nav-bar">
    """, unsafe_allow_html=True)

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
                "font-size": "20px",
            },
            "nav-link": {
                "font-size": "14px",
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

    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)

# Carregar páginas
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
