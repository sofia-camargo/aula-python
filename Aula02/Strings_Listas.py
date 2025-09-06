#String em python

texto="Curso de Python na Prática"

print(texto.find("curso"))
print(texto.upper())
print(texto.lower())
print(texto.replace("Python","Java"))

listapalavras = texto.split(",")
print(listapalavras)

novo_texto = '-'.join(listapalavras)
print(novo_texto)


texto = "Sofia Camargo Nunes"
lista_palavras = texto.split(" ")
nome = ''.join(lista_palavras)
print(nome)

#Listas em Python
carros = []
carros.append("HRV")
carros.append("Corolla")
carros.append("Civic")
carros.append("Peugeot")
print(carros[0])

carros[3] = "Golf"
print(carros)

carros.insert(1, "Uno")
print(carros)

