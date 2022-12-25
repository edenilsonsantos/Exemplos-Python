# exemplos para usar com requests.

import requests
import re

############### PESQUISAR NO GOOGLE E OBTER OS LINKS DE PÁGINAS REFERENTE A BUSCA ##########
def pesquisa_google(busca):
    res = requests.get(url=f'https://www.google.com/search?q={busca}')
    links = re.findall('(https://.*?"><)', res.text)
    links = [x for x in links if not 'google' in x ]
    new_links = []
    print(len(links), ' links de resultado\n')

    for link in links:
        link = re.sub('"><.*|<.*','', link)
        link = link.split('&')[0]
        link = link.split()[0]
        new_links.append(link)
        print(link)
    print()
    return new_links
     
pesquisa_google('presidente do brasil')

############### LOGIN EM SITE COM REQUESTS, E DEPOIS PEGAR TABELA NOUTRA URL DO MESMO SITE ##########
# EM BREVE...
