import streamlit as st
from utils import wk_url_validate, download_page, WkUrlNotFound
from scraper import get_wikipedia_links, get_image_filenames, get_table_of_contents, get_aria_labels, get_alt_text

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

    options = [
        "Tópicos de índice do artigo", 
        "Nomes de arquivos e imagens", 
        "Links para outros artigos da Wikipedia",
        "Textos alternativos de imagens",
        "Etiquetas de acessibilidade"
        ]
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

if st.session_state.show_results:
    # Iterar pelas opções selecionadas
    for option in slct_options:
        match option:

            case "Tópicos de índice do artigo":
                with st.expander("Tópicos de índice do artigo", expanded=False):
                    # Iterar pelos tópicos da página
                    html_list = '<ol style="word-break: break-all">'
                    for topic in get_table_of_contents(html_code):
                        html_list += f"<li>{topic}</li>"
                    html_list += "</ol>"
                    st.write(html_list, unsafe_allow_html=True)

            case "Nomes de arquivos e imagens":
                with st.expander("Nomes de arquivos e imagens", expanded=False):
                    # Iterar pelos nomes de arquivos de imagem
                    html_list = '<ol style="word-break: break-all">'
                    for img_file_name in get_image_filenames(html_code):
                        html_list += f"<li>{img_file_name}</li>"
                    html_list += "</ol>"
                    st.write(html_list, unsafe_allow_html=True)
            
            case "Links para outros artigos da Wikipedia":
                with st.expander("Links para outros artigos da Wikipedia", expanded=False):
                    # Iterar pelos links da Wikipedia
                    html_list = '<ol style="word-break: break-all">'
                    for link in get_wikipedia_links(html_code):
                        html_list += f"<li>{link}</li>"
                    html_list += "</ol>"
                    st.write(html_list, unsafe_allow_html=True)
            
            case "Textos alternativos de imagens":
                with st.expander("Textos alternativos de imagens", expanded=False):
                    # Iterar pelos textos alternativos
                    html_list = '<ol style="word-break: break-all">'
                    for alt_text in get_alt_text(html_code):
                        html_list += f"<li>{alt_text}</li>"
                    html_list += "</ol>"
                    st.write(html_list, unsafe_allow_html=True)
            
            case "Etiquetas de acessibilidade":
                with st.expander("Etiquetas de acessibilidade", expanded=False):
                    # Iterar pelos rótulos de acessibilidade
                    html_list = '<ol style="word-break: break-all">'
                    for aria_label in get_aria_labels(html_code):
                        html_list += f"<li>{aria_label}</li>"
                    html_list += "</ol>"
                    st.write(html_list, unsafe_allow_html=True)