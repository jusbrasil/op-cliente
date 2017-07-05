# -*- coding: utf-8 -*-

import requests
from pprint import pprint
# A variável api_key armazena o Token de usuário

api_key = "e2d85934-9bc8-4811-baf6-59e5069a279d"

# Uma lista é criada com todos os números de processos a serem incluidos no DB

lista_processos = """0022615-39.2016.8.11.0002
0820358-48.2016.8.23.0010
0007803-63.2016.8.05.0000
1031359-76.2017.8.26.0576
0501593-64.2017.4.05.8106"""

lista_processos = lista_processos.splitlines()

if __name__ == '__main__':
    # Itera sob cada processo e gera um JSON com o número do processo para fazer um POST request
    # Retorna o status do POST request
    
    for processo in lista_processos:
        payload = {
            'numero': processo,
            'is_monitored_tribunal': True,
            'is_monitored_diario': False,
            'monitor_period': 2,  # 36h
        }
        url = "https://op.digesto.com.br/api/proc?api_key=" + api_key
        response = requests.post(url, json=payload)
        response_data = response.json()
        pprint(response_data)

