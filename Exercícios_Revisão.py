# Peça três números ao usuário e informe qual é o maior deles.
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")

if num1 > num2 and num1 > num3:
    print("O maior número é:", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)


#Outra forma de resolver o exercício:
#num1 = input("Digite o primeiro número: ")
#num2 = input("Digite o segundo número: ")
#num3 = input("Digite o terceiro número: ")
#maior = num1
#if num2 > maior:
#    maior = num2
#if num3 > maior:
#    maior = num3
#print("O maior número é:", maior)


#Peça um número inteiro `n` e mostre todos os números de `1` até `n`.
n = int(input("Digite um número inteiro: "))
soma = 0 
for i in range(1, n + 1):
    soma += i

print("A soma dos números de 1 a", n, "é:", soma)

#Peça um número inteiro `n` e mostre a tabuada de multiplicação de `1` até `10` para esse número.
n = int(input("Digite um número inteiro: "))
print("Tabuada de multiplicação para", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)