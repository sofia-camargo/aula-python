#Dicionários
#Dicionários são coleções do tipo chave/valor
#São representados por chaves {}
#Podem ser criados com a função dict()

dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

print(dicionario)
print(dicionario['nome'])
print(dicionario.get('idade'))
print(dicionario.keys())
print(dicionario.values())

chave = input("Digite a chave que deseja acessar: ")
valor = input("Digite o valor para a chave: ")
dicionario[chave] = valor
print(dicionario)