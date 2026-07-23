import os
import sys
import time
import ctypes
import keyboard


def init_console():
    """Força o pythonw.exe a alocar e exibir uma janela de console do Windows."""
    # Aloca uma nova janela de CMD
    ctypes.windll.kernel32.AllocConsole()

    # Redireciona a saída padrão (stdout e stderr) para a nova janela do CMD
    sys.stdout = open('CONOUT$', 'w', encoding='utf-8')
    sys.stderr = open('CONOUT$', 'w', encoding='utf-8')

    # Define o título da janela
    ctypes.windll.kernel32.SetConsoleTitleW("Contador Interativo")

    # Habilita suporte a cores ANSI no console alocado
    os.system('')


# Inicializa o console do Windows no .pyw
init_console()

# Cores ANSI
VERDE = "\033[92m"
RESET = "\033[0m"

# Dicionário ASCII para os dígitos (0-9) e sinal de menos (-)
DIGITS = {
    '0': ["█████", "█   █", "█   █", "█   █", "█████"],
    '1': ["  ██ ", " ███ ", "  ██ ", "  ██ ", "█████"],
    '2': ["█████", "    █", "█████", "█    ", "█████"],
    '3': ["█████", "    █", "█████", "    █", "█████"],
    '4': ["█   █", "█   █", "█████", "    █", "    █"],
    '5': ["█████", "█    ", "█████", "    █", "█████"],
    '6': ["█████", "█    ", "█████", "█   █", "█████"],
    '7': ["█████", "    █", "   ██", "  ██ ", " ██  "],
    '8': ["█████", "█   █", "█████", "█   █", "█████"],
    '9': ["█████", "█   █", "█████", "    █", "█████"],
    '-': ["     ", "     ", "█████", "     ", "     "]
}

count = 0
need_update = True


def render_big_number(number):
    """Converte o número em texto ASCII verde gigante."""
    num_str = str(number)
    lines = ["", "", "", "", ""]

    for char in num_str:
        if char in DIGITS:
            glyph = DIGITS[char]
            for i in range(5):
                lines[i] += glyph[i] + "  "

    return "\n".join([VERDE + line + RESET for line in lines])


def increment():
    global count, need_update
    count += 1
    need_update = True


def decrement():
    global count, need_update
    count -= 1
    need_update = True


def main():
    global need_update

    # Escuta as setas do teclado
    keyboard.add_hotkey('up', increment)
    keyboard.add_hotkey('down', decrement)

    # Oculta o cursor no terminal
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while True:
            if need_update:
                os.system('cls')
                print("\n" + "=" * 45)
                print("       CONTADOR INTERATIVO (PYW)")
                print("=" * 45 + "\n")

                print(render_big_number(count))

                print("\n" + "=" * 45)
                print(" [▲] Seta para CIMA: Incrementar (+1)")
                print(" [▼] Seta para BAIXO: Decrementar (-1)")
                print(" Feche a janela para sair.")

                need_update = False

            time.sleep(0.05)

    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


if __name__ == "__main__":
    main()