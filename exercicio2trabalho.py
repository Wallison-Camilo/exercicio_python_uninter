print('Aluno Wallison camilo rosa RU: 3947124 e este é meu programa')
print('Bem vindo a Pizzaria do Wallison Camilo')
print('---------------------Cardápio-----------------------')
print('| Código | Descrição  | Pizza Média | Pizza Grande |')
print('|   21   | Napolitana |    R$20,00  |      R$26,00 |')
print('|   22   | Margherita |    R$20,00  |      R$26,00 |')
print('|   23   | Calabresa  |    R$25,00  |      R$32,50 |')
print('|   24   | Toscana    |    R$30,00  |      R$39,00 |')
print('|   25   | Portuguesa |    R$30,00  |      R$39,00 |')
print('----------------------------------------------------')

total = 0
#algoritmo de repetição que finaliza com break
while True:
    #primeiro testar o tamanho da pizza
    tam = input('Qual o tamanho da pizza (M/G):')
    if (tam == 'M' or tam == 'G'):
        #testar codigo da pizz
        piz = int(input('Entre com o código da pizza:'))
        #organizei por codigos diferentes para cada tamanho para receber o valor da pizza(valp)
        if(piz == 21):
            p = 'Napolitana'
            if (tam == 'M'):
                valp = 20
            else:
                valp = 26
        elif(piz == 22):
            p = 'Margherita'
            if (tam == 'M'):
                valp = 20
            else:
                valp = 26
        elif (piz == 23):
            p = 'Calabresa'
            if (tam == 'M'):
                valp = 25
            else:
                valp = 32.50
        elif (piz == 24):
            p = 'Toscana'
            if (tam == 'M'):
                valp = 30
            else:
                valp = 39
        elif (piz == 25):
            p = 'Portuguesa'
            if (tam == 'M'):
                valp = 30
            else:
                valp = 39
        #else caso o codigo estiver errado
        else:
            print('Opção Invalida')
            #continue para voltar o laço
            continue
        #soma do total para o retorno ao usuario
        total += valp
        #retorno ao usuario
        print('Voce pediu uma pizza {}'.format(p))
        print('Deseja pedir mais alguma coisa?')
        #saber se o cliente quer continuar ou não
        print('1 - Sim')
        print('0 - Não')
        x = int(input('>>'))
        if (x == 1):
            continue
        #retorno do total e o break para parar com o laço
        elif(x == 0):
            print('O total a ser pago é {:.2f}'.format(total))
            break
        #else caso o usuario nao entre com 1 ou 0 em continuar ou nao a operação
        else:
            print('Opçao Invalida')
            continue
    #else caso o usuario informe o tamanho errado da pizza
    else:
        print('Opção Invalida')
        continue