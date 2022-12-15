print('Aluno Wallison camilo rosa RU: 3947124 e este é meu programa')
#Entrada
valp = float(input('Qual o preço do produto escolhido?'))
qntp = int(input('Qual a quantidade de unidades do produto?'))
#primeiro if sem desconto
if (qntp < 5 and qntp > 0):
    desc = (valp * qntp)
# primeiro elif para saber o resultado da compra com apenas 3% de desconto. 5 a 19 unidades
elif(qntp >= 5 and qntp <= 19):
    desc = (valp * qntp )-(valp * qntp / 100 * 3)
# segundo elif para saber o resultado da compra com 6% de desconto. 20 a 99 unidades
elif(qntp >= 20 and qntp <= 99):
    desc = (valp * qntp)-(valp * qntp / 100 * 6)
# terceiro elif para saber o resultado da compra com 10% de desconto. 100 ou mais unidades
elif(qntp >= 100):
    desc = (valp * qntp)-(valp * qntp / 100 * 10)
# um else para caso as informações colocadas nao atingissem as especificações
else:
    print('Ocorreu um erro, por favor insira os dados novamente')
#retorno
print('O valor de sua compra sem desconto foi {}'.format(valp*qntp))
print('O valor de sua compra com descontou é de {}'.format(desc))