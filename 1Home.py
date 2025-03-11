import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go
 
# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")
 
# Criando as sub-abas (pages)
pages = st.sidebar.selectbox("Escolha a sua seção:", [
    "Quem sou eu?",
    "Formação e Experiências Profissionais",
    "Skills",
    "Análise de Dados"
])
 
st.sidebar.markdown("Desenvolvido por Pedro Henrique Nardaci Chaves")
 
if pages == "Quem sou eu?":
    st.image("code.png", width=600)
    st.header("Quem sou eu?")
    st.header("**Pedro Henrique Nardaci Chaves - 19 anos**")
    st.write("""
    - Aluno da **Faculdade de Informática e Administração Paulista (FIAP)**, atualmente cursando **Engenharia de Software**.
    - Interesse em oportunidades internacionais, com o objetivo de **trabalhar fora do país** e explorar novas experiências profissionais.
    - Especialização em **Back-end**, com conhecimentos em diversas tecnologias.
    """)
 
elif pages == "Formação e Experiências Profissionais":
    st.image("experiences.png", width=600)
    st.header("Formação e Experiências Profissionais")
    st.write("""
    - **Formação Acadêmica:**
        - Engenharia de Software na **FIAP** (Faculdade de Informática e Administração Paulista).
    - **Experiência Profissional:**
        - Ainda sem experiência profissional formal.
    - **Projetos Acadêmicos:**
        - Participação na **Global Solutions da FIAP**, desenvolvendo **websites e aplicativos** para empresas reais.
        - Durante os quatro primeiros semestres, atuei na **criação e apresentação de soluções** para **duas empresas**, aplicando conhecimentos práticos e inovadores.
    - **Certificados:**
        - Diversos certificados em **programação** e **soft skills** obtidos através de **Nano-Courses da FIAP** e **Alura**.
    """)
 
elif pages == "Skills":
    st.image("skills.png", width=400)
    st.header("Skills")
    st.write("""
    - **Hard Skills:**
        - Especialização em **Back-end**
        - Linguagens de programação: **Python, Java, JavaScript**
        - Banco de Dados: **MySQL, PostgreSQL**
        - Ferramentas: **Git, Docker, APIs REST**
    - **Soft Skills:**
        - **Comunicativo**, com facilidade para expressar ideias e trabalhar em equipe.
        - **Bom em equipes**, sabendo colaborar e ouvir diferentes perspectivas.
        - **Eficiente com tempo**, com boa organização e entrega dentro de prazos.
    - **Idiomas:**
        - **Fluente em inglês**, certificado pelo **MET (Michigan English Test)**.
    """)
 
elif pages == "Análise de Dados":
    st.header("Análise de Dados")
    st.header("**Problema: Queda no engajamento no canal do Youtube.**")
    st.write("**Análise Inicial**: Os dados indicam que o canal pode estar enfrentando uma queda de engajamento, e para entender melhor essa situação, podemos observar algumas métricas principais.")
    st.write("**Engajamento ao longo do tempo**: Podemos verificar se visualizações, likes e comentários diminuíram ao longo dos meses.")
    st.write("**Fatores que influenciam o engajamento**: Podemos analisar se vídeos com maior tempo assistido ou maior taxa de cliques (CTR) recebem mais interações.")
    st.write("**Padrões e sazonalidade**: Podemos identificar se há dias ou horários que impactam o desempenho dos vídeos.")
    st.write("**Retenção e duração dos vídeos**: Podemos verificar se vídeos mais curtos ou longos tendem a ter melhor desempenho.")
    st.write("**Com o upload do arquivo Excel, será possível analisar cada um desses padrões de forma estatística.**")
    uploaded_file = st.file_uploader("Carregue o arquivo Excel", type=["xlsx", "xls"])
   
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Amostra dos dados:")
        st.write(df.head())
       
        colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
        if colunas_numericas:
            coluna_escolhida = st.selectbox("Escolha uma coluna numérica:", colunas_numericas)
           
            if coluna_escolhida:
                st.write("Distribuição dos dados:")
                st.write(df[coluna_escolhida].describe())
               
                st.write("""
                Escolhemos duas distribuições para análise:
                - **Distribuição Normal**: útil para dados contínuos e que seguem um padrão simétrico em torno da média.
                - **Distribuição Binomial**: apropriada para modelar sucessos e falhas em eventos discretos.
                """)
               
                dist = st.selectbox("Escolha a distribuição para análise:", ["Normal", "Binomial"])
               
                if dist == "Normal":
                    mu_est = df[coluna_escolhida].mean()
                    sigma_est = df[coluna_escolhida].std()
                    x = np.linspace(mu_est - 4*sigma_est, mu_est + 4*sigma_est, 100)
                    y = stats.norm.pdf(x, mu_est, sigma_est)
                    st.write("Distribuição Normal")
                    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
                    st.plotly_chart(fig)
                    st.write("""
                    A **Distribuição Normal** nos ajuda a identificar padrões gerais de variação no engajamento do canal.
                    Podemos determinar se os dados estão concentrados em torno de um valor médio e analisar possíveis desvios.
                    """)
               
                elif dist == "Binomial":
                    n = 10  # número de tentativas fixo
                    p = df[coluna_escolhida].mean() / max(df[coluna_escolhida])
                    x = np.arange(0, n + 1)
                    y = stats.binom.pmf(x, n, p)
                    st.write("Distribuição Binomial")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)
                    st.write("""
                    A **Distribuição Binomial** é útil para modelar o número de sucessos (ex: número de vídeos que atingem um certo nível de engajamento).
                    Ajuda a entender as chances de sucesso e prever padrões futuros.
                    """)
