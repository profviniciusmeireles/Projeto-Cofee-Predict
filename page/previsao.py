import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
import plotly.graph_objects as go
import plotly.express as px
import warnings

# Ignorar todos os avisos
warnings.filterwarnings("ignore")

def show():

    @st.cache_data
    def load_data():
        data = pd.read_excel("data/Dados_Conab.xlsx")
        return data

    df = load_data()

    #inicio da página
   
    st.subheader("📊 Previsão da Produção e Produtividade do Café ☕", divider='green')

    # Dividir a tela em duas colunas
    col1, col2 = st.columns([1.5, 4.5])
    with col1:
        # Seletores para variável, estado e ano de previsão
        with st.expander("Selecione as opções abaixo para realizar a previsão dos dados:", expanded=True):
            with st.container(border=True):        
                                
                # Escolher a variável dependente a ser prevista
                variavel_previsao = st.selectbox("Variável para previsão:", 
                                                ['Producao', 'Produtividade'])
                
                st.markdown("")
                # Definir ES como o estado selecionado por padrão
                estado = st.selectbox("Estado:", df['Estado'].unique(), index=1)
                st.markdown("")
                ano_previsao = st.slider("Ano para previsão:", 2025, 2035, step=1)

            #st.image("img/images.png")
          
    #Especificar a unidade de medida: produção /produtividade
    if variavel_previsao == 'Producao':
        unidade = 'em mil sacas'
    else:
        unidade = 'sacas/hectare' 

    # Filtrar dados do estado selecionado
    df_estado = df[df['Estado'] == estado]

    # Verificar se há dados suficientes
    if len(df_estado) >= 5:  # mínimo de dados para treinar o modelo
        # Preparação dos dados
        X = df_estado[['Ano']]
        y = df_estado[variavel_previsao]

        # Dividir os dados em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Modelo de Regressão Linear
        linear_model = LinearRegression()
        linear_model.fit(X_train, y_train)

        # Modelo de Regressão Polinomial (grau 2)
        poly = PolynomialFeatures(degree=2)
        X_poly_train = poly.fit_transform(X_train)
        X_poly_test = poly.transform(X_test)

        poly_model = LinearRegression()
        poly_model.fit(X_poly_train, y_train)

        # Previsão para o ano selecionado com Regressão Linear
        #previsao_linear = linear_model.predict([[ano_previsao]])[0]

        # Previsão para o ano selecionado com Regressão Polinomial
        ano_previsao_poly = poly.transform([[ano_previsao]])
        previsao_poly = poly_model.predict(ano_previsao_poly)[0]

        with col2:    
            # Exibir a previsão (Regressão Polinomial)
            with st.container(border=True): 
                st.markdown(f"🎯 Previsão para {estado} no ano de {ano_previsao}:")

                col0, col1 = st.columns(2)
                with col0:
                    if variavel_previsao == 'Producao':
                        st.info(f"Produção estimada: {previsao_poly:.2f} mil sacas.")  # Mude para previsao_linear se desejar
                    elif variavel_previsao == 'Produtividade':
                        st.info(f"Produtividade estimada: {previsao_poly:.2f} sacas/ha")  # Mude para previsao_linear se desejar
                    else:
                        st.error("Selecione uma variável válida para previsão.")

                # Métricas do modelo
                # Previsão para os dados de teste com Regressão Polinomial
                y_pred_poly = poly_model.predict(X_poly_test)

                # Calcular a precisão usando MAPE
                mape_poly = mean_absolute_percentage_error(y_test, y_pred_poly) * 100

                with col1:
                # Exibir a métrica de precisão
                    st.success(f"**Precisão do modelo Polinomial:** {100 - mape_poly:.2f}%")  # Precisão como porcentagem

                # Gerar gráfico de histórico e previsão
                fig = go.Figure()

                # Adicionar a linha de histórico
                fig.add_trace(go.Scatter(x=df_estado['Ano'], 
                                        y=df_estado[variavel_previsao], 
                                        mode='lines', 
                                        name='Histórico'))

                # Adicionar a previsão futura
                fig.add_trace(go.Scatter(x=[ano_previsao], 
                                        y=[previsao_poly], 
                                        mode='markers', 
                                        marker=dict(color='red', size=10), 
                                        name='Previsão Polinomial'))

                # Adicionar título e rótulos
                fig.update_layout(title='Previsão por Ano',
                                xaxis_title='Ano',
                                yaxis_title=f"{variavel_previsao} ({unidade})")

                # Exibir o gráfico
                st.plotly_chart(fig)
                st.write("<p style='font-size:13px;'>Fonte: Elaborado pelo autor</p>", unsafe_allow_html=True)
                
    else:
        st.info("Dados insuficientes para realizar previsão para este estado.")    

        