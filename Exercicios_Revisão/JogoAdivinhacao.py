import random
numero_aleatorio = random.randint(1, 100)

# Primeira leitura
num = int(input("Digite um número inteiro entre 1 e 100: "))

if num < 1 or num > 100:
    print("Número inválido. Por favor, digite um número entre 1 e 100.")
else:
    while(num != numero_aleatorio):
        if num < numero_aleatorio:
            print(f"O número secreto é maior do que {num}") 
        else:
            print(f"O número secreto é menor do que {num}")
        
        num = int(input("Tente novamente: "))

    print(f"Parabéns! Você acertou o número {numero_aleatorio}")