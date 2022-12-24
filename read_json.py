import json

res = {'valor':'1111','valor':[[{'id':'5023', 'valor':'joao silva'},{'id':'5025', 'valor':'55555-5'}], 
                [{'id':'5023', 'valor':'marcos paulo'},{'id':'5025', 'valor':'33333-3'}]]
       }

# Opcional, mas é util
# comandos para converter um conteudo em elementos json, ou converter em elementos python.
# Experimente usar cada um deles em seguida usar o print, ou tentar iterar.

json_elementos = json.dumps(res, indent=4)
python_elementos = json.loads(json_elementos)
qtd = len(python_elementos['valor'])


for pos in range(0, qtd):  
    coluna_0 =  python_elementos['valor'][pos][0].get('valor')
    coluna_1 =  python_elementos['valor'][pos][1].get('valor')
    print(coluna_0,  coluna_1)
