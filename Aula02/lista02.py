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