import json

from xml.dom.minidom import parse

dom = parse("imobiliaria.xml")


imobiliaria = dom.documentElement


imoveis = imobiliaria.getElementsByTagName('imovel')

imobiliaria_json = []


for imovel in imoveis:
    descricao = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue

    nome = imovel.getElementsByTagName('nome')[0].firstChild.nodeValue
    emails = imovel.getElementsByTagName('email')
    telefones = imovel.getElementsByTagName('telefone')
    rua = imovel.getElementsByTagName('rua')[0].firstChild.nodeValue
    bairro = imovel.getElementsByTagName('bairro')[0].firstChild.nodeValue
    cidade = imovel.getElementsByTagName('cidade')[0].firstChild.nodeValue
    numero = imovel.getElementsByTagName('numero')
    tamanho = imovel.getElementsByTagName('tamanho')[0].firstChild.nodeValue
    numQuartos = imovel.getElementsByTagName('numQuartos')[0].firstChild.nodeValue
    numBanheiros = imovel.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue
    valor = imovel.getElementsByTagName('valor')[0].firstChild.nodeValue

    imovel_dict = {}
    proprietario = {}
    endereco = {}
    caracteristicas = {}
    imovel_dict ["descricao"] = descricao
    proprietario ["nome"] = nome
    
    telefones_json = []
    for telefone in telefones:
        telefones_json.append(telefone.firstChild.nodeValue)
    proprietario["telefone"] = telefones_json

    emails_json = []
    for email in emails:
        emails_json.append(telefone.firstChild.nodeValue)
    proprietario["email"] = emails_json

    imovel_dict["proprietario"]=proprietario

    endereco["rua"] = rua
    endereco["bairro"] = bairro
    endereco["cidade"] = cidade
    if (len(numero) > 0):
        endereco["numero"] = numero[0].firstChild.nodeValue
    imovel_dict["endereco"] = endereco
    
    caracteristicas["tamanho"] = tamanho
    caracteristicas["numQuartos"] = numQuartos
    caracteristicas["numBanheiros"] = numBanheiros
    imovel_dict["caracteristicas"] = caracteristicas
    imovel_dict["valor"] = valor
    imobiliaria_json.append(imovel_dict)

    print(imovel_dict)

with open("imobiliaria_json", "w") as json_file:
    json.dump(imobiliaria_json, json_file)







