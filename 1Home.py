import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *

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
    st.write("""
    - **Pedro Henrique Nardaci Chaves**
    - Aluno da **Faculdade de Informática e Administração Paulista (FIAP)**, atualmente cursando **Engenharia de Software**.
    - Interesse em oportunidades internacionais, com o objetivo de **trabalhar fora do país** e explorar novas experiências profissionais.
    - Especialização em **Back-end**, com conhecimentos em diversas tecnologias.
    """)

elif pages == "Formação e Experiências Profissionais":
    st.image("code.png", width=600)
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
    st.image("code.png", width=600)
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
    st.write("Faça upload do seu arquivo Excel para analisar a distribuição de uma variável numérica.")
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel", type=["xlsx", "xls"])
    
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
                
                dist = st.selectbox("Escolha a distribuição para análise:", ["Poisson", "Normal", "Binomial"])
                
                if dist == "Poisson":
                    lambda_est = df[coluna_escolhida].mean()
                    x = np.arange(0, 2 * lambda_est)
                    y = stats.poisson.pmf(x, lambda_est)
                    st.write("Distribuição de Poisson")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)
                
                elif dist == "Normal":
                    mu_est = df[coluna_escolhida].mean()
                    sigma_est = df[coluna_escolhida].std()
                    x = np.linspace(mu_est - 4*sigma_est, mu_est + 4*sigma_est, 100)
                    y = stats.norm.pdf(x, mu_est, sigma_est)
                    st.write("Distribuição Normal")
                    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
                    st.plotly_chart(fig)
                
                elif dist == "Binomial":
                    n = 10  # número de tentativas fixo
                    p = df[coluna_escolhida].mean() / max(df[coluna_escolhida])
                    x = np.arange(0, n + 1)
                    y = stats.binom.pmf(x, n, p)
                    st.write("Distribuição Binomial")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)
