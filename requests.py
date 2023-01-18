# exemplos para usar com requests.

import requests
requests.packages.urllib3.disable_warnings()
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


############### LOGIN EM SITE COM REQUESTS, E DEPOIS LER HTML DE OUTRA URL DO MESMO SITE ##########
# Exemplo de realizar login no site via post com requests, e guardar a sessao
# em seguida acessar outra url do site com a sessão autenticada.

usuario = 'demo'
senha = 'demo'
url_login = 'https://demo.owncloud.org/login'

##### Armazenar sessao de login
minha_Session = requests.Session() 
autenticacao = {'user': usuario, 'password': senha}
minha_Session.post(url_login, data=autenticacao)

##### Usar a sessao para acessar outra url da página, autenticando com o cookie
url_page = 'https://demo.owncloud.org/apps/files/?dir=/'
page = minha_Session.get(url_page)
print(page.content)



####################################################################
######################## LIB REQUESTS-HTML #########################
# pip install requests-html

import os
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# <input type="hidden" name="requesttoken" value="Tik6cy1DKj8/PhZAX1I8GVkMNhstJB4RGiwgGQotHTQ=:wNc0X0ctZYb576JUiGZTCBUhwaQSbzvmo78p+BmkPGo=">

with HTMLSession() as c:

    url = 'https://demo.owncloud.org/login'
    USERNAME = 'demo'
    PASSWORD = 'demo'

    r = c.get(url)
    input_element = r.html.find('input[name=requesttoken]', first=True)
    requesttoken_value = input_element.attrs.get('value')

    
    login_data = dict(user=USERNAME, password=PASSWORD, requesttoken=requesttoken_value)
    c.post(url, data=login_data)
    page = c.get('https://demo.owncloud.org/apps/files/?dir=/Photos&fileid=9')
    
    # soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.prettify())
    
    # page.html.render(sleep=5)
    # soup = BeautifulSoup(page.html.raw_html, "html.parser")
    # p = soup.findAll("a", class_="name")
    # for i in p:
    #     print(i)
    
    print(page.html.text)   
    # print(page.html.links)
    # print(page.html.absolute_links)
    # print(page.html.render())
    

    '''
    about = page.html.find('table[id=filestable]')
    for x in about:
        print(x.text)
        print(x.attrs)
        print(x.html)
        print(x.tag)
    '''
