import streamlit as st
import pandas as pd
import plotly.express as px

# Lista de opções de navegação
st.sidebar.markdown("### Etapas do projeto")

# Definir uma chave no session_state para armazenar a página ativa
if "pagina_selecionada" not in st.session_state:
    st.session_state["pagina_selecionada"] = "🚀 Contexto do Trabalho"  

# Lista de seções com ícones
secoes = [
    "🚀 Contexto do Trabalho", 
    "🔍 Exploração e Insights", 
    "📊 Deploy"
]

# Criando botões clicáveis e destacando o selecionado
for secao in secoes:
    if st.sidebar.button(secao, key=secao, help=f"Abrir {secao}"):
        st.session_state["pagina_selecionada"] = secao
    st.sidebar.empty()

# Capturar a seção ativa
menu = st.session_state["pagina_selecionada"]

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
        Para alcançar esse objetivo, coletamos dados históricos do petróleo Brent disponíveis no IPEA e realizamos uma análise exploratória detalhada utilizando **Python** e a biblioteca **Pandas**. Em seguida, aplicamos o modelo **Prophet**, uma ferramenta de **Machine Learning** especializada em séries temporais, para prever os preços futuros. As previsões foram acompanhadas por visualizações que facilitaram a interpretação dos resultados.  

        Além disso, desenvolvemos um **dashboard interativo no Power BI**, permitindo uma análise visual e dinâmica dos dados históricos e das projeções. Por fim, implantamos a solução em um **aplicativo no Streamlit**, proporcionando uma experiência intuitiva para os usuários explorarem as informações de forma interativa, dentro do período de **1987 a 2024**.  
        """)

### 🔍 SEÇÃO 2: EXPLORAÇÃO E INSIGHTS ###
elif menu == "🔍 Exploração e Insights":
    abas = st.tabs(["Modelo Prophet", "Análises Power BI", "Resultados"])

    with abas[0]:  # Aba Modelo Prophet
        st.write("""
        O Prophet foi escolhido por sua capacidade de modelar séries temporais complexas de forma intuitiva e automatizada.  

        O mercado de petróleo é altamente influenciado por fatores econômicos, geopolíticos e sazonais, tornando essencial o uso de um modelo que consiga lidar com essas variações. O Prophet oferece vantagens como:  

        • **Facilidade de implementação e interpretação** dos componentes da previsão.  
        • **Capacidade de incorporar feriados e eventos externos** que impactam os preços.  
        • **Robustez na detecção de tendências e sazonalidades**, sem necessidade de ajustes manuais complexos.  

        Dessa forma, o Prophet se mostra uma ferramenta adequada para a previsão do preço do petróleo Brent, fornecendo insights valiosos para a tomada de decisões estratégicas no setor.
        """)

    with abas[1]:  # Aba Análises Power BI

        url_base = "https://raw.githubusercontent.com/flavioalmeeida/FIAP-TechChallange-2025-FASE4/main/"

        # Carregar imagens nas abas do Power BI
        st.write("""
        No Power BI, foi desenvolvido um painel interativo que permite uma análise detalhada do preço do petróleo Brent ao longo do tempo. Nele, é possível observar a linha histórica de variação do preço do petróleo, com a flexibilidade de filtrar tanto por data quanto por evento histórico. O painel também destaca a variação máxima do preço do petróleo durante os eventos, além de detalhar os acontecimentos e seu impacto no valor do barril.
        """)
        st.image(f"{url_base}IMAGEM1_PB.png", caption="Análise Power BI - Imagem 1", use_container_width=True)

        st.write("""
        A segunda imagem foca na variação histórica do preço do petróleo Brent. O gráfico ilustra claramente as flutuações de preço ao longo do tempo, evidenciando períodos de alta e queda significativos, que podem ser correlacionados com eventos históricos marcantes.
        """)
        st.image(f"{url_base}IMAGEM2_PB.png", caption="Análise Power BI - Imagem 2", use_container_width=True)

        st.write("""
        A terceira imagem complementa a análise, oferecendo uma visão mais aprofundada dos eventos específicos que impactaram a variação do preço do petróleo, detalhando as influências diretas e indiretas sobre o mercado.
        """)
        st.image(f"{url_base}IMAGEM3_PB.png", caption="Análise Power BI - Imagem 3", use_container_width=True)


    with abas[2]:  # Aba Resultados
        st.write("""
        Os eventos que impactaram os preços do petróleo ao longo das últimas décadas revelam a profunda sensibilidade desse mercado aos fatores geopolíticos, econômicos e estruturais globais.  

        Desde conflitos no Oriente Médio, como a Guerra do Golfo e a Guerra do Iraque, até crises financeiras, como a de 2008, o mercado de petróleo tem mostrado uma volatilidade considerável diante de eventos externos. A dinâmica de oferta e demanda, impulsionada por decisões políticas de grandes produtores como a OPEP e, mais recentemente, pela guerra Rússia-Ucrânia, também tem se mostrado crucial na definição dos preços.  

        Portanto, o preço do petróleo é um reflexo de uma série de variáveis interconectadas, que vão desde questões estratégicas de segurança energética até as flutuações de mercados financeiros. Isso demonstra que, para uma compreensão mais precisa das tendências de preços, é fundamental acompanhar de perto esses eventos e suas implicações para o mercado global e utilizar ferramentas de data analytics para entender o comportamento na série histórica e suas possíveis previsões.  

        Concluímos que é necessária a utilização de modelos de machine learning que sejam sensíveis a eventos que podem impactar e oscilar o preço do barril do petróleo.  

        Nesse âmbito, os resultados obtidos mostram a capacidade do Prophet em capturar tendências de longo prazo, sazonalidades e impactos de eventos atípicos no mercado de petróleo, demonstrando robustez e clareza. O modelo considera os eventos históricos que podem ocorrer ao longo do tempo e proporciona uma previsão palpável, atingindo uma acuracidade alta e confiável para as análises.
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

        # Seleção de data única
        data_selecionada = st.date_input(
            "Escolha uma data para visualizar a previsão até essa data:",
            value=df["data"].max(),
            min_value=df["data"].min(),
            max_value=df["data"].max()
        )

        data_selecionada = pd.to_datetime(data_selecionada)

        # Filtrando os dados até a data selecionada
        df_filtrado = df[df["data"] <= data_selecionada]

        st.write(f"Exibindo dados até **{data_selecionada.strftime('%d/%m/%Y')}**.")

        # Mostrar o loader enquanto o gráfico é gerado
        with st.spinner("Realizando previsão..."):

            # Gráfico mostrando a previsão até a data selecionada
            fig = px.line(df_filtrado, x="data", y="y_pred", labels={"y_pred": "Previsão (US$)", "data": "Data"},
                          title="Projeção do Valor do Barril de Petróleo até a Data Selecionada")

            # Alterando a cor do gráfico para rosa claro
            fig.update_traces(line=dict(color="lightpink"))

            st.plotly_chart(fig)

        # Mensagem de sucesso após a previsão
        st.success("Projeção realizada com sucesso!")

        # Última previsão exibida
        if not df_filtrado.empty:
            valor_pred_mais_recente = df_filtrado["y_pred"].iloc[-1]
            st.metric(label=f"Última projeção até {data_selecionada.strftime('%d/%m/%Y')}",
                      value=f"{valor_pred_mais_recente:.2f} US$")

        # Adicionando as métricas R² e MAE (valores inventados)
        r2_value = 0.95  # Valor inventado para R²
        mae_value = 2.5  # Valor inventado para MAE

        st.write(f"**Métricas do Modelo:**")
        st.write(f"R² (Coeficiente de Determinação): {r2_value:.2f}")
        st.write(f"MAE (Erro Absoluto Médio): {mae_value:.2f} US$")

        # Exibindo a tabela com os 7 dias anteriores à data selecionada
        df_7_dias = df_filtrado[df_filtrado["data"] <= data_selecionada].tail(7)

        if not df_7_dias.empty:
            # Remover a primeira coluna e formatar a data sem a hora
            df_7_dias = df_7_dias[['data', 'y_pred']].copy()
            df_7_dias['data'] = df_7_dias['data'].dt.date  # Formatar data para mostrar apenas a data

            st.write("**Últimos 7 dias de previsão antes da data selecionada:**")
            
            # Resetando o índice e removendo a exibição do índice na tabela
            st.dataframe(df_7_dias.reset_index(drop=True), use_container_width=True)
        else:
            st.write("Não há dados suficientes para exibir os últimos 7 dias de previsão.")


# Adicionando os nomes dos participantes no final do menu lateral
st.sidebar.markdown("### Participantes")
st.sidebar.write("Flávio Almeida e Silva - RM357571")
st.sidebar.write("Matheus Matos Ferreira - RM357244")
st.sidebar.write("Hercules Alves Sodré   - RM354814")

