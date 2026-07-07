from utils import WikipediaBaseUrlError, WikipediaUrlNotFound
from downloader import download_html

try:
    # Altere a URL para testar as classes de erro
    url = "https://pt.wikipedia.org/wiki/Super_Mario_Odyssey"
    page = download_html(url)
    print(page)

except WikipediaBaseUrlError as e:
    print(e)

except WikipediaUrlNotFound as e:
    print(e)
