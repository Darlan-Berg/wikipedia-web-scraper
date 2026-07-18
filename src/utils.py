import requests as reqs
import re

class WkUrlNotFound(Exception):
    """Exceção lançada quando a requisição a uma URL da Wikipédia falha.
    A exceção armazena o código de status HTTP e a URL que retornou erro.
    """

    def __init__(self, resp: reqs):
        self.status_code = resp.status_code
        self.url = resp.url
        self.message = f"""
        Erro: URL {self.url} não existe.
        Código do status de resposta da requisição: {self.status_code}.
        """
        super().__init__(self.message)
    
    def __str__(self):
        return self.message

def wk_url_validate(url: str):
    """Usa Regex para validar uma URL da Wikipedia, retornando True ou False.
    """

    wk_url_regex = r'https?://pt\.wikipedia\.org/wiki/([^:#"\s]+)'
    return (re.search(wk_url_regex, url) is not None)


def download_page(url: str):
    """Faz uma requisição GET para a URL informada. Se o status de resposta não
    estiver na faixa 2xx, lança WkUrlNotFound.
    Retorna um objeto Response.
    """

    headers = { "User-Agent": "WebScraper/1.0" }
    resp = reqs.get(url, headers=headers)

    if (resp.status_code < 200 or resp.status_code >= 300):
        raise WkUrlNotFound(resp)
    
    return resp
