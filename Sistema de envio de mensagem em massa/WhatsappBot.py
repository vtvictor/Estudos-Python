#Bibliotecas utilizadas, comandos para instalar as mesmas:
#pip install pywhatkit
import pywhatkit as w
import time

#pip install pyautogui
import pyautogui as py
#pip install pandas

import pandas as pd

#Fazendo leitura do arquivo que contem os números.
dados = pd.read_excel(r'')
df = pd.DataFrame(dados)

#Contador de linhas para que o programa possa finalizar quando acabar
#os números de celulares.
qtd_linhas = (df['numero'].count())
print(f"Quantidade de números: {qtd_linhas}")

#Exceção utilizada para caso o bot consiga fazer o envio da mensagem.
try:
    for i in range(qtd_linhas):

        #Usuario vai receber a localização da linha (i) da coluna "numero" da tabela.
        usuario = df.loc[i, 'numero']

        w.sendwhatmsg_instantly(f'+5579{usuario}','')
        
        #time.sleep de 2 segundos para que o envio não seja rápido demais e trave.
        time.sleep(2)
        py.click(x=0, y=0)
        py.press('Enter')
        print("Mensagem enviada com sucesso!")

except:
    print("Erro inesperado!!")