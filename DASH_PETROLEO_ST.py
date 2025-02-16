import streamlit as st
import pandas as pd
import plotly.express as px

# Lista de opções de navegação
st.sidebar.markdown("### Etapas do projeto")

# Lista de seções com ícones
secoes = [
    "🚀 Contexto do Trabalho", 
    "🔍 Exploração e Insights", 
    "📊 Deploy", 
    "📌 Conclusão e Referências"
]

# Criando botões clicáveis e destacando o selecionado
for secao in secoes:
    if st.sidebar.button(secao, key=secao, help=f"Abrir {secao}"):
        st.session_state["pagina_selecionada"] = secao
    st.sidebar.empty()

# Seção ativa
menu = st.session_state.get("pagina_selecionada", "🚀 Contexto do Trabalho")

# Título principal
st.title("FIAP Pós Tech - Data Analytics")

### 🚀 SEÇÃO 1: CONTEXTO DO TRABALHO ###
if menu == "🚀 Contexto do Trabalho":
    abas = st.tabs(["Objetivo", "Metodologia"])
    
    with abas[0]:  # Aba Objetivo
        st.write("""
        O objetivo deste trabalho é analisar os dados históricos do preço do petróleo Brent, identificar padrões e tendências significativas, e desenvolver uma solução de previsão utilizando Machine Learning para prever os preços futuros. Além disso, busca-se fornecer insights sobre o impacto de fatores econômicos, geopolíticos e sociais nas oscilações desse mercado. 
        """)
    
    with abas[1]:  # Aba Metodologia
        st.write("""
        Para alcançar esse objetivo, coletamos os dados históricos do petróleo Brent e realizamos uma análise exploratória. Aplicamos um modelo de Machine Learning para previsão dos preços futuros, utilizando visualizações para comunicar os resultados. Desenvolvemos um dashboard interativo no Power BI e, por fim, implantamos a solução na plataforma Streamlit, permitindo uma interação intuitiva com os usuários.
        """)

### 🔍 SEÇÃO 2: EXPLORAÇÃO E INSIGHTS ###
elif menu == "🔍 Exploração e Insights":
    abas = st.tabs(["Modelo Prophet", "Análises Power BI", "Resultados"])

    with abas[0]:  # Aba Modelo Prophet
        st.write("""
        O modelo Prophet foi utilizado para realizar a previsão do preço do petróleo Brent. A partir dos dados históricos, ajustamos o modelo para prever os preços futuros, identificando tendências e sazonalidades que impactam os preços ao longo do tempo.
        """)

    with abas[1]:  # Aba Análises Power BI
        st.write("""
        No Power BI, foi realizado um estudo exploratório detalhado para identificar padrões e visualizar o comportamento do preço do petróleo Brent ao longo do tempo. Foram criados gráficos interativos que ilustram as tendências de mercado, sazonalidades e o impacto de eventos históricos no preço do petróleo.
        """)

        url_base = "https://raw.githubusercontent.com/flavioalmeeida/FIAP-TechChallange-2025-FASE4/main/"

        # Carregar imagens nas abas do Power BI
        st.image(f"{url_base}IMAGEM1_PB.png", caption="Análise Power BI - Gráfico 1", use_container_width=True)
        st.image(f"{url_base}IMAGEM2_PB.png", caption="Análise Power BI - Gráfico 2", use_container_width=True)
        st.image(f"{url_base}IMAGEM3_PB.png", caption="Análise Power BI - Gráfico 3", use_container_width=True)


    with abas[2]:  # Aba Resultados
        st.write("""
        Os resultados mostraram que o modelo de previsão tem uma boa capacidade de capturar as oscilações do preço do petróleo Brent. A análise também revelou como certos fatores geopolíticos e econômicos influenciam diretamente o valor do barril, além de identificar períodos críticos de alta e baixa.
        """)

### 📊 SEÇÃO 3: DEPLOY ###
elif menu == "📊 Deploy":
    abas = st.tabs(["Previsão"])

    with abas[0]:

        @st.cache_data
        def gerar_df():
            url = "https://raw.githubusercontent.com/flavioalmeeida/FIAP-TechChallange-2025-FASE4/ec795cc24b07cdb2d3ac5cd0c427c5fa1ba14d2d/DADOS_PETROLEO_ST.xlsx"
            df = pd.read_excel(io=url, engine="openpyxl", sheet_name="Sheet1", usecols="A:C", nrows=11345)
            return df

        df = gerar_df()

        # Seleção de intervalo de datas
        data_selecionada = st.date_input(
            "Escolha o intervalo de datas para visualizar:",
            value=[df["data"].min(), df["data"].max()],
            min_value=df["data"].min(),
            max_value=df["data"].max()
        )

        if len(data_selecionada) == 2:
            data_inicial, data_final = pd.to_datetime(data_selecionada[0]), pd.to_datetime(data_selecionada[1])
            df_filtrado = df[(df["data"] >= data_inicial) & (df["data"] <= data_final)]

            st.write(f"Exibindo dados de **{data_inicial.strftime('%d/%m/%Y')}** até **{data_final.strftime('%d/%m/%Y')}**.")

            fig = px.line(df_filtrado, x="data", y=["y", "y_pred"], labels={"value": "Valor (US$)", "data": "Data"},
                        title="Projeção vs Valor Real do Barril de Petróleo")
            st.plotly_chart(fig)

            if not df_filtrado.empty:
                valor_pred_mais_recente = df_filtrado["y_pred"].iloc[-1]
                st.metric(label=f"Última projeção no intervalo selecionado ({data_final.strftime('%d/%m/%Y')})",
                          value=f"{valor_pred_mais_recente:.2f} US$")
        else:
            st.write("Selecione um intervalo completo para visualizar os dados filtrados.")
            fig = px.line(df, x="data", y=["y", "y_pred"], labels={"value": "Valor (US$)", "data": "Data"},
                          title="Projeção Completa do Valor do Barril de Petróleo")
            st.plotly_chart(fig)

### 📌 SEÇÃO 4: CONCLUSÃO E REFERÊNCIAS ###
elif menu == "📌 Conclusão e Referências":
    abas = st.tabs(["Conclusão", "Referências"])

    with abas[0]:  # Conclusão
        st.write("Resumo final do estudo.")

    with abas[1]:  # Referências
        st.write("Lista de fontes utilizadas no estudo.")

# Adicionando os nomes dos participantes no final do menu lateral
st.sidebar.markdown("### Participantes")
st.sidebar.write("Flávio Almeida e Silva - RM357571")
st.sidebar.write("Matheus Matos Ferreira - RM357244")
st.sidebar.write("Hercules Alves Sodré   - RM354814")

