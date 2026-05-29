import random
import platform
import pyperclip
import os
import colorama
import keyboard

colorama.init(autoreset=True)

operacionalSystem = platform.system()

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

simbols = [
    '!', '<', '>', '@', '#', '$', '%', '&', '*',
    '(', '=', ')', '-', '+', '[', ']', '.', ',',
    '"', "'"
]

lists = [letters, numbers, simbols]


def clear_terminal():
    if operacionalSystem == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main(passwordLenght):
    password = ''

    for _ in range(passwordLenght):
        random_list = random.choice(lists)
        random_element = random.choice(random_list)
        password += str(random_element)

    print(
        colorama.Fore.GREEN +
        f"\n[+] Senha Gerada com sucesso: "
        f"{colorama.Fore.WHITE}{password}"
    )

    # Apenas no Windows copia automaticamente
    if operacionalSystem == "Windows":
        pyperclip.copy(password)
        print(
            colorama.Fore.GREEN +
            "[+] Senha copiada para a área de transferência."
        )
    else:
        print(
            colorama.Fore.YELLOW +
            "[!] Sistema não Windows detectado."
        )
        print(
            colorama.Fore.YELLOW +
            "[!] A senha NÃO foi copiada automaticamente."
        )

    print(colorama.Fore.RED + "\n-----END\n")

    print(colorama.Fore.YELLOW + "[$] Especificações da senha")
    print(f"[$] Total de caracteres na senha: {passwordLenght}")

    if passwordLenght < 16:
        print("[$] Força da senha: [X] Boa | [] Forte | [] Impenetrável")
    elif passwordLenght < 100:
        print("[$] Força da senha: [] Boa | [X] Forte | [] Impenetrável")
    else:
        print("[$] Força da senha: [] Boa | [] Forte | [X] Impenetrável")

    print(colorama.Fore.GREEN + "\n[+] Aperte qualquer tecla para sair.")
    keyboard.read_event()


clear_terminal()

while True:
    try:
        print(
            "/ Gerador de senhas para maniacos /\n"
            + colorama.Fore.GREEN +
            " - by fyex86\n\n"
            + colorama.Fore.YELLOW
        )

        print("[-] Minimo caracteres: 8")
        print("[-] Máximo caracteres: quantos quiser")
        print("[-] Aperte Ctrl + C para sair.\n")

        lenght = int(input(
            colorama.Fore.GREEN + " -> " + colorama.Fore.WHITE
        ))

        clear_terminal()

        if lenght < 8:
            print(
                colorama.Fore.RED +
                "[-] A senha deve ter pelo menos 8 caracteres."
                "\n-----END\n"
            )

        else:
            main(lenght)
            break

    except ValueError:
        clear_terminal()

        print(
            colorama.Fore.RED +
            "[-] Por favor, digite um número inteiro.\n"
            "-----END\n"
        )

    except KeyboardInterrupt:
        clear_terminal()
        print("[:3] Tchau tchau.\n")
        break