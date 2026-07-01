"""Pings a single host or IP address 6 times (Windows-specific).

"""
def main():
    #Importar a bilioteca OS 
    import os
    
    ip_host = input("Digite o IP ou Host a ser verificado: ")
    
    os.system(f'ping -n 6 {ip_host}')

if __name__ == "__main__":
    main()
