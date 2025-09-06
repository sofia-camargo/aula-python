print("exercicio 01")
x=10 
y=5

print("Soma:", x+y)
print("Subtração:", x-y)
print("Multiplicação: ", x*y)
print("Divisão real: ", x/y)
print("Divisão inteira: ", x//y)
print("Resto da divisão: ", x%y)
print("Potência: ", x**y)

print("\nexercicio 02")
x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))

print("A média dos dois números informados é ", (x+y)//2)

print("\nexercicio 03")
idade = int(input("Informe a idade:"))

if idade<=12:
    print("Criança")
elif idade<=17:
    print("Adolescente")
elif idade<=59:
    print("Adulto")
else:
    print("Idoso")


print("exercicio 07")

soma=0

for i in range(1,101):
    if i%2==0:
        soma+=i
print(soma)

print("Exercicio 09")

import random
numero_sorteado = random.randint(1,100)

numero= int(input("Adivinhe o número:"))
while numero != numero_sorteado:
    if numero>numero_sorteado:
        print("Maior que o sorteado")
    else:
        print("Menor que o sorteado")
    numero= int(input("Adivinhe o número:"))

print("Exercicio 10")

num = int(input("Digite um numero: "))
soma = 0
qtd = 0

while num != 0:
    soma+=num
    qtd+=1
    num = int(input("Digite um numero: "))

media = soma/qtd
print(f"Media dos números digitados é {media}")