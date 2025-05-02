import streamlit as st

# Configuração da página
st.set_page_config(page_title="Currículo Pedro Chaves", layout="wide")

# Barra lateral
st.sidebar.title("Navegação")
pages = st.sidebar.selectbox("Escolha a seção:", [
    "Quem sou eu?",
    "Formação e Experiências Profissionais",
    "Skills"
])

st.sidebar.markdown("""---""")
st.sidebar.markdown("""
Desenvolvido por **Pedro Chaves**

[Github](https://github.com/P4Chaves)  
[LinkedIn](https://www.linkedin.com/in/pedro-chaves-480056290/)
""")

# Páginas
if pages == "Quem sou eu?":
    st.image("code.png", width=600)
    st.header("Quem sou eu?")
    st.subheader("Pedro Henrique Nardaci Chaves — 19 anos")
    st.write("""
    - Aluno da **Faculdade de Informática e Administração Paulista (FIAP)**, cursando **Engenharia de Software**.
    - Interesse em oportunidades internacionais, com o objetivo de **trabalhar fora do país** e explorar novas experiências profissionais.
    - Especialização em **Back-end**, com conhecimentos em diversas tecnologias.
    """)

elif pages == "Formação e Experiências Profissionais":
    st.image("experiences.png", width=600)
    st.header("Formação e Experiências Profissionais")
    st.write("""
    ### Formação Acadêmica:
    - Engenharia de Software na **FIAP** (Faculdade de Informática e Administração Paulista).

    ### Experiência Profissional:
    - Ainda sem experiência profissional formal.

    ### Projetos Acadêmicos:
    - Participação na **Global Solutions da FIAP**, desenvolvendo **websites e aplicativos** para empresas reais.
    - Durante os quatro primeiros semestres, atuei na **criação e apresentação de soluções** para **duas empresas**, aplicando conhecimentos práticos e inovadores.

    ### Certificados:
    - Diversos certificados em **programação** e **soft skills** obtidos através de **Nano-Courses da FIAP** e **Alura**.
    """)

elif pages == "Skills":
    st.image("skills.png", width=400)
    st.header("Skills")
    st.write("""
    ### Hard Skills:
    - Especialização em **Back-end**
    - Linguagens de programação: **Python, Java, JavaScript**
    - Banco de Dados: **MySQL, PostgreSQL**
    - Ferramentas: **Git, Docker, APIs REST**

    ### Soft Skills:
    - **Comunicativo**, com facilidade para expressar ideias e trabalhar em equipe.
    - **Bom em equipes**, sabendo colaborar e ouvir diferentes perspectivas.
    - **Eficiente com tempo**, com boa organização e entrega dentro de prazos.

    ### Idiomas:
    - **Fluente em inglês**, certificado pelo **MET (Michigan English Test)**.
    """)

