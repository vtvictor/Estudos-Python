import os
import shutil
import subprocess

def remover_arquivo(caminho):
    try:
        os.remove(caminho)
    except PermissionError:
        print(f'Não foi possível remover o arquivo: {caminho}. Está em uso por outro processo.')

def limpar_temporarios():
    # Limpar arquivos temporários do computador
    os.system('del /F /Q C:\Windows\Temp\*')
    os.system('del /F /Q C:\Users\%USERNAME%\AppData\Local\Temp\*')

def limpar_firefox():
    # Limpar o Firefox
    subprocess.run('taskkill /F /IM firefox.exe', shell=True)
    shutil.rmtree('C:\Users\%USERNAME%\AppData\Local\Mozilla\Firefox\Profiles')

def limpar_chrome():
    # Limpar o Chrome
    subprocess.run('taskkill /F /IM chrome.exe', shell=True)
    shutil.rmtree('C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data')

def limpar_temp_usuarios():
    # Limpar a pasta TEMP dos usuários
    for root, dirs, files in os.walk('C:\Users'):
        if 'Temp' in dirs:
            temp_path = os.path.join(root, 'Temp')
            shutil.rmtree(temp_path)
            os.mkdir(temp_path)

def limpar_windows_temp():
    # Limpar a pasta Windows Temp
    os.system('del /F /Q C:\Windows\Temp\*')

def limpar_arquivos_log():
    # Limpar arquivos de log do Windows
    os.system('del /F /Q C:\Windows\Logs\CBS\*.log')
    os.system('del /F /Q C:\Windows\Logs\MoSetup\*.log')
    os.system('del /F /Q C:\Windows\Panther\*.log')
    os.system('del /F /Q C:\Windows\inf\*.log')
    os.system('del /F /Q C:\Windows\logs\*.log')
    os.system('del /F /Q C:\Windows\SoftwareDistribution\*.log')
    os.system('del /F /Q C:\Windows\Microsoft.NET\*.log')

def executar_limpezas():
    limpar_temporarios()
    limpar_firefox()
    limpar_chrome()
    limpar_temp_usuarios()
    limpar_windows_temp()
    limpar_arquivos_log()

executar_limpezas()
