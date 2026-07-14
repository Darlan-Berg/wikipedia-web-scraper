import re

def get_table_of_contents(html_content: str) -> list[str]:
    """Extrai os títulos de seções (h2-h6) do conteúdo HTML.
    Retorna uma lista com os títulos das seções, apenas o texto limpo.
    """

    pattern = r'<h[2-6][^>]*>(.*?)</h[2-6]>'

    content = re.findall(pattern, html_content, re.DOTALL)
    table_of_contents = [re.sub(r'<[^>]+>', '', c).strip() for c in content]

    return table_of_contents

def get_image_filenames(html_content: str) -> list[str]:
    """Extrai nomes de arquivos de imagem do conteúdo HTML.
    Retorna lista com nomes únicos dos arquivos de imagem encontrados.
    """
    pattern = r'src="[^"]*/([^/"\s]+\.(?:jpg|jpeg|png|svg|gif|webp))'

    filenames = re.findall(pattern, html_content, re.IGNORECASE)

    return list(set(filenames))

def get_wikipedia_links(html_content: str) -> list[str]:
    """Extrai links para artigos da Wikipédia do conteúdo HTML.
    Retorna lista com URLs únicas de artigos encontrados no formato https://dominio/wiki/artigo.
    """
    pattern = r'href="(?:https?:)?//(\w+\.wikipedia\.org)/wiki/([^:#"\s]+)"'

    content = re.findall(pattern, html_content)
    links = list(set(content))

    return [f"https://{dominio}/wiki/{artigo}" for dominio, artigo in links]

def get_aria_labels(html_content: str) -> list[str]:
    """Extrai os textos dos atributos aria-label do conteúdo HTML.
    Retorna uma lista com todos os textos de aria-labels encontrados.
    """
    pattern = r'aria-label="([^"]*)"'
    return re.findall(pattern, html_content)

def get_alt_text(html_content: str) -> list[str]:
    """Extrai os textos alternativos (atributos alt) do conteúdo HTML.
    Retorna uma lista com todos os textos alternativos encontrados.
    """
    pattern = r'alt="([^"]*)"'
    return re.findall(pattern, html_content)
