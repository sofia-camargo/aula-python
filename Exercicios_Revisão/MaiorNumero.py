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