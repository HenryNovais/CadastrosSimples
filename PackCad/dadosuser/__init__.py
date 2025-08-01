def estilo(msg):
    print('\033[m--' * 20)
    print(f'{msg:^40}')
    print('--' * 20)

def validar(msg):
    while True:
        try:
            n = int(input(msg))
            if n > 3 or n < 1:
                print('\033[31mERRO! Digite um vaor dentro dos limites.\033[m')
                continue
            return n
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

def lerInteiro(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')