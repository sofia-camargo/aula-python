#O modo "a" adiciona o novo conteúdo ao final do arquivo.
arquivo = open("dados.txt", "a")
arquivo.write("Adicionando uma nova linha ao arquivo.\n")
arquivo.close()

#O modo "w" apaga todo o conteúdo do arquivo e escreve o novo conteúdo.
with open("dados.txt", "w") as arquivo:
    arquivo.write("Sobrescrevendo o conteudo do arquivo.\n")
    conteudo = arquivo.read()
    print(conteudo)

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo) #O modo "r" abre o arquivo para leitura (padrão)
    for linha in arquivo:
        print("Linha:", linha, end="")
