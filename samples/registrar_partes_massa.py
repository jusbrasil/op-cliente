# -*- coding: utf-8 -*-

import re
import requests
import csv
from pprint import pprint

# A variável api_key armazena o Token de usuário
api_key = "....-1f78-4152-8097-b4a49cbe084b"


if __name__ == '__main__':
    # Itera sob cada processo e gera um JSON com o número do processo para fazer um POST request
    # Retorna o status do POST request
    # Uma lista é criada com todos as partes e CNPJS a serem incluidos no monitoramento
    # definido manualmente
    if False:
        partes = [(u'nome...', 'cnpj'),
                  ]
    # lendo de csv
    if False:
        my_file = open("partes.csv", 'r')
        reader = csv.reader(my_file, delimiter=',')
        partes = list(reader)
    # lendo de excel
    import pandas

    partes = [[x[0], x[1]] for index, x in pandas.read_excel(
        '/Users/rnc/Downloads/Empresas SAP  08.08.2017.xlsx').iterrows()]

    ok = 0
    for nome, cnpj in partes:
        # ver detalhes de um processo monitorado em https://op.digesto.com.br/doc_api/schemas/proc.html
        payload = {
            'nome': nome,
            'is_monitored_tribunal': True,
            'is_monitored_diario': False,
            'cnpj': long(re.sub(r'[^\d]', "", str(cnpj))),
        }
        url = "https://op.digesto.com.br/api/monitored_person?api_key=" + api_key
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            ok += 1
        response_data = response.json()
        pprint(response_data)

    print 'solicitados', len(partes)
    print 'sucesso', ok
