#Importando a biblioteca PyAutogui para a leitura de tela, screenshot e pixels
import pyautogui
#Importando keyboard para verificar qual esta apertada para parar o loop
import keyboard
#Importando Apis do windows para realizar o click de forma mais rapida e eficaz
import win32api, win32con
#Importando time para usar o sleep, após um click no alvo  para evitar double click
import time

#Função para clicar na tela, recebendo X e Y
def click (x,y):
    #Usando api do windows porque é mais rapido

    win32api.setCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32.api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#O core do aimbot, a inteligencia que roda enquanto não apertar a tecla C no teclado
while keyboard.is_pressed('c')==False:

    #Tira um print da regiao onde está o jogo
    sc = pyautogui.screenshot(region=(103,250,500,500))
    #O tamanho da altura e largura do printscreen
    width,height = sc.size 

    #Loopando o printscreen e loopando os pixels do printscreen para validar o RGB
    #ou seja, quando for um RGB especifico vai clicar.   
    for x in range(0,width,12):
        achou = 0
        for y in range (0, height,12):
            #Pegando o RGB
            r,g,b = sc.getpixel((x,y))
            #Verificando o RGB se é o mesmo do alvo
            print(r,g,b)
            if r==255 and g==219 and b==195:
                #Se for, clica no alvo extamente na posição X e Y
                achou == 1
                click(103+x,250+y)
                #Espera 5 milisegundos para não clicar novamente e errar o alvo
                time.sleep(0.05)
                break
            
        if achou == 1 :
            break

sc = pyautogui.screenshot(region=(103,250,610,610))
sc.save('Exemplo.png')