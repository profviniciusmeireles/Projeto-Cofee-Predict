import streamlit as st

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def show():
    with st.container(border=True):
        
        st.markdown("<h2 style='text-align: center; color: #ffc130;'>👩‍🎓💻 Sobre o projeto</h2>", unsafe_allow_html=True)        
       
        col0, col1 = st.columns([2.5, 5])
        with col0:

            st.markdown("")
            st.subheader("Projeto:", divider='green')
            
            st.markdown("""<h6 style='text-align: justify;'> Desenvolvedor e Cientista de Dados: Profº. Esp. Paulo Vinicius Meireles. </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> Sistema Coffee Predict (Previsão da Produção/Produtividade do Café no ES e MG). </h6""", unsafe_allow_html=True)
            st.image("img/logo.png", use_container_width=True)
            #st.subheader("", divider='green')
        
        with col1:      
            st.markdown("")
            st.subheader("Ferramentas e Bibliotecas:", divider='green')
            
           # Define as imagens em uma matriz para organização em tabela
            images = [
                ["img/logo_coffee.png", "logo/01.png", "logo/02.png"],
                ["logo/03.png", "logo/04.png", "logo/05.png"],
                ["logo/06.png", "logo/07.png", "logo/IFES.png"]
            ]

            # Exibe a tabela de imagens
            for row in images:
                cols = st.columns(len(row))
                for col, img_path in zip(cols, row):
                    with col:
                        st.image(img_path, use_container_width=True)
       