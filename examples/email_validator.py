"""Validates email format using a simple regular expression pattern.

"""
def main():
    import re
    
    def verificar_email(email):
        padrao = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+$"
        if re.match(padrao, email):
            return True
        else:
            return False
    
    email = input("Digite o e-mail: ")
    if verificar_email(email):
        print("E-mail válido")
    else:
        print("E-mail inválido")
    

if __name__ == "__main__":
    main()
