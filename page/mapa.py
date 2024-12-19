import streamlit as st
import pandas as pd
import folium
from folium import Choropleth
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import json
from streamlit_extras.metric_cards import style_metric_cards


def show():
    @st.cache_data
    def load_data():
        return pd.read_excel("data/Cafe_ES.xlsx")

    df = load_data()

    required_columns = ["ANO", "CIDADE", "VALOR", "QUANTIDADE", "AREA", "LATITUDE", "LONGITUDE"]
    if not all(col in df.columns for col in required_columns):
        st.error("Colunas necessárias não encontradas no arquivo. Verifique o arquivo Excel.")
        return

    anos_disponiveis = sorted(df['ANO'].unique())
    ano_selecionado = st.radio("Selecione o Ano:", anos_disponiveis, horizontal=True)
    df_ano = df[df['ANO'] == ano_selecionado]

    with st.container(border=True): 
        st.subheader(f"Mapa do ES: Café - Estatística de produção {ano_selecionado}", divider='green')

        col1, col2, col3 = st.columns([1.5, 4.5, 2])

        # Aplicando estilo CSS às métricas
        st.markdown("""
        <style>
            .stMetric > div {
                font-size: 20px !important;
            }
            .stMetric .label {
                font-size: 10px !important;
                font-weight: bold !important;
                color: #000000 !important; /* Preto */
        }        
            .stMetric .delta {
                font-size: 10px !important;
                font-weight: bold !important;
                color: #1E90FF !important; /* Azul */
        }
        </style>
        """, unsafe_allow_html=True)

        with col1:
            st.markdown("##### Estatísticas")

            # Cálculo das métricas
            df_ano_filtered = df_ano[df_ano['VALOR'] > 0]

            if not df_ano_filtered.empty:
                # Calcula as métricas principais
                valor_total = df_ano_filtered['VALOR'].sum()
                quantidade_total = df_ano_filtered['QUANTIDADE'].sum()
                area_total = df_ano_filtered['AREA'].sum()
                rendimento_medio = (quantidade_total / area_total) * 1000 if area_total > 0 else 0

                # Cidades de maior e menor produção
                maior_produtor = df_ano_filtered.loc[df_ano_filtered['VALOR'].idxmax(), 'CIDADE']
                menor_produtor = df_ano_filtered.loc[df_ano_filtered['VALOR'].idxmin(), 'CIDADE']

                # Exibe métricas no formato adaptado
                st.metric(label=f"{maior_produtor} (Maior Produtor)", 
                    value=f"R${valor_total:,.0f} mil".replace(",", "."), 
                    delta=f"{quantidade_total:,.0f} toneladas".replace(",", "."))

                st.metric(label=f"{menor_produtor} (Menor Produtor)",   
                    value=f"R${df_ano_filtered['VALOR'].min():,.0f} mil".replace(",", "."), 
                    delta=f"{df_ano_filtered['QUANTIDADE'].min():,.0f} toneladas".replace(",", "."))
            else:
                st.metric(label="Sem Dados", value="N/A", delta="N/A")

            # Exibição de rendimento médio
            if area_total > 0:
                st.markdown("##### Rendimento Médio")
                rendimento_kg_por_hectare = round(rendimento_medio, 2)
                st.metric(
                    label="Rendimento Médio (Kg/Hectare)",
                    value=f"{rendimento_kg_por_hectare} Kg/ha".replace(",", "."),
                    delta=f"{area_total:,.0f} hectares".replace(",", "."))
                
            else:
                st.metric(label="Rendimento Médio", value="N/A", delta="N/A")

            # Estilo customizado
            style_metric_cards(
                background_color="#000000",    
                border_left_color="#1E90FF",   # Azul Vivo
                border_color="#FFFFFF",        # Branco
                box_shadow="#4682B4"           # Azul Escuro
            )

        with col2:
            with open("data/geojs-es.json", "r", encoding="utf-8") as f:
                geojson_data = json.load(f)

            df_ano.dropna(subset=['VALOR'], inplace=True)

            m = folium.Map(location=[-20.3155, -40.3123], zoom_start=7, tiles="cartodb positron")

            min_valor, max_valor = df_ano['VALOR'].min(), df_ano['VALOR'].max()
            interval_range = (max_valor - min_valor) / 5
            intervals = [min_valor + i * interval_range for i in range(6)]

            Choropleth(
                geo_data=geojson_data,
                name="choropleth",
                data=df_ano,
                columns=["CIDADE", "VALOR"],
                key_on="feature.properties.name",
                fill_color="YlOrRd",
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name="Valor da Produção (Mil Reais)",
                threshold_scale=intervals
            ).add_to(m)

            marker_cluster = MarkerCluster().add_to(m)
            for _, row in df_ano.iterrows():
                popup_info = f"{row['CIDADE']}: R${row['VALOR']:.2f} mil<br>Quantidade: {row['QUANTIDADE']} toneladas<br>Área: {row['AREA']} hectares"
                folium.Marker(
                    location=[row['LATITUDE'], row['LONGITUDE']],
                    popup=popup_info
                ).add_to(marker_cluster)

            folium_static(m)
            st.write("<p style='font-size:13px;'>Fonte: IBGE</p>", unsafe_allow_html=True)

        with col3:
            st.markdown("##### Dados de Produção por Cidade")

            st.dataframe(
                df_ano,
                column_order=("CIDADE", "VALOR"),
                hide_index=True,
                use_container_width= True,
                column_config={
                    "CIDADE": st.column_config.TextColumn("Cidade"),
                    "VALOR": st.column_config.ProgressColumn(
                        "Valor da Produção (Mil Reais)",
                        format="R$%f",
                        min_value=0,
                        max_value=max(df_ano["VALOR"])
                    ),
                # "QUANTIDADE": st.column_config.ProgressColumn(
                    #    "Quantidade Produzida (Toneladas)",
                    #   format="%f",
                    #  min_value=0,
                    # max_value=max(df_ano["QUANTIDADE"])
                # ),
                
                }
            
            )
            st.write("<p style='font-size:13px;'>Fonte: IBGE</p>", unsafe_allow_html=True)
