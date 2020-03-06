#импорты:
        #цветовая библиотека:
from colorama import Fore, Back, Style, init
        #задержка:
from time import sleep
import os
def clearShell():
    os.system(['clear', 'cls'][os.name == os.sys.platform])

init()

#открытие файла с алгоритмом
f = open("algorithm.txt", "r")
commands = []
for i in f:
    commands.append(i.split())


