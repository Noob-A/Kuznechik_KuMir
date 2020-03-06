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
f = open("alg.txt", "r")
commands = []
for i in f:
    commands.append(i.split())

#переменные:
pos = 0
commands_counter = 0
x = 0
listor = []
listor_counter = []

colornumlist = []
print(Fore.WHITE, end = "")
stat = False
while True:
    # try:
        command = commands[commands_counter]
        commands_counter += 1
        command_split = command
        if command_split[0] == "крас":
            colornumlist.append(pos)
            print("Клетка " + str(pos) + " окрашена")
        elif command_split[0] == "лев":
            pos -= int(command_split[1])
            print("Переместился влево на " + str(command_split[1]))
        elif command_split[0] == "прав":
            pos += int(command_split[1])
            print("Переместился вправо на " + str(command_split[1]))
        elif command_split[0] == "список":
            print(colornumlist)
        elif command_split[0] == "украс":
            colornumlist.remove(pos)
            print("С клетки " + str(pos) + " краска удалена")
        elif command_split[0] == "абс":
            pos = int(command_split[1])
            print("Переместился на " + str(command_split[1]))
        elif command_split[0] == "цикл":
            stat = True
            i3 = commands_counter
            while True:
                if command_split[2] == "+":
                    listor.append(i3)
                else:
                    break
        
        if pos in colornumlist:
            print("Текущая позиция " + str(pos))
        else:
            print("Текущая позиция " + str(pos))
				
        #    
        #цикл 2
        #+ лев 1 
        #+ красичоооооооооооооооооооо
        linelist = list(range(pos - 5, pos + 6))
        for i in linelist:
            if i == pos and i in colornumlist:
                print(Back.WHITE + Fore.CYAN + "*" + str(i) + "*" + Back.RESET, end="")
            elif i in colornumlist:
                print(Fore.CYAN + "{0}".format(i), end="")
            elif i == pos:
                print(Back.WHITE + Fore.BLACK  + "*" + str(i) + "*" + Back.RESET, end="")
            else:
                print(Fore.WHITE + "{0}".format(i), end="")
            print(Fore.RED + " ─ ", end = "")
            print(Fore.WHITE, end="")
        print()
            
        
        
        
        if commands_counter >= len(commands):
            input()
            break

        sleep(2)
        clearShell()
    # except:		
    #     x += 1
    #     if x == 5:
    #         break
