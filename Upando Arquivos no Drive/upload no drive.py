import pyautogui
import time

pyautogui.alert("O código vai começar! Não mexa em nada!")
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.PAUSE = 0.5
pyautogui.write('chrome')
pyautogui.PAUSE = 0.5
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write("drive.google.com")
pyautogui.PAUSE = 0.5
pyautogui.press('enter')
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(1310, 529)
pyautogui.mouseDown()
pyautogui.moveTo(729, 685)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()
pyautogui.alert("Fim do processo")