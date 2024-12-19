import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def show():

    @st.cache_data
    def load_data():
        data = pd.read_excel("data/Dados_Conab.xlsx")
        return data

    df = load_data()

    ## st.info: texto justificado na página
    st.markdown("""
    <style>
    .stAlert p {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

    
    col1, col2 = st.columns([1, 6])
        
    with col1:    
        # Exibir selectbox para escolher o estado
        estado = st.radio("Selecione o estado:", df['Estado'].unique(), index=1, horizontal=True)             

    # Selecionar um único estado
    dados_estado = df[df['Estado'] == estado]
    with st.container(border=True):
        st.subheader(f"📈 Analisando dados para {estado}", divider='green')
    
        # Criar as 3 abas (Tabs)
        tabs = st.tabs(["Produção Anual", "Tendência e Sazonalidade", "Bienalidade", "Tabela de Dados"])

        with tabs[0]:
        # Produção Anual
            st.write("📊 Gráficos de Produção e Produtividade")

            # Criar a figura para produção e produtividade
            fig1, fig2 = st.columns(2)

            with fig1:
                # Produção
                fig_prod = go.Figure()
                fig_prod.add_trace(go.Bar(
                    x=dados_estado['Ano'],
                    y=dados_estado['Producao'],
                    name=f"{estado} - Produção",
                    marker_color='green',
                    opacity=0.6
                ))

                # Adicionar linha de média móvel para o estado selecionado
                fig_prod.add_trace(go.Scatter(
                    x=dados_estado['Ano'],
                    y=dados_estado['Producao'].rolling(2).mean(),
                    mode='lines+markers',
                    name=f"{estado} - Previsão Produção",
                    line=dict(color='red', dash='dash')
                ))

                fig_prod.update_layout(
                    xaxis_title='Ano',
                    yaxis_title=f"Produção (em mil sacas)",
                    #legend_title="Estado",
                    legend=dict(
                        orientation="h",  # Legenda horizontal
                        y=-0.2,  # Ajuste a posição vertical (acima do gráfico)
                        xanchor="center",  # Alinhar a legenda ao centro
                        x=0.5  # Ajuste a posição horizontal
                    )
                )

                st.plotly_chart(fig_prod)
            
            # Inicializar a figura para produtividade
            with fig2:
               
                fig_produtividade = go.Figure()
                fig_produtividade.add_trace(go.Bar(
                    x=dados_estado['Ano'],
                    y=dados_estado['Produtividade'],
                    name=f"{estado} - Produtividade",
                    marker_color='blue',
                    opacity=0.6
                ))

                # Adicionar linha de média móvel para o gráfico de Produtividade
                fig_produtividade.add_trace(go.Scatter(
                    x=dados_estado['Ano'],
                    y=dados_estado['Produtividade'].rolling(2).mean(),
                    mode='lines+markers',
                    name=f"{estado} - Previsão Produtividade",
                    line=dict(color='red', dash='dash')
                ))

                fig_produtividade.update_layout(
                    xaxis_title='Ano',
                    yaxis_title=f"Produtividade (sacas/hectare)",
                    #legend_title="Estado",
                    legend=dict(
                        orientation="h",  # Legenda horizontal
                        y=-0.2,  # Ajuste a posição vertical (acima do gráfico)
                        xanchor="center",  # Alinhar a legenda ao centro
                        x=0.5  # Ajuste a posição horizontal
                    )
                )
                st.plotly_chart(fig_produtividade)
                st.write("<p style='font-size:13px;'>Fonte: Conab</p>", unsafe_allow_html=True)


            
    #########################################################################################

        with tabs[1]:
        # Análise de tendência sazonal

            df_estado = dados_estado
            df_estado['Data'] = pd.to_datetime(df_estado['Ano'].astype(str) + '-01-01')  # Ajuste para dados mensais ou trimestrais
            df_estado.set_index('Data', inplace=True)

            # Aplicar decomposição de séries temporais
            from statsmodels.tsa.seasonal import seasonal_decompose
            result = seasonal_decompose(df_estado['Producao'], model='multiplicative', period=12)  # Período ajustável (12 para mensal)

            # Extraindo componentes de decomposição
            trend = result.trend
            seasonal = result.seasonal

            with st.container(border=True): 
                st.write("📅 Análise de Tendências Sazonais")
                
                col1, col2 = st.columns(2)
                with col1:
                    # Gráfico da tendência
                    fig_trend = go.Figure()
                    fig_trend.add_trace(go.Scatter(x=df_estado.index, y=trend, mode='lines', name='Tendência', line=dict(color='blue')))
                    fig_trend.update_layout(title=f'Tendência da Produção para {estado}', xaxis_title='Data', yaxis_title='Produção (em mil sacas)')
                    st.plotly_chart(fig_trend)
                
                with col2:
                    # Gráfico da sazonalidade
                    fig_seasonal = go.Figure()
                    fig_seasonal.add_trace(go.Scatter(x=df_estado.index, y=seasonal, mode='lines', name='Sazonalidade', line=dict(color='orange')))
                    fig_seasonal.update_layout(title=f'Sazonalidade da Produção para {estado}', xaxis_title='Data', yaxis_title='Produção (em mil sacas)')
                    st.plotly_chart(fig_seasonal)

                    
                # Exibir informações sobre os resultados
                if estado == "ES":
                    st.info(f"📅 **Resultado da decomposição sazonal para {estado}**: A análise da produção de café no Espírito Santo mostra uma tendência de crescimento constante ao longo dos anos. A sazonalidade apresenta variações anuais regulares com picos e quedas. Os resíduos são próximos de zero, indicando que o modelo captura bem a tendência e sazonalidade.")
                else:
                    st.info(f"📅 **Resultado da decomposição sazonal para {estado}**: A análise da produção de café em Minas Gerais indica uma tendência de crescimento contínuo de 2000 a 2024. A sazonalidade apresenta flutuações anuais regulares com picos e vales definidos. Resíduos próximos de zero mostram que a variabilidade é amplamente explicada pela tendência e sazonalidade.")


            # Exibir um gráfico da previsão ajustada para o ano selecionado
            with st.container(border=True): 
                st.write("📈 Previsão Ajustada")
                df_estado['Previsao_Ajustada'] = result.trend * result.seasonal  # Previsão ajustada pela tendência e sazonalidade

                # Gráfico de linha da previsão ajustada
                fig = go.Figure()

                fig.add_trace(go.Scatter(x=df_estado.index, y=df_estado['Producao'], mode='lines', name='Produção Original'))
                fig.add_trace(go.Scatter(x=df_estado.index, y=df_estado['Previsao_Ajustada'], mode='lines', name='Produção Ajustada', line=dict(dash='dash', color='red')))

                fig.update_layout(title=f'Produção Ajustada por Tendência Sazonal para {estado}',
                                xaxis_title='Data',
                                yaxis_title='Produção (em mil sacas)')

                st.plotly_chart(fig)
                st.write("<p style='font-size:13px;'>Fonte: Elaborado pelo autor</p>", unsafe_allow_html=True)

                # Exibir informações sobre os resultados da previsão ajustada
                if estado == "ES":
                    st.info(f"📅 **Resultado para {estado}**: A previsão ajustada para o ES mostra que a produção segue a original com sazonalidade suavizada. Entre 2005 e 2020, observa-se uma tendência de crescimento, com flutuações em 2015 e um pico em 2020, destacando as tendências subjacentes na produção..")
                else:
                    st.info(f"📅 **Resultado para {estado}**: A previsão ajustada para MG mostra que a produção acompanha de perto a original, com sazonalidade suavizada. Há uma tendência de crescimento até 2020, seguida por uma queda e uma recuperação parcial, destacando a tendência subjacente na produção. ")

        
        with tabs[2]:    
            with st.container(border=True): 
                st.write(f"📈 Bienalidade do Café: {estado}")     

                # Separar dados de bienalidade positiva (anos pares) e negativa (anos ímpares)
                positive_years = dados_estado[dados_estado['Ano'] % 2 == 0]
                negative_years = dados_estado[dados_estado['Ano'] % 2 != 0]

                # Separar dados de bienalidade positiva (anos pares) e negativa (anos ímpares)
                positive_years = dados_estado[dados_estado['Ano'] % 2 == 0]
                negative_years = dados_estado[dados_estado['Ano'] % 2 != 0]

                # Criar o gráfico com os anos como eixo X e a produção como eixo Y
                fig = go.Figure()

                # Adicionar colunas para bienalidade positiva e negativa
                fig.add_trace(go.Bar(
                    x=positive_years['Ano'],
                    y=positive_years['Producao'],
                    name='Bienalidade Positiva (Anos Pares)',
                    marker_color='green'        
                ))

                fig.add_trace(go.Bar(
                    x=negative_years['Ano'],
                    y=negative_years['Producao'],
                    name='Bienalidade Negativa (Anos Ímpares)',
                    marker_color='darkred'        
                ))

                # Adicionar linha de tendência móvel para a bienalidade positiva (anos pares)
                fig.add_trace(go.Scatter(
                    x=positive_years['Ano'],
                    y=positive_years['Producao'].rolling(2).mean(),
                    mode='lines+markers',
                    name='Tendência Bienalidade Positiva',
                    line=dict(color='aqua', dash='dash')
                ))

                # Adicionar linha de tendência móvel para a bienalidade negativa (anos ímpares)
                fig.add_trace(go.Scatter(
                    x=negative_years['Ano'],
                    y=negative_years['Producao'].rolling(2).mean(),
                    mode='lines+markers',
                    name='Tendência Bienalidade Negativa',
                    line=dict(color='yellow', dash='dash')
                ))


                # Ajustes do layout do gráfico
                fig.update_layout(
                    title=dict(
                        text=f"Produção Anual para {estado} - Comparação Bienalidade Positiva e Negativa",
                        x=0.5,              # Centraliza o título
                        xanchor="center",
                        yanchor="top"
                    ),
                    xaxis_title="Ano",
                    yaxis_title="Produção (em mil sacas)",
                    barmode='group',
                    legend=dict(
                        orientation="h",    # Horizontal
                        y=-0.2,             # Abaixo do gráfico
                        x=0.5,
                        xanchor="center"
                    )
                )

                  
                # Gráfico de pizza para proporção de bienalidade
                total_positive = positive_years['Producao'].sum()
                total_negative = negative_years['Producao'].sum()

                fig_pie = go.Figure(
                    go.Pie(
                        labels=['Bienalidade Positiva', 'Bienalidade Negativa'],
                        values=[total_positive, total_negative],
                        marker=dict(colors=['green', 'darkred']),
                        hole=0.4
                    )
                )

                fig_pie.update_layout(
                    title=dict(
                        text="Proporção de Bienalidade na Produção do Café",
                        x=0.5,             # Centraliza o título no contêiner
                        xanchor="center",
                        yanchor="top"
                    ),
                    legend=dict(
                        orientation="h",   # Horizontal
                        y=-0.2,            # Abaixo do gráfico
                        x=0.5,
                        xanchor="center"
                    )
                )

                # Exibir gráficos lado a lado
                col1, col2 = st.columns(2)

                with col1:
                    st.plotly_chart(fig)

                with col2:
                    st.plotly_chart(fig_pie)

                st.write("<p style='font-size:13px;'>Fonte: Elaborado pelo autor</p>", unsafe_allow_html=True)



                st.info(f"""
                O gráfico exibe a produção anual para o estado de {estado}, com a distinção entre anos de bienalidade positiva (pares) e negativa (ímpares).
                Observa-se uma flutuação consistente, indicando anos de maior e menor produção alternados, típica da bienalidade de culturas específicas como o Café Arábica. Essa análise ajuda a compreender a variação de produção e a expectativa para anos futuros.
                """)   
                
                st.divider()
                st.write("⌛ Fatores que influenciam a Bienalidade do Café:")


                # Exibir informações sobre os resultados da previsão ajustada
                if estado == "ES":
                    st.info(f"O {estado} é o 2º maior estado produtor, focado no café conilon, a resiliência climática do ES, com menor impacto de secas severas, torna a bienalidade mais branda. A variedade conilon é naturalmente mais estável e menos suscetível a flutuações, e o uso de técnicas de irrigação auxilia na manutenção da umidade constante, suavizando a bienalidade negativa. A adoção de tecnologias modernas também contribui para uma produção mais regular ao longo dos anos.")
                else:
                    st.info(f" {estado} é o maior produtor de café do Brasil, apresenta uma bienalidade fortemente influenciada por fatores como condições climáticas, onde períodos de chuva favorecem anos de alta produção. As práticas de manejo (poda e descanso das plantas) ajudam a manter o ciclo de bienalidade, enquanto a diversidade de solo e topografia propicia variações de produção. Além disso, a carga nutricional do solo é crucial; anos de alta produtividade podem esgotar os nutrientes, impactando a produção no ciclo seguinte. ")    

        with tabs[3]:  

            # Renomeando as colunas
            df.rename(columns={
                'PRODUCAO': 'Producao mil sacas',
                'AREA': 'Area em Producao ha',
                'PRODUTIVIDADE': 'Produtividade mil sacas/ha'
            }, inplace=True)
            
            # Configuração de estilo para o DataFrame
            styled_df = df.drop('id', axis=1).style.set_properties(
                **{
                    'background-color': '#f5f5f5',
                    'color': '#333',
                    'border': '1px solid #ddd',
                    'padding': '10px'
                }
            ).set_table_styles(
                [
                    {
                        'selector': 'thead th',
                        'props': [
                            ('background-color', '#4CAF50'),
                            ('color', 'white'),
                            ('font-weight', 'bold')
                        ]
                    },
                    {
                        'selector': 'tbody tr:nth-child(even)',
                        'props': [('background-color', '#e6f7ff')]  # Azul suave para linhas ímpares
                    },
                    {
                        'selector': 'tbody tr:nth-child(odd)',
                        'props': [('background-color', '#ffffff')]  # Branco para linhas pares
                    }
                ]
            )

            # Remover o índice antes de exibir a tabela
            styled_df = styled_df.hide(axis="index")

           
            
            with st.expander("📑 Tabela de Dados", expanded=True):
                st.table(styled_df)