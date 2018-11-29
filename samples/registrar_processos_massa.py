# -*- coding: utf-8 -*-

import requests
from pprint import pprint

# A variável api_key armazena o Token de usuário
api_key = "..."

# Uma lista é criada com todos os números de processos a serem incluidos no DB
lista_processos = [
    ['1315271', '08052625820148120110', ],
    ['1588098', '01735267420128190004', ],
]

# caso entrada seja texto puro com um CNJ por linha:
# lista_processos = lista_processos.splitlines()

if __name__ == '__main__':
    # Itera sob cada processo e gera um JSON com o número do processo para fazer um POST request
    # Retorna o status do POST request

    for user_custom, processo in lista_processos:
        # ver detalhes de um processo monitorado em https://op.digesto.com.br/doc_api/schemas/proc.html
        payload = {
            'numero': processo,
            'user_custom': user_custom,
            'is_monitored_tribunal': False,
            'is_monitored_diario': True,
            # 'monitor_period': 2,  # 36h
        }
        url = "https://op.digesto.com.br/api/proc?api_key=" + api_key
        response = requests.post(url, json=payload)
        response_data = response.json()
        if response.status_code != 200:
            pprint(response.content)
            # pprint(response_data)
        else:
            print processo, 'ok'
