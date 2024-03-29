from amostragens import sistematica as sis
from amostragens import casualSimples as cs
from amostragens import proporcionalEstratificada as pe


def menuPrincipal():
    while True:
        print('[1] - Amostragem simples casual')
        print('[2] - Amostragem sistematica')
        print('[3] - Amostragem proporcional estratificada')
        opcao = int(input('-> '))

        if opcao in [1, 2, 3]:
            break
        else:
            print('Opção inválida')
    return opcao


def acoes(opcao):
    if opcao in [1, 2]:
        pop = int(input('População: '))
        tamanho_amostra = int(input('Amostra: '))

    match opcao:
        case 1:
            amostras = cs.coletarAmostra(pop, tamanho_amostra)
            cs.imprimirAmostras(amostras)
        case 2:
            amostragem = sis.criarAmostragem(pop, tamanho_amostra)

            numeroInicial = sis.lerValorInicial(amostragem)
            amostras = sis.coletarAmostra(numeroInicial, pop, amostragem)
            sis.imprimirAmostra(amostras)
        case 3:
            qtde_grupos = int(input('Quantos grupos há na população: '))

            while True:
                tamanho_amostra = int(input('Digite o tamanho da amostra: '))

                if tamanho_amostra >= qtde_grupos:
                    break
                else:
                    print('Você digitou um número muito baixo')

            grupos = pe.coletarAmostra(qtde_grupos, tamanho_amostra)
            pe.mostrarTabela(grupos)


opcao = menuPrincipal()
acoes(opcao)

while True:
    print('')
    print('[1] - Sim')
    print('[2] - Não')
    opcao = int(input('Deseja visualizar outras amostragens: '))
    if opcao == 1:
        opcao = menuPrincipal()
        acoes(opcao)
    elif opcao == 2:
        print('Programa encerrado!')
        break
    else:
        print('')
        print('Opção invalida')
