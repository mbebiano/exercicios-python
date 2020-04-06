def computador_escolhe_jogada(n, m):
    jogadapc= n % (m+1)
    return jogadapc

def usuario_escolhe_jogada(n,m):
    jogadausuario= int(input('Quantas peças você vai tirar? '))
    while jogadausuario < 1 or jogadausuario > m:
        print('Oops! Jogada inválida! Tente de novo.')
        jogadausuario = int(input('Quantas peças você vai tirar?'))
    return jogadausuario

def partida():
    userjoke = 0
    pcjoke = 0
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    whostartfirst = n%(m+1)

    if whostartfirst == 0:
        print('Voce começa!')
        while n != 0:
            userjoke = usuario_escolhe_jogada(n, m)
            n = n - userjoke
            print('Você tirou ',userjoke,'peça(s).')
            print('Agora restam ', n, 'peça(s) no tabuleiro.')

            if n == 0:
                n = 0;
            else:
                pcjoke = computador_escolhe_jogada(n, m)
                n = n - pcjoke
                print('O computador tirou', pcjoke, 'peça(s).')
                if n == 0:
                    n = 0
                    print('Fim do jogo! O computador ganhou!')
                else:
                    print('Agora restam ', n, 'peça(s) no tabuleiro.')

    else:
        print('Computador começa!')
        while n != 0:
            pcjoke = computador_escolhe_jogada(n, m)
            n = n - pcjoke
            print('O computador tirou', pcjoke, 'peça(s).')
            if n == 0:
                n = 0
                print('Fim do jogo! O computador ganhou!')
            else:
                print('Agora restam ', n, 'peça(s) no tabuleiro.')
            if n==0:
                n=0
            else:
                userjoke = usuario_escolhe_jogada(n, m)
                n = n - userjoke
                print('Você tirou ', userjoke, 'peça(s).')
                print('Agora restam ', n, 'peça(s) no tabuleiro.')

def campeonato ():
    cont=1
    while cont<4:
        print('\n**** Rodada ',cont,' ****')
        partida()
        cont+=1

    print('**** Final do campeonato! ****')
    print('Placar: Você 0 X 3 Computador')

print('Bem-vindo ao jogo do NIM! Escolha:')
TipoJogo = int(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato: '))
if TipoJogo == 1:
    partida()
else:
    campeonato()