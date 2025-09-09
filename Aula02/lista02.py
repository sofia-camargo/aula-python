'''Exercicio 01
Faça um programa em Python que leia uma data de nascimento no formato dd/mm/aaaa e
imprima a data com o mês escrito por extenso.
'''
data = (input("Digite a data de nascimento:"))

data = data.split("/")
print(f"Você nasceu em {data[0]} de {data[1]} de {data[2]}")
## da para resolver como dicionario ou lista

print(data)

'''
Exercício 02 
Faça um programa em Python que recebe uma string que representa uma cadeia de DNA e
gera a cadeia complementar.'''

dna = input("Digite uma cadeia de DNA: ").upper()
tam_dna = list(dna)

for i in range(len(tam_dna)):
    if tam_dna[i] == "A":
        tam_dna[i] = "T"
    elif tam_dna[i] == "T":
        tam_dna[i] = "A"
    elif tam_dna[i] == "C":
        tam_dna[i] = "G"
    elif tam_dna[i] == "G":
        tam_dna[i] = "C"
    else:
        print("Cadeia de DNA inválida")
        break

print(''.join(tam_dna))

'''Exercício 
Crie uma lista com as notas [7.5, 8.0, 6.0, 9.5, 10.0].
• Remova a menor nota;
• Mostre a média final.
'''
notas = [7.5,8.0,6.0,9.5,10.0]

# Adiciona uma nova nota
notas.append(9.2)
print(notas)

# Remove a menor nota
notas.remove(min(notas))

print(notas)    

# Calcula a média final
soma = 0
for i in range(len(notas)):
    soma += notas[i]

media = soma / len(notas)
print(f"A média das notas é: {media}")

'''Exercício 04
Crie uma tupla com os 12 meses do ano.
• Peça para o usuário digitar um número de 1 a 12 e mostre qual mês corresponde.
'''
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

mes = int(input("Digite um numero de 1 a 12: "))
if 1 <= mes <= 12:
    print(f"O mês correspondente é: {meses[mes-1]}")
else: 
    print("Número inválido")

'''Exercício 05
Crie um dicionário para armazenar informações de um aluno:
• Nome, idade e curso.
• Depois, imprima os dados formatados.
'''
aluno = {
    "nome": "Sofia",
    "idade": 22,
    "curso": "Sistemas de Informação"
}
print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")

'''Exercício 06
Peça para o usuário digitar 10 números (pode repetir). 
• Armazene-os em um conjunto; 
• Mostre quais números foram digitados sem repetição. '''

numeros = set()
for i in range(10):
    num = int(input("Digite um número: "))
    numeros.add(num)
print("Números digitados sem repetição:", numeros)

'''exercício 7
Escreva uma função que receba a base e a altura de um triângulo e retorne sua área. 
'''

def calcularArea(a, b):
    return (a*b)/2

altura = int(input("Digite a altura do triângulo:"))
base = int(input("Digite a base do triângulo:"))

resultado = calcularArea(altura,base)

print(f"Área do triângulo: {resultado}")

'''
Exercício 08
Escreva uma função que receba uma lista de números e retorne apenas os números pares. 
'''
def definirPar(lista, TamLista):
    pares = []
    for i in range(TamLista):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    return pares    

lista = [1,2,3,4,5,6,7,8,9,10]
tamLista = len(lista)
resultado = definirPar(lista, tamLista)

print("Números pares na lista:", resultado)

with open("nomes.txt", "a") as arquivo:
    while True:
        nomeAluno = input("Digite o nome de um aluno:")
        if nomeAluno == "fim":
            break
        arquivo.write(nomeAluno + "\n")
print("Nomes salvos com sucesso!")

with open("nomes.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Nome dos alunos:")
    print(conteudo)