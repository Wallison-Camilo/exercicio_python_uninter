print('Aluno Wallison camilo rosa RU: 3947124 e este é meu programa')
print('Bem vindo ao programa de feijoada do Wallison Camilo')
#funçao com try e except para evitar erro de digitaçao do usuario
def volumeFeijoada():
    while True:
        try:
            print('Menu Volume Feijoada')
            ml = float(input('Entre com a quantidade que deseja(ml):'))
            if (ml >= 300 and ml <= 5000):
                return ml * 0.08
            else:
                print('Não aceitamos porções menores que 300 ml ou maiores que 5l. Tente novamente!')
                continue
        except ValueError:
            print('Você não digitou uma opção valida')
            continue
    #funçao simples com repetiçao caso insera um valor indesejado
def opcaoFeijoada():
    while True:
        print('Menu Opção Feijoada:')
        print('Entre com a opção de Feijoada:')
        print('b - Básica(Feijão + paiol + costelinha')
        print('p - Premium(Feijão + paiol + costelinha + partes de porco')
        print('s - Suprema(Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon')
        opc = input('>>')
        if(opc == 'b'):
            return 1.0
        elif(opc == 'p'):
            return 1.25
        elif(opc == 's'):
            return 1.5
        else:
            print('Você não digitou uma opção valida')
            continue
#funcao para gerar infinitos acompanhamentos e somar os seus valores
def acompanhamentoFeijoada(x = 0):
    while True:
        print('Deseja mais algum acompanhamento?')
        print('0- Não desejo mais acompanhamentos (encerrar pedido)')
        print('1- 200g de arroz')
        print('2- 150g de farofa especial')
        print('3- 100g de couve cozida')
        print('4- 1 laranja descascada')
        #adicionei um try e except para nao dar erro caso o usuario entre com algo que nao fosse um numero
        try:
            acp = int(input('>>'))
            if(acp == 1):
                x += 5
                continue
            elif (acp == 2):
                x += 6
                continue
            elif (acp == 3):
                x += 7
                continue
            elif (acp == 4):
                x += 3
                continue
            elif (acp == 0):
                return x
            else:
                print('Você não digitou uma opção valida')
                continue
        except ValueError:
            print('Você não digitou uma opção valida')
            continue
#saida dos valores
volumeFeijoada = volumeFeijoada()
opcaoFeijoada = opcaoFeijoada()
acompanhamentoFeijoada = acompanhamentoFeijoada()
total = (volumeFeijoada* opcaoFeijoada) + acompanhamentoFeijoada
print('O valor a ser pago é (R$): {:.2f} (volume = {:.2f} * opçao = {:.2f} + acompanhamento = {:.2f})'.format(total,volumeFeijoada,opcaoFeijoada,acompanhamentoFeijoada))