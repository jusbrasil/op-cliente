# -*- coding: utf-8 -*-

import requests
from pprint import pprint

# A variável api_key armazena o Token de usuário
api_key = "..."

# Uma lista é criada com todos as partes e CNPJS a serem incluidos no monitoramento
partes = [(u'ABN AMRO Arrendamento Mercantil', '34033779000163'),
(u'América do Sul Leasing SA Arrendamento Mercantil', '44081677000177'),
(u'AYMORÉ CRÉDITO, FINANCIAMENTO E INVESTIMENTO', '7707650000110'),
(u'Banco ABN AMRO REAL', '33066408000115'),
(u'BANCO BANDEPE', '10866788000177'),
(u'Banco Comercial de Investimentos Sudameris', '61230165004131'),
(u'BANCO SANTANDER', '90400888000142'),
(u'ISBAN BRASIL', '62588793000169'),
(u'PRODUBAN SERVIÇOS DE INFORMÁTICA', '94870557000127'),
(u'SANPREV – SANTANDER ASSOCIAÇÃO DE PREVIDÊNCIA', '60741360000176'),
(u'SANTANDER BRASIL ADMINISTRADORA DE CONSÓRCIO', '55942312000106'),
(u'SANTANDER BRASIL ASSET MANAGEMENT DISTRIBUIDORA', '10977742000125'),
(u'VALORES MOBILIÁRIOS', '10977742000125'),
(u'Santander Brasil Establecimiento Financeiro de Crédito', '18323912000160'),
(u'SANTANDER CAPITALIZAÇÃO', '3209092000102'),
(u'SANTANDER CORRETORA DE CÂMBIO E VALORES MOBILIÁRIOS', '51014223000149'),
(u'SANTANDER LEASING SA ARRENDAMENTO MERCANTIL', '47193149000106'),
(u'SANTANDER MICROCRÉDITO ASSESSORIA FINANCEIRA', '4980127000175'),
(u'SANTANDER PARTICIPAÇÕES', '4270778000171'),
(u'Santander SA - Corretora de Câmbio e Títulos', '51014223000149'),
(u'SANTANDER SA - SERVIÇOS TÉCNICOS, ADMINISTRATIVOS E DE CORRETAGEM DE SEGUROS', '52312907000190'),
(u'SANTANDER SECURITIES SERVICES BRASIL DTVM', '62318407000119'),
(u'SANTANDERPREVI – SOCIEDADE DE PREVIDÊNCIA PRIVADA', '68687185000198'),
(u'WEBCASAS', '18511694000197'),
(u'WEBMOTORS', '3347828000109'),
(u'ZURICH SANTANDER BRASIL SEGUROS E PREVIDÊNCIA', '87376109000106'),
(u'SANTANDER BRASIL SEGUROS', '6136920000118'),]

if __name__ == '__main__':
    # Itera sob cada processo e gera um JSON com o número do processo para fazer um POST request
    # Retorna o status do POST request
    ok = 0
    for nome, cnpj in partes:
        # ver detalhes de um processo monitorado em https://op.digesto.com.br/doc_api/schemas/proc.html
        payload = {
            'nome': nome,
            'is_monitored_tribunal': True,
            'is_monitored_diario': False,
            'cnpj': long(cnpj),
        }
        url = "https://op.digesto.com.br/api/monitored_person?api_key=" + api_key
        response = requests.post(url, json=payload)
        if response.status == 200:
            ok += 1
        response_data = response.json()
        pprint(response_data)

    print 'solicitados', len(partes)
    print 'sucesso', ok
