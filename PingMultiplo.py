import os
import time

with open ('ping_test_hosts.txt') as file:
    lerConteudo = file.read()
    lerConteudo = lerConteudo.splitlines()

    for ip in lerConteudo:
        print("Verificando o ip: ", ip)
        os.system(f'ping -n 2 {ip} ')
        time.sleep(5)

#remoção da main