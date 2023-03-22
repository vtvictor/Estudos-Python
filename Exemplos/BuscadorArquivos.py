import os

diretorio = input("Digite o diretório a ser buscado: ")
termo = input("Digite o termo a ser buscado: ")

for raiz, diretorios, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        if termo in arquivo:
            caminho = os.path.join(raiz, arquivo)
            print(caminho)
