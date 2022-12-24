# Esta biblioteca faz converção do xml para dicionário, e facilita o acesso as tags.
import xmltodict

# No exemplo aqui, o data é um atributo da tag cadastro, para acessar atributos use "@nome_atributo"
xml_file = '''<cadastro data='15/12/2022'>
                <pf>
                    <nome>joao</nome>
                    <telefone>111-222</telefone>
                    <status ativo='sim'></status>
                </pf>
                <pf>
                    <nome>jose</nome>
                    <telefone>555-555</telefone>
                    <status ativo='sim'></status>
                </pf>
                
            </cadastro>
            '''


doc = xmltodict.parse(xml_file)
print(doc['cadastro']['@data'])
print(doc['cadastro']['pf'][0]['nome'])
print(doc['cadastro']['pf'][0]['telefone'])
print(doc['cadastro']['pf'][0]['status']['@ativo'])
