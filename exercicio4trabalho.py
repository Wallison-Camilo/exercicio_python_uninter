print('Aluno Wallison camilo rosa RU: 3947124 e este é meu programa')
print('Bem vindo ao controle de estoque de mercearia do Wallison Camilo')
listaprodutos = []
codigodoproduto = 0
#funçao de cadastro dos produtos
def cadastrarProduto():
    while True:
        print('Você selecionou a opção de Cadastrar Produtos')
        print('Codigo do produto 00{}'.format(codigodoproduto))
        nome = input('Por Favor entre com o nome do Produto: ')
        fabricante = input('Por Favor entre com o Fabricante do Produto: ')
        valor = float(input('Por Favor entre com o VALOR(R$) do Produto: '))
        codigo = codigodoproduto
        produtos = {'codigo': [], 'nome': [], 'fabricante': [], 'valor': []}
        produtos['nome'].append(nome)
        produtos['fabricante'].append(fabricante)
        produtos['valor'].append(float(valor))
        produtos['codigo'].append(codigo)
        listaprodutos.append(produtos.copy())
        break
#funçao de consulta dos produtos
def consultarProduto():
    while True:
        print('Você selecionou a opção de Consultar Produto')
        print('Escolha a opção desejada:')
        print('1- Consultar todos os Produtos')
        print('2- Consultar produto por Código')
        print('3- Consultar produto por Fabricante')
        print('4- retornar')
        resp = int(input('>>'))
        #if para consultar todos os produtos
        if resp == 1:
            for produtos in listaprodutos:
                for chave,valor in produtos.items():
                    for dado in valor:
                        print('{} : {}'.format(chave,dado))
        #elif para consultar um produto pelo codigo dele
        elif resp == 2:
            dg = int(input('Digite o CODIGO do produto:'))
            for produtos in listaprodutos:
                if (produtos['codigo'][0] == dg):
                    for chave, valor in produtos.items():
                        for dado in valor:
                            print('{} : {}'.format(chave,dado))
        #elif para consultar um produto pelo seu fabricante
        elif resp == 3:
            dg = input('Digite o FABRICANTE do(s) produto(s):')
            for produtos in listaprodutos:
                if (produtos['fabricante'][0] == dg):
                    for chave, valor in produtos.items():
                        for dado in valor:
                            print('{} : {}'.format(chave, dado))
        #elif para sair do laço
        elif resp == 4:
            break
#funçao de remover o produto
def removerProduto():
    print('Você selecionou a opção de Remover Produto')
    dg = int(input('Digite o CODIGO do produto que deseja remover: '))
    for produtos in listaprodutos:
        if (produtos['codigo'][0] == dg):
            listaprodutos.remove(produtos)

#Main
while True:
    print('Escolha a opção desejada:')
    print('1- Cadastrar produto')
    print('2- Consultar produto(s)')
    print('3- Remove produto')
    print('4- Sair')
    entrada = int(input('>>'))
    #chamada da funçao de cadastro
    if entrada == 1:
        codigodoproduto += 1
        cadastrarProduto()
        continue
    #chamada da funçao de consulta
    elif entrada == 2:
        consultarProduto()
    #cadastro da funçao de romoçao
    elif entrada == 3:
        removerProduto()
    #saida do programa
    elif entrada == 4:
        break