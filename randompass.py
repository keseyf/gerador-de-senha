import random
import platform
import pyperclip
import os
import time
import colorama
import keyboard

operacionalSystem = platform.system()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbols = ['!','<','>','@','#','$','%','&','*','(','=',')', '-', '+','[',']','.',',','"',"'"]
lists = [letters, numbers, simbols]

def main(passwordLenght):
    password = ''
    for _ in range(passwordLenght):
        random_list = random.choice(lists)
        random_element = random.choice(random_list)
        password += str(random_element)

    print(colorama.Fore.GREEN + f"\n[+] Senha Gerada com sucesso: {colorama.Fore.WHITE + password}")
    if operacionalSystem == "Windows":
        pyperclip.copy(password)
        print(colorama.Fore.GREEN + f"[+] Senha copiada para a área de transferência.")
    print(colorama.Fore.RED+"\n-----END\n")
    print(colorama.Fore.YELLOW+"[$] Especificações da senha")
    print(f"[$] Total de caracteres na senha: {passwordLenght}")
    
    if passwordLenght < 16:
        print("[$] Força da senha: [X] Boa | [] Forte | [] Impenetrável")
    elif passwordLenght >= 16 and passwordLenght < 100:
        print("[$] Força da senha: [] Boa | [X] Forte | [] Impenetrável")
    else:
        print("[$] Força da senha: [] Boa | [] Forte | [X] Impenetrável")
    
    
    print(colorama.Fore.GREEN + "[+] Aperte qualquer tecla para sair do processo.")
    print(colorama.Fore.WHITE)
    
    # Espera o usuário pressionar qualquer tecla para sair
    keyboard.read_event()

if operacionalSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

while True:
    try:
        print("/ Gerador de senhas para maniacos /\n" +colorama.Fore.GREEN +" - by fyex86\n\n"+colorama.Fore.YELLOW+"")
        print("[-] Minimo caracteres: 8")
        print("[-] Máximo caracteres: quantos quiser")
        print("[-] Aperte Ctrl + C para sair.\n")
        lenght = int(input(colorama.Fore.GREEN +" -> "+colorama.Fore.WHITE+""))
        if operacionalSystem == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        if lenght < 8:
            # Se o número for menor que 8, não fecha o programa, apenas pede para tentar novamente.
            if operacionalSystem == "Windows":
                os.system("cls")
                print(colorama.Fore.RED+"[-] A senha deve ter pelo menos 8 caracteres. Tente novamente.\n-----END\n"+colorama.Fore.WHITE+"")
            else:
                os.system("clear")
                print(colorama.Fore.RED+"[-] A senha deve ter pelo menos 8 caracteres. Tente novamente.\n-----END\n"+colorama.Fore.WHITE+"")
        else:
            # Quando o número de caracteres for válido, gera a senha.
            main(lenght)
            break  # Sai do loop após gerar a senha válida

    except ValueError:
        # Caso o usuário insira um valor não numérico, pede para tentar novamente.
        if operacionalSystem == "Windows":
            os.system("cls")
            print(colorama.Fore.RED+"[-] Por favor, digite um número inteiro.\n"+"-----END\n"+colorama.Fore.WHITE+"")
        else:
            os.system("clear")
            print(colorama.Fore.RED+"[-] Por favor, digite um número inteiro.\n"+"-----END\n"+colorama.Fore.WHITE+"")
    except KeyboardInterrupt:
        # Caso o usuário pressione Ctrl + C, fecha o programa.
        if operacionalSystem == "Windows":
            os.system("cls")
            print("[:3] Tchau tchau.\n")
        else:
            os.system("clear")
        print("[:3] Tchau tchau.\n")
        break
