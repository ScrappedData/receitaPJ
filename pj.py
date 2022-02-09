# https://github.com/ScrappedData/receitaPJ
import requests
import re
import json
import time
vermelho = "\033[0;31m"
vermelho2 = "\033[1;31m"
branco = "\033[1;37m"
verde = "\033[1;32m"
azul = "\033[1;34m"
print(f'''
{azul}
                    ,--.,-.----.        ,---._  
  ,----..         ,--.'|\    /  \     .-- -.' \ 
 /   /   \    ,--,:  : ||   :    \    |    |   :
|   :     :,`--.'`|  ' :|   |  .\ :   :    ;   |
.   |  ;. /|   :  :  | |.   :  |: |   :        |
.   ; /--` :   |   \ | :|   |   \ :   |    :   :
;   | ;    |   : '  '; ||   : .   /   :         
|   : |    '   ' ;.    ;;   | |`-'    |    ;   |
.   | '___ |   | | \   ||   | ;   ___ l         
'   ; : .'|'   : |  ; .':   ' | /    /\    J   :
'   | '/  :|   | '`--'  :   : :/  ../  `..-    ,
|   :    / '   : |      |   | :\    \         ; 
 \   \ .'  ;   |.'      `---'.| \    \      ,'  
  `---`    '---'          `---`  "---....--'    
{branco}                                       
''')
cnpj = input(f'{verde}CNPJ:{branco} ')
cnpj = re.sub('[^0-9]', "", cnpj)
def resultado(requestConsulta):
    jsonConsulta = json.loads(requestConsulta)
    status = jsonConsulta["status"]
    if(status == "ERROR"):
        return f"{vermelho2}Invalid{branco} CNPJ."
    atividadePrincipal = jsonConsulta["atividade_principal"]
    totalAtividades = len(atividadePrincipal)
    textoAtividades = ""
    if(totalAtividades >= 1):
        for i in range(0, totalAtividades):
            textoAtividades += atividadePrincipal[i]['text'] + ' - ' + atividadePrincipal[i]['code'] + '\n'
    else:
        textoAtividades = "No main activity found.\n"
    atividadeSecundaria = jsonConsulta["atividades_secundarias"]
    totalAtividadesSec = len(atividadeSecundaria)
    textoAtividadesSec = ""
    if(totalAtividadesSec >= 1):
        for i in range(0, totalAtividadesSec):
            textoAtividadesSec += atividadeSecundaria[i]['text'] + ' - ' + atividadeSecundaria[i]['code'] + '\n'
    else:
        textoAtividadesSec = "No secondary activity found.\n"
    QSA = jsonConsulta["qsa"]
    totalQSA = len(QSA)
    textoQSA = ""
    if(totalQSA >= 1):
        for i in range(0, totalQSA):
            textoQSA += QSA[i]['nome'] + ' - ' + QSA[i]['qual'] + '\n'
    else:
        textoQSA = "No QSA found.\n"
    cnpj = jsonConsulta["cnpj"]
    data_situacao = jsonConsulta["data_situacao"]
    situacao = jsonConsulta["situacao"]
    complemento = jsonConsulta["complemento"]
    tipo = jsonConsulta["tipo"]
    nome = jsonConsulta["nome"]
    uf = jsonConsulta["uf"]
    telefone = jsonConsulta["telefone"]
    email = jsonConsulta["email"]
    bairro = jsonConsulta["bairro"]
    logradouro = jsonConsulta["logradouro"]
    numero = jsonConsulta["numero"]
    cep = jsonConsulta["cep"]
    municipio = jsonConsulta["municipio"]
    porte = jsonConsulta["porte"]
    abertura = jsonConsulta["abertura"]
    natureza_juridica = jsonConsulta["natureza_juridica"]
    fantasia = jsonConsulta["fantasia"]
    ultima_atualizacao = jsonConsulta["ultima_atualizacao"]
    capital_social = jsonConsulta["capital_social"]
    return f'\n{verde}Name:{branco} {nome}\n{verde}Document:{branco} {cnpj}\n{verde}Date Status:{branco} {data_situacao}\n{verde}Status:{branco} {situacao}\n{verde}Type:{branco} {tipo}\n{verde}Fantasy:{branco} {fantasia}\n{verde}Phone:{branco} {telefone}\n{verde}Email:{branco} {email}\n{verde}Size:{branco} {porte}\n{verde}Opening:{branco} {abertura}\n{verde}Legal Nature:{branco} {natureza_juridica}\n{verde}Capital:{branco} {capital_social}\n{verde}Address:{branco} {logradouro}, {numero} - {complemento} - {municipio} - {uf} - CEP: {cep}\n{verde}Main Activities:{branco}\n{textoAtividades}{verde}Secondary Activities:{branco}\n{textoAtividadesSec}{verde}QSA:{branco}\n{textoQSA}{verde}Last Update:{branco} {ultima_atualizacao}'
if(len(cnpj) != 14):
    print(f'{vermelho2}CNPJ must contain {branco}15{vermelho2} digits.')
else:
    print(f'{verde}Looking for CNPJ:{branco} {cnpj}')
    requestConsulta = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').text
    if 'Too many requests, please try again later.' not in requestConsulta:
        print(resultado(requestConsulta))
    else:
        print(f'Too many requests, sleeping 1 minute.')
        time.sleep(60)
        print(resultado(requestConsulta))
