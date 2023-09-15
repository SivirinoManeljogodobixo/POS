import json

with open('imobiliaria_json') as json_file:
    imobiliaria = json.load(json_file)

id_imovel = 0

for imovel in imobiliaria:
    id_imovel += 1
    print(f'{id_imovel} - {imovel["descricao"]}')

id_visualizado = int(input("Digite o id do imóvel: "))

imovel = imobiliaria[id_visualizado-1]

proprietario = imovel["proprietario"]

endereco = imovel["endereco"]

caracteristicas = imovel["caracteristicas"]

print("/n")

print("\nDescrição: ", imovel["descricao"])

print("\nProprietário: ")

print("       Nome: ", proprietario["nome"])
print("       Telefones: ", ''.join(proprietario["telefone"]))
print("       Emails: ", ''.join(proprietario["email"]))
print("Endereço: ")
print("       Rua: ", endereco["rua"])
print("       Bairro: ", endereco["bairro"])
print("       Cidade: ", endereco["cidade"])
if("numero" in endereco):
    print("       Número: ", endereco["numero"])
print("\nCaracteristicas: ")
print("       Tamanho: ", caracteristicas["tamanho"], 'm²')
print("       Número de quartos: ", caracteristicas["numQuartos"])
print("       Número de banheiros: ", caracteristicas["numBanheiros"])
print("       Valor: R$", imovel["valor"])