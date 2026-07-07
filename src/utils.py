import requests as reqs

class WikipediaBaseUrlError(Exception):
    def __init__(self):
        self.message = "URL não possui a estrutura de uma página da Wikipedia."
        super().__init__(self.message)
    
    def __str__(self):
        return self.message

class WikipediaUrlNotFound(Exception):
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
    