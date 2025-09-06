#Funções em Python
def somar(a, b):
    return a + b   

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
resultado = somar(x,y)
print(resultado)

#Outro exemplo
def envia_email(nome, email):
    nome_dest = nome
    email_dest = email
    return(f"Email enviado para {nome_dest} no endereço {email_dest}")

pessoas = [
    {
        'nome': 'João',
        'idade': 30,  # <-- VÍRGULA ADICIONADA AQUI
        'email': 'joao@gmail.com'
    },
    {
        'nome': 'Maria',
        'idade': 25,  # <-- VÍRGULA ADICIONADA AQUI
        'email': 'maria@gmail.com'
    }
]

for pessoa in pessoas:
    email_enviado = envia_email(pessoa["nome"], pessoa["email"])
    print(email_enviado)

for indice, pessoa in enumerate(pessoas):
    email_enviado = envia_email(pessoa["nome"], pessoa["email"])
    print(f"{indice} - {email_enviado}")