"""Searches for files containing a specific term in a directory tree.

"""
def main():
    import os
    
    diretorio = input("Digite o diretório a ser buscado: ")
    termo = input("Digite o termo a ser buscado: ")
    
    for raiz, diretorios, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if termo in arquivo:
                caminho = os.path.join(raiz, arquivo)
                print(caminho)
    

if __name__ == "__main__":
    main()
