# -*- coding: utf-8 -*-

import requests
from pprint import pprint

# A variável api_key armazena o Token de usuário
api_key = "0ed03bdc-dec7-4ac6-a385-3d0c8d1ec19b"

# Uma lista é criada com todos os números de processos a serem incluidos no DB

# caso entrada seja texto puro com um CNJ por linha:
lista_emails = """yulli.santos@grupopan.com
    joyce.sousa@grupopan.com
    Daniel.Ribeiro@grupopan.com
    nikolas.goi@grupopan.com
    michelle.duarte@grupopan.com
    janaina.barbosa@grupopan.com
    leticia.silva@grupopan.com
    angela.watanabe@grupopan.com
    marcell.garabito@grupopan.com
    caio.teixeira@grupopan.com
    cristiano.melo@grupopan.com
    felipe.araujo@grupopan.com
    Marcus.Rodovalho@grupopan.com
    natalia.andrade@grupopan.com
    yasmin.rosa@grupopan.com
    Rute.Silva.ext@grupopan.com
    rainna.lemos@grupopan.com
    Vanessa.MSilva.ext@grupopan.com
    gabriel.leite@grupopan.com
    vinicius.souza@grupopan.com
    ewerton.boscariol@grupopan.com
    juliana.pimenta@grupopan.com
    vanessa.lima@grupopan.com
    mayara.pereira@grupopan.com
    mayte.souza@grupopan.com
    Nayara.santos@grupopan.com
    Patricia.Gomes@grupopan.com
    fabiana.vasconcelos@pansolucoes.com
    rozana.costa@pansolucoes.com
    elisete.santos@grupopan.com
    elisabete.oliveira@pansolucoes.com
    selma.oliveira@grupopan.com
    kelly.himino@grupopan.com
    Luigi.Pontello.ext@grupopan.com
    Tiago.SAraujo.ext@grupopan.com
    Pedro.Nascimento.ext@grupopan.com
    samantha.rocha@interfile.com.br
    Larissa.Gomes.ext@grupopan.com
    leticia.jacome.ext@grupopan.com
    Nathalia.Silva.ext@grupopan.com
    Paula.Campos.ext@grupopan.com
    Camilo.Santos.ext@grupopan.com
    Leticia.Miranda.ext@grupopan.com
    Brenda.Moreira.ext@grupopan.com
    Flavia.Costa.ext@grupopan.com
    jessica.duarte@interfilebh.com.br
    Ivana.Ferreira.ext@grupopan.com
    Emily.Dias.ext@grupopan.com
    mt11256@interfile.com.br
    mt11319@interfile.com.br
    mt11412@interfile.com.br
    mt11792@interfile.com.br
    mt11923@interfile.com.br
    mt11965@interfile.com.br
    mt11967@interfile.com.br
    rene.costa@interfile.com.br
    Kelly.LSilva.ext@grupopan.com
    amanda.alves@interfile.com.br
    lorrane.dias@interfilebh.com.br
    gisele.silva@interfile.com.br
    jennifer.santos@interfile.com.br
    ana.reis@interfile.com.br
    ingrid.saviotti@interfile.com.br
    jenifer.silva@interfile.com.br
    dayane.almeida@interfile.com.br
    Barbara.Silva@interfilebh.com.br
    debora.candido@interfile.com.br
    deivide.silva@interfilebh.com.br
    erik.santos@interfile.com.br
    amanda.souza@interfilebh.com.br
    isabela.silva@interfile.com.br
    jessica.paz@interfile.com.br
    pedro.nascimento@interfile.com.br
    fabio.pontes@interfilebh.com.br
    wellida.silva@interfilebh.com.br
    Laisa.Oliveira@interfilebh.com.br
    kaique.goncalves@interfile.com.br
    larissa.gomes@interfile.com.br
    karine.silva@interfile.com.br
    cynthia.santos-cs@interfile.com.br
    emily.dias@interfile.com.br
    kelly.silva@interfile.com.br
    Leticia.Nascimento@interfile.com.br
    moniely.macedo@interfile.com.br
    otavio.presoti@interfile.com.br
    nathalia.silva@interfile.com.br
    Rafaella.Machado@interfilebh.com.br
    mariana.santos@interfile.com.br
    polyana.souza@interfile.com.br
    paula.campos@interfile.com.br
    tais.santana@interfile.com.br
    luigi.pontello@interfile.com.br
    tiago.araujo@interfile.com.br
    tessica.meireles@interfile.com.br
    ruth.silva@interfile.com.br
    juliana.santos@interfile.com.br
    victoria.paulo@interfile.com.br
    paula.guimaraes@interfile.com.br
    jonathan.santos@interfilebh.com.br
    gleidson.almeida@interfilebh.com.br
    mariana.santos@interfile.com.br
    amanda.alves@interfile.com.br
    renata.lopes@interfile.com.br
    edison.junior@interfilebh.com.br
    luis.rosa@interfile.com.br
    tessica.meireles@interfile.com.br
    patricia.pereira@interfilebh.com.br
    fabiula.zanoni@interfilebh.com.br
    daniele.ramalho@grupopan.com
    alessandra.lira@grupopan.com
    michelle.duarte@grupopan.com
    fabio.penha@grupopan.com
    tiago.mota@grupopan.com
    vanessa.baronceloyahata@grupopan.com
    vanessa.lima@grupopan.com
    daniel.ribeiro@grupopan.com
    ruth.silva@interfile.com.br
    Paula.Guimaraes@interfilebh.com.br
    Danielle.freitas@interfile.com.br
    deivide.silva@interfilebh.com.br
    juliana.pimenta@grupopan.com
    ewerton.boscariol@grupopan.com
    renata.ferreira@grupopan.com
    marcelo.costa@grupopan.com
    fabio.pontes@interfilebh.com.br
    paula.guimaraes@interfile.com.br
    emily.dias@interfile.com.br
    daniela.moreira@interfile.com.br
    Ana.Araujo@interfilebh.com.br"""
lista_emails = lista_emails.splitlines()

if __name__ == '__main__':
    # Itera sob cada processo e gera um JSON com o número do processo para fazer um POST request
    # Retorna o status do POST request

    for email in lista_emails:
        email = email.strip()
        payload = {
            'nome': email.split('@')[0].replace('.',' ').title(),
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
