import streamlit as st

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def show():
    with st.container(border=True):
        
        st.markdown("<h2 style='text-align: center; color: #ffc130;'>👩‍🎓💻 Sobre o projeto acadêmico</h2>", unsafe_allow_html=True)        
       
        col0, col1 = st.columns([4, 3])
        with col0:

            st.markdown("")
            st.subheader("Equipe do projeto:", divider='green')
            st.markdown("""<h6 style='text-align: justify;'> Alunos: </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> -- Beathriz Gomes de Freitas; </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> -- Ellen Hubner Souza; </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> -- Emanuela Ramos Ribeiro; </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> -- Nicolas Daniel de Oliveira Silveira. </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> Desenvolvedor e Orientador: Profº. Esp. Paulo Vinicius Meireles. </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> Profº: Dr. Fábio da Silveira Castro. </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> Disciplina: Práticas Florestais Supervisionadas II (2024-2025). </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> Curso Técnico em Florestas Integrado ao Ensino Médio - Ifes Campus Ibatiba. </h6""", unsafe_allow_html=True)
            st.markdown("""<h6 style='text-align: justify;'> Projeto TCC: Sistema Coffee Predict (Previsão da Produção/Produtividade do Café no ES e MG). </h6""", unsafe_allow_html=True)
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
       