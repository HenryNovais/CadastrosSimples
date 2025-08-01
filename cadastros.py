from PackCad import dadosuser
import time


laço = True
while laço:
    dadosuser.estilo("MENU PRINCIPAL")
    print('\033[0;33m1 - \033[0;34mVer pessoas cadastradas\n\033[0;33m2 - \033[0;34mCadastra nova pessoa\n\033[0;33m3 - \033[0;34mSair do Sistema\033[m')
    print('--' * 20)
    try:
        res = dadosuser.validar('\033[0;33mSua Opção: \033[m\033[0;32m')
    except:
        print('\n\033[31mENCERRANDO.\033[m', end='')
        time.sleep(0.3)
        print('\033[31m.\033[m', end='')
        time.sleep(0.3)
        print('\033[31m.\033[m')
        time.sleep(0.3)
        laço = False
        continue
    time.sleep(0.5)
    if res == 1:
        dadosuser.estilo('PESSOAS CADASTRADAS')
        with open('cadastros.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            if conteudo != '':
                print(conteudo)
            else:
                print('\033[31mNenhum usuário cadastrado no momento!\033[m')
    elif res == 2:
        dadosuser.estilo('NOVO CADASTRO')
        with open('cadastros.txt', 'a') as arquivo:
            try:
                nome = input('Nome: ')
                idade = dadosuser.lerInteiro('Idade: ')
            except:
                print('\n\033[31mENCERRANDO.\033[m', end='')
                time.sleep(0.3)
                print('\033[31m.\033[m', end='')
                time.sleep(0.3)
                print('\033[31m.\033[m')
                time.sleep(0.3)
                laço = False
                continue
            arquivo.write(f'{nome:<30}{idade:>3} anos\n')
        print(f'Novo registro de {nome} adicionado!')
        time.sleep(1)
    elif res == 3:
        dadosuser.estilo('VOLTE SEMPRE!')
        break
