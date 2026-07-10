import streamlit as st
from utils import wk_url_validate, download_page, WkUrlNotFound
from scraper import get_wikipedia_links, get_image_filenames, get_table_of_contents

st.set_page_config(
    page_title="Wikipedia Web Scraper",
    page_icon="📚"
)

# Muda o valor da variável de sessão "show_results" para 
# que o conteúdo da página requisitada seja mostrado.
def show_results():
    st.session_state.show_results = True

if "show_results" not in st.session_state:
    st.session_state.show_results = False

st.markdown(
"""
<header>
        <b>Atividade Prática Supervisionada 1 - 19/07/2026</b><br>
        Centro de Informática - UFPB<br>
        Curso: Ciência da Computação<br>
        Disciplina: Linguagens Formais e Computabilidade - Prof. Dr. Bruno Bruck
<header>
""",
    unsafe_allow_html=True
)

st.title("Wikipedia Web Scraper")
st.caption("Por Darlan Berg e Gabriela Marques Mangueira")

# Formulário
with st.form(key="url_form"):

    url = st.text_input("Digite uma URL da Wikipedia")
    validated_url = wk_url_validate(url)

    options = ["Tópicos de índice do artigo", "nomes de arquivos e imagens", "Links para outros artigos da Wikipedia"]
    slct_options = st.multiselect(
        "Selecione o que buscar na página.",
        options = options,
        placeholder="Nenhum"
    )

    sbmt_button = st.form_submit_button(label="Buscar")

    if not validated_url:
        st.warning("A URL não possui a estrutura de uma página da Wikipedia.")
    if not slct_options:
        st.warning("É preciso selecionar ao menos uma opção.")
    elif validated_url and slct_options:
        # A partir desse ponto resta fazer a requisição do HTML da página
        try:
            wk_page = download_page(url)
            html_code = wk_page.content.decode("utf-8")
            show_results()
            st.success("Formulário submetido com sucesso.")

        except WkUrlNotFound as e:
            st.write(e)

# Parte dos resultados da busca (por enquanto retorna apenas HTML)
if st.session_state.show_results:
    print("topicos: ", get_table_of_contents(html_code))
    print("\nimagens:", get_image_filenames(html_code))
    print("\nlinks:", get_wikipedia_links(html_code))
    st.header("Resultados da Busca")
    st.code(html_code, language="html")
