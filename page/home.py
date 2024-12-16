import streamlit as st

def show():

   # Style
   with open('style.css')as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
      
      
                  
   with st.container(border=True): 
      st.subheader("☕ O Sistema Coffee Predict", divider='green')
      #Texto apresentação do Sistema
      
      st.markdown("""
         <style>
            .custom-text {
               text-align: justify; 
               line-height: 1.5;
            }
         </style>

         <h6 class='custom-text'> 
            Desenvolvido com algoritmos de Machine Learning (ML) de Inteligência Artificial (IA), melhora a previsão de safras futuras ao analisar dados históricos de produção e índices de produtividade. 
            Ele identifica padrões e antecipa o impacto de variáveis climáticas, auxiliando nas decisões estratégicas e no planejamento de safras. 
            A plataforma possui uma barra de navegação superior dividida em: 
         </h6>
         """, unsafe_allow_html=True)
      
      st.markdown("""<h6 style='text-align: justify;'> 🔹 (Home) - Página principal com informações e um resumo executivo sobre o Café no ES. </h6""", unsafe_allow_html=True)
      st.markdown("""<h6 style='text-align: justify;'> 🔹 (Análise) - Nessa página será demonstrado plotagem gráfica para análise da produção/produtividade por estado. </h6""", unsafe_allow_html=True)
      st.markdown("""<h6 style='text-align: justify;'> 🔹 (Resumo) - Mostra estatísticas anuais por estado com resumos de vários índices de produção/produtividade. </h6""", unsafe_allow_html=True)
      st.markdown("""<h6 style='text-align: justify;'> 🔹 (Mapa) - Seção onde é plotado o mapa interativo do ES e tabela de dados com informações de: Quantidade, Área produção e Valor total da produção (R$) em um determinado ano. </h6""", unsafe_allow_html=True)
      st.markdown("""<h6 style='text-align: justify;'> 🔹(Previsão) - Seção mais importante, na qual seleciona o estado, ano de previsão e variável, gerando um gráfico com a tendência histórica e o valor previsto. </h6""", unsafe_allow_html=True)
      st.markdown("<br>" , unsafe_allow_html=True)
      
      #Texto sobre resumo executivo
      st.subheader("📋🧑‍🌾 Resumo executivo do café no ES e MG", divider='green')
       
      col1, col2 = st.columns([5, 3])
      with col1: 
         st.markdown("""
            <style>
               .custom-text {
                  text-align: justify; 
                  line-height: 2;
               }
            </style>

            <h6 class='custom-text'> 
               O resumo executivo do boletim de setembro de 2024 da Conab traz uma análise da produção de café nos estados de Espírito Santo e Minas Gerais: 
            </h6>
            """, unsafe_allow_html=True)
         st.markdown("""<h5 style='text-align: justify;'> 1️⃣ Espírito Santo: </h5""", unsafe_allow_html=True)

         st.markdown("""
            <style>
               .custom-text {
                  text-align: justify; 
                  line-height: 1.5;
               }
            </style>

            <h6 class='custom-text'> 
               A produção total de café no estado está estimada em aproximadamente 14 milhões de sacas, refletindo um crescimento de 7,6% em relação à safra anterior. 
               O conilon representa uma grande parte dessa produção, com cerca de 9,97 milhões de sacas, o que é uma redução de 1,9% em comparação ao ano anterior. 
               Para o arábica, a produção aumentou significativamente em 41%, com uma estimativa de 4,03 milhões de sacas. 
            </h6>
            """, unsafe_allow_html=True)

         st.markdown("""<h5 style='text-align: justify;'> 2️⃣ Minas Gerais: </h5""", unsafe_allow_html=True)
         st.markdown("""
            <style>
               .custom-text {
                  text-align: justify; 
                  line-height: 1.5;
               }
            </style>

            <h6 class='custom-text'> 
               A produção de café arábica foi estimada em cerca de 28,06 milhões de sacas, apresentando uma redução de 3,3% em comparação com o ano anterior. 
               Essa diminuição é atribuída a condições climáticas adversas, como estiagens prolongadas e temperaturas elevadas, que afetaram as fases críticas do ciclo reprodutivo das plantações. 
               Cerca de 95% da colheita foi concluída até o final de agosto. 
            </h6>
            """, unsafe_allow_html=True)
         
         st.markdown("<br>" , unsafe_allow_html=True)
         st.markdown("""<h6 style='text-align: justify;'> 🔗 Fonte: [https://www.conab.gov.br/info-agro/safras/cafe]</h6""", unsafe_allow_html=True)
      with col2:
         st.image("img/cafe.jpg", width=6000) 
         
      st.markdown("<br>" , unsafe_allow_html=True)     

      #Texto sobre informações do café no ES
      st.subheader("📋 Informações sobre o café no Espírito Santo", divider='green')
       
      st.markdown("""
      <style>
         .custom-text {
            text-align: justify; 
            line-height: 2;
         }
      </style>

      <h6 class='custom-text'> 
         A cafeicultura é a principal atividade agrícola do Espírito Santo, desenvolvida em todos os municípios capixabas (exceto Vitória). 
         Gera em torno de 400 mil empregos diretos e indiretos e está presente aproximadamente em 60 mil das 90 mil propriedades agrícolas do Estado. 
         Dessa produção, em torno de 73% dos produtores capixabas são de base familiar, com o tamanho médio das propriedades em 8 hectares. 
         Existem 131 mil famílias produtoras capixabas.
      </h6>
      """, unsafe_allow_html=True)

      st.markdown("")

      st.markdown("""
      <h6 class='custom-text'> 
         O Espírito Santo é o 2º maior produtor brasileiro de café, com expressiva produção de arábica e conilon. 
         É responsável por mais de 30% da produção brasileira. Atualmente, existem 402 mil hectares em produção no Estado. 
         A atividade cafeeira é responsável por 37% do Produto Interno Bruto (PIB) Agrícola capixaba. 
      </h6>
      """, unsafe_allow_html=True)

      st.markdown("")

      st.markdown("""
      <h6 class='custom-text'> 
         É lei: 14 de maio é dia de iniciar a colheita do café conilon no ES, 60-80% de frutos maduros. 
         Também agora tem o dia 25 de maio para início da colheita do café arábica. 
         A medida evita que o café seja colhido antes da hora, garantindo assim mais qualidade aos grãos. 
         O Espírito Santo deverá produzir 16 milhões de sacas de café (arábica + conilon). 
         A maior produção de conilon foi de em torno de 11,2 milhões de sacas em 2021. 
         A maior produção de arábica chegou a 4,745 milhões de sacas em 2020 (estimativa). 
      </h6>
      """, unsafe_allow_html=True)

      st.markdown("")

      st.markdown("""
      <h6 class='custom-text'> 
         A cafeicultura está em todas as regiões do Estado de maneira bastante diversificada. 
         A diversidade começa nas espécies cultivadas no Estado: Coffea arábica (arábica) e Coffea canephora (conilon). 
         Além disso, a cafeicultura capixaba é praticada em diferentes altitudes, o nível tecnológico dos produtores é variado, 
         o tamanho das propriedades é diverso (os pequenos produtores são maioria, mas há grandes empresas rurais na cafeicultura capixaba), 
         e a qualidade do café produzido no Espírito Santo também é vasta. 
         O arábica é mais cultivado em regiões de temperaturas mais baixas e altitudes acima de 500m. 
         Já o conilon é de regiões mais quentes, normalmente plantado abaixo de 500m de altitude.
      </h6>
      """, unsafe_allow_html=True)

      st.markdown("")
      st.markdown("")
      st.markdown("""<h6 style='text-align: justify;'> 🔗 Fonte: [https://incaper.es.gov.br/cafeicultura]</h6""", unsafe_allow_html=True)

      #st.toast("Página atualizada!", icon='✅')