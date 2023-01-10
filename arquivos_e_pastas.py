# Procurar nome de arquivo em pasta, usando nome parcial com coringa *
from pathlib import Path

ano = '2023'
mes = '01'
rootdir = f"c:\\temp\\{ano}\\Mês {mes}\\"

for extension in 'xlsx'.split():
    for path in Path(rootdir).glob('Inadimplentes*.' + extension):
        nome_arquivo = str(path)
        print(str(path))
