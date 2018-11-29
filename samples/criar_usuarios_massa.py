# -*- coding: utf-8 -*-

import requests
from pprint import pprint

# A variável api_key armazena o Token de usuário
api_key = "..."

# Uma lista é criada com todos os números de processos a serem incluidos no DB

# caso entrada seja texto puro com um CNJ por linha:
lista_emails = """nome.sobrenome@dominio.com
"""
lista_emails = lista_emails.splitlines()

if __name__ == '__main__':
    # Itera sob cada processo e gera um JSON com o número do processo para fazer um POST request
    # Retorna o status do POST request

    for email in lista_emails:
        email = email.strip()
        payload = {
            'name': email.split('@')[0].replace('.', ' ').title(),
            'email': email,
            'roles': ["tribproc.buscar_proc"],
        }
        url = "https://op.digesto.com.br/api/user?api_key=" + api_key
        response = requests.post(url, json=payload)
        response_data = response.json()
        if response.status_code != 200:
            pprint(response.content)
            # pprint(response_data)
        else:
            print email, 'ok'
