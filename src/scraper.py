import re

def get_table_of_contents(html_content):

    pattern = r'<h[2-6][^>]*>(.*?)</h[2-6]>'

    content = re.findall(pattern, html_content, re.DOTALL)
    table_of_contents = [re.sub(r'<[^>]+>', '', c).strip() for c in content]

    return table_of_contents

def get_image_filenames(html_content):

    pattern = r'src="[^"]*/([^/"\s]+\.(?:jpg|jpeg|png|svg|gif|webp))'

    filenames = re.findall(pattern, html_content, re.IGNORECASE)

    return list(set(filenames))

def get_wikipedia_links(html_content):
    
    pattern = r'href="(?:https?:)?//(\w+\.wikipedia\.org)/wiki/([^:#"\s]+)"'

    content = re.findall(pattern, html_content)
    links = list(set(content))

    return [f"https://{dominio}/wiki/{artigo}" for dominio, artigo in links]