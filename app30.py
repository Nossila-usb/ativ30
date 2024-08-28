# importa bibliotecas
import pyautogui as aut
import time

link_reposi = input('O link do repositório: ')
versao = input('O nome da versão: ')

aut.PAUSE = 1


aut.press('win')
aut.write('vscode')
aut.press('enter')

time.sleep(5)

aut.hotkey('ctrl', 'j')
time.sleep(5)

aut.write('git init')
aut.press('enter')
aut.write('git add .')
aut.press('enter')
aut.write(f'git commit -m "{versao}"')
aut.press('enter')



time.sleep(5)

aut.write('git branch -M main')
aut.press('enter')
aut.write(f'git remote add origin {link_reposi}')
aut.press('enter')

aut.write('git push -u origin main')
aut.press('enter')