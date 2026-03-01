#Peça um número inteiro `n` e mostre a tabuada de multiplicação de `1` até `10` para esse número.
n = int(input("Digite um número inteiro: "))
print("Tabuada de multiplicação para", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)