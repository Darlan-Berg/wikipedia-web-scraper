import requests as reqs
import re
from utils import WikipediaBaseUrlError, WikipediaUrlNotFound

"""
A função download_html:
    1) Usa Regex para verificar se a URL passada como parâmetro é válida;
    2) Faz a requisição do HTML da página da Wikipedia;
    3) Retorna o conteúdo da requisição.
"""
def download_html(url: str):
    wikipedia_regex = "^(https://pt.wikipedia.org/)(\\w*)|^(https://pt.wikipedia.org/?)"

    if not (re.search(wikipedia_regex, url)):
        raise WikipediaBaseUrlError
    
    headers = { "User-Agent": "WebScraper/1.0" }
    resp = reqs.get(url, headers=headers)

    if (resp.status_code == 404):
        raise WikipediaUrlNotFound(resp)
    
    return resp.text
