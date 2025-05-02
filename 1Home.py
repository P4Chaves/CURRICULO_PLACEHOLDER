import streamlit as st
import base64
import os

# Configuração da página
st.set_page_config(
    page_title="Currículo Pedro Chaves",
    layout="wide",
    page_icon="📄",
    initial_sidebar_state="expanded"
)

# Custom CSS para as cores e estilo
st.markdown("""
    <style>
        body {
            background-color: #1C1C1C;
            color: #F5F5F5;
        }
        .block-container {
            padding-top: 2rem;
        }
        h1, h2, h3 {
            color: #1F4E79;
        }
        .stTabs [role="tablist"] {
            background-color: #2A2A2A;
        }
        .stTabs [role="tab"] {
            color: #F5F5F5;
        }
        .stTabs [role="tab"][aria-selected="true"] {
            background-color: #1F4E79;
        }
        .sidebar .sidebar-content {
            background-color: #2A2A2A;
        }
    </style>
""", unsafe_allow_html=True)

# Função para exibir PDF na tela (bem maior)
def mostrar_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Função para botão de download
def botao_download(file_path, label):
    with open(file_path, "rb") as f:
        st.download_button(
            label=label,
            data=f,
            file_name=os.path.basename(file_path),
            mime="application/pdf"
        )

# Abas principais
abas = st.tabs([
    "Quem sou eu?",
    "Formação e Experiências Profissionais",
    "Skills",
    "Certificados"
])

# Aba 1 — Quem sou eu
with abas[0]:
    st.image("code.png", width=600)
    st.header("Quem sou eu?")
    st.header("**Pedro Henrique Nardaci Chaves - 19 anos**")
    st.write("""
    - Aluno da **Faculdade de Informática e Administração Paulista (FIAP)**, atualmente cursando **Engenharia de Software**.
    - Interesse em oportunidades internacionais, com o objetivo de **trabalhar fora do país** e explorar novas experiências profissionais.
    - Especialização em **Back-end**, com conhecimentos em diversas tecnologias.
    """)

# Aba 2 — Formação e Experiências Profissionais
with abas[1]:
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

# Aba 3 — Skills
with abas[2]:
    st.image("skills.png", width=400)
    st.header("Skills")
    st.write("""
    - **Hard Skills:**
        - Adequado para ambos **Front** e **Back-end**
        - Linguagens de programação: **Python, Java, JavaScript**
        - Banco de Dados: **MySQL**
        - Ferramentas: **Github**
    - **Soft Skills:**
        - **Comunicativo**, com facilidade para expressar ideias e trabalhar em equipe.
        - **Bom em equipes**, sabendo colaborar e ouvir diferentes perspectivas.
        - **Eficiente com tempo**, com boa organização e entrega dentro de prazos.
    - **Idiomas:**
        - **Fluente em inglês**, certificado pelo **MET (Michigan English Test)**.
    """)

# Aba 4 — Certificados com visualização grande + botão de download
with abas[3]:
    st.header("Certificados")
    st.write("Clique para visualizar e/ou baixar seus certificados:")

    certificados = [
        ("AlgoritmosCertificado.pdf", "Algoritmos"),
        ("DesignThinkingCertificado.pdf", "Design Thinking"),
        ("FormacaoSocialCertificado.pdf", "Formação Social"),
        ("GestaoInfraCertificado.pdf", "Gestão de Infraestrutura"),
        ("OracleDatabaseCertificado.pdf", "Oracle Database"),
        ("Pedro Chaves - MET Certificate.pdf", "MET (Inglês)")
    ]

    for arquivo, titulo in certificados:
        st.subheader(f"📄 {titulo}")
        col1, col2 = st.columns([7, 1])
        with col1:
            mostrar_pdf(arquivo)
        with col2:
            botao_download(arquivo, f"⬇️ Baixar certificado")

# Rodapé no sidebar
st.sidebar.markdown("""Desenvolvido por Pedro Chaves  

[GitHub](https://github.com/P4Chaves)  
[LinkedIn](https://www.linkedin.com/in/pedro-chaves-480056290/)
""")
