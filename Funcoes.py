import json  # Importa o módulo json para manipulação de arquivos JSON
import os

def cadastrarFuncionario():
    # Solicita as informações básicas do funcionário e converte o nome e sexo para minúsculas
    nome = input('Nome do funcionário: ').lower()
    sexo = input('Sexo do funcionário: ').lower()
    cpf = input('CPF do funcionário: ')

    # Verifica se os campos obrigatórios foram preenchidos
    if nome and sexo and cpf:
        print('Informe a data de nascimento do funcionário OBS: Informar apenas o que foi solicitado.')
        
        # Solicita a data de nascimento do funcionário
        dia = input('Dia de nascimento: ')
        mes = input('Mês de nascimento: ')
        ano = input('Ano de nascimento: ')
        
        # Verifica se todos os campos da data de nascimento foram preenchidos
        if dia and mes and ano:
            # Formata a data de nascimento e cria um dicionário com os dados do funcionário
            idade = f'{dia}/{mes}/{ano}'
            registro = {'nome': nome, 'sexo': sexo, 'cpf': cpf, 'idade': idade, 'vendas': 0}
            
            try:
                # Tenta abrir o arquivo 'funcionarios.json' no modo de leitura
                with open('funcionarios.json', 'r', encoding='utf-8') as file:
                    funcionarios = json.load(file)  # Carrega os dados existentes no arquivo JSON
            except (FileNotFoundError, json.JSONDecodeError):
                # Se o arquivo não existir ou estiver vazio/inválido, inicializa uma lista vazia
                funcionarios = []

            # Adiciona o novo registro de funcionário à lista
            funcionarios.append(registro)

            # Abre o arquivo 'funcionarios.json' no modo de escrita para salvar os dados atualizados
            with open('funcionarios.json', 'w', encoding='utf-8') as file:
                # Grava a lista de funcionários atualizada no arquivo JSON
                json.dump(funcionarios, file, ensure_ascii=False, indent=4)

            # Informa ao usuário que o funcionário foi cadastrado com sucesso
            print('Funcionário cadastrado com sucesso!')
        else:
            # Informa ao usuário que todos os campos da data de nascimento precisam ser preenchidos
            print('Todos os campos precisam ser preenchidos!')
    else:
        # Informa ao usuário que todos os campos obrigatórios devem ser preenchidos para o cadastro
        print('Preencha todos os campos corretamente para realizar o cadastro do funcionário.')

def editarFuncionario():
    # abrir o arquivo e carregar os dados dele 
    try:
        with open('funcionarios.json', 'r', encoding='utf-8') as arq:
            registro = json.load(arq)
            nome = input('Informe o nome do funcionário: ').lower()
            if nome:
                for funcionario in registro:
                # localizar funcionario
                    if funcionario['nome'] == nome:
                        print('Quais dados deseja alterar ? ')
                        print('[1] - nome\n[2] sexo\n[3] - CPF\n[4] - Idade\n[5] - Adicionar venda\n[6] - sair')
                        opcao = input('Informe a opção desejada: ')
                        if opcao == '1':
                            novoNome = input('Informe o novo nome: ')
                            funcionario['nome'] = novoNome
                            print('Nome alterado com sucesso!')
                        elif opcao == '2':
                            novoSexo = input('Informe o novo sexo: ')
                            funcionario['sexo'] = novoSexo
                            print('Sexo alterado com sucesso!')
                        elif opcao == '3':
                            novoCPF = input('Informe o novo cpf: ')
                            funcionario['cpf'] = novoCPF
                            print('O novo cpf foi atualizado')
                        elif opcao == '4':
                            print('Informe o novo nascimento: ')
                            dia = input('dia: ')
                            mes = input('mes: ')
                            ano = input('ano: ')
                            funcionario['idade'] = f"{dia}/{mes}/{ano}"
                            print('Idade alterada com sucesso!')
                            quantidade = int(input('Informe a quantidade de vendas a ser adicionada: '))
                            funcionario['vendas'] += quantidade
                            print('Vendas adicionadas com sucesso!')
                        elif opcao == '5':
                            print('Finalizado')
                            break
                        else:
                            print('Ocorreu um erro! ou informou algum dado inválido')       
            else:
                print('Nome não informado!')

        with open('funcionarios.json','w', encoding='utf-8') as arq:
            json.dump(registro, arq, ensure_ascii=False, indent=4)
                
    except:
        print('O arquivo "funcionarios.json" não existe!')

import json

def cadastrarProduto():
    nome = input('Nome do produto: ').lower()
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade em estoque: '))

    if nome and preco and quantidade:
        produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}

        try:
            with open('produtos.json', 'r', encoding='utf-8') as file:
                produtos = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            produtos = []

        produtos.append(produto)

        with open('produtos.json', 'w', encoding='utf-8') as file:
            json.dump(produtos, file, ensure_ascii=False, indent=4)

        print('Produto cadastrado com sucesso!')
    else:
        print('Preencha todos os campos corretamente para realizar o cadastro do produto.')

def editarProduto():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            nome = input('Informe o nome do produto: ').lower()
            if nome:
                for produto in produtos:
                    if produto['nome'] == nome:
                        print('Quais dados deseja alterar ? ')
                        print('[1] - Nome\n[2] Preço\n[3] Quantidade\n[4] - Sair')
                        opcao = input('Informe a opção desejada: ')
                        if opcao == '1':
                            novoNome = input('Informe o novo nome: ').lower()
                            produto['nome'] = novoNome
                            print('Nome alterado com sucesso!')
                        elif opcao == '2':
                            novoPreco = float(input('Informe o novo preço: '))
                            produto['preco'] = novoPreco
                            print('Preço alterado com sucesso!')
                        elif opcao == '3':
                            novaQuantidade = int(input('Informe a nova quantidade: '))
                            produto['quantidade'] = novaQuantidade
                            print('Quantidade alterada com sucesso!')
                        elif opcao == '4':
                            print('Finalizado')
                            break
                        else:
                            print('Ocorreu um erro! ou informou algum dado inválido')       
            else:
                print('Nome não informado!')

        with open('produtos.json','w', encoding='utf-8') as arq:
            json.dump(produtos, arq, ensure_ascii=False, indent=4)
                
    except:
        print('O arquivo "produtos.json" não existe!')

def excluirProduto():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            nome = input('Informe o nome do produto a ser excluído: ').lower()
            if nome:
                produtos = [produto for produto in produtos if produto['nome'] != nome]

                with open('produtos.json','w', encoding='utf-8') as arq:
                    json.dump(produtos, arq, ensure_ascii=False, indent=4)
                print('Produto excluído com sucesso!')
            else:
                print('Nome não informado!')
                
    except:
        print('O arquivo "produtos.json" não existe!')


def atualizarEstoque():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            nome = input('Informe o nome do produto: ').lower()
            if nome:
                for produto in produtos:
                    if produto['nome'] == nome:
                        novaQuantidade = int(input('Informe a nova quantidade em estoque: '))
                        produto['quantidade'] = novaQuantidade
                        print('Estoque atualizado com sucesso!')

        with open('produtos.json','w', encoding='utf-8') as arq:
            json.dump(produtos, arq, ensure_ascii=False, indent=4)
                
    except:
        print('O arquivo "produtos.json" não existe!')

def exibirBaixoEstoque():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            baixoEstoque = [produto for produto in produtos if produto['quantidade'] < 10]
            for produto in baixoEstoque:
                print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}")

    except:
        print('O arquivo "produtos.json" não existe!')

def registrarEntradaSaida():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            nome = input('Informe o nome do produto: ').lower()
            if nome:
                for produto in produtos:
                    if produto['nome'] == nome:
                        tipo = input('Registrar [E]ntrada ou [S]aída de produto? ').lower()
                        quantidade = int(input('Informe a quantidade: '))
                        if tipo == 'e':
                            produto['quantidade'] += quantidade
                            print('Entrada registrada com sucesso!')
                        elif tipo == 's':
                            produto['quantidade'] -= quantidade
                            print('Saída registrada com sucesso!')
                        else:
                            print('Opção inválida!')

        with open('produtos.json','w', encoding='utf-8') as arq:
            json.dump(produtos, arq, ensure_ascii=False, indent=4)
                
    except:
        print('O arquivo "produtos.json" não existe!')


def registrarVenda():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            vendas = []

            nome = input('Informe o nome do produto vendido: ').lower()
            if nome:
                for produto in produtos:
                    if produto['nome'] == nome:
                        quantidadeVendida = int(input('Informe a quantidade vendida: '))
                        if quantidadeVendida <= produto['quantidade']:
                            produto['quantidade'] -= quantidadeVendida
                            valorVenda = produto['preco'] * quantidadeVendida
                            print(f'Valor da venda: R${valorVenda:.2f}')
                            formaPagamento = input('Informe a forma de pagamento (dinheiro/cartão): ').lower()
                            
                            venda = {
                                'produto': nome,
                                'quantidade': quantidadeVendida,
                                'valor': valorVenda,
                                'forma_pagamento': formaPagamento
                            }
                            vendas.append(venda)
                            print('Venda registrada com sucesso!')

                            # Salvar a venda em um arquivo de comprovante
                            if not os.path.exists('comprovantes_vendas'):
                                os.makedirs('comprovantes_vendas')

                            with open(f'comprovantes_vendas/comprovante_{nome}_{quantidadeVendida}.json', 'w', encoding='utf-8') as file:
                                json.dump(venda, file, ensure_ascii=False, indent=4)

                        else:
                            print('Quantidade vendida maior do que a disponível em estoque!')

        with open('vendas.json', 'w', encoding='utf-8') as arq:
            json.dump(vendas, arq, ensure_ascii=False, indent=4)

        with open('produtos.json','w', encoding='utf-8') as arq:
            json.dump(produtos, arq, ensure_ascii=False, indent=4)
                
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def gerarRecibo():
    try:
        with open('vendas.json', 'r', encoding='utf-8') as arq:
            vendas = json.load(arq)
            total = 0
            print('Recibo:')
            for venda in vendas:
                print(f"Produto: {venda['produto']}, Quantidade: {venda['quantidade']}, Valor: {venda['valor']}")
                total += venda['valor']
            print(f"Total: {total}")
                
    except:
        print('O arquivo "vendas.json" não existe!')


def gerarRelatorioVendas(periodo):
    try:
        with open('vendas.json', 'r', encoding='utf-8') as arq:
            vendas = json.load(arq)
            # Aqui deve-se adicionar a lógica de filtragem das vendas pelo período desejado
            # Por enquanto, vamos apenas exibir todas as vendas
            for venda in vendas:
                print(f"Produto: {venda['produto']}, Quantidade: {venda['quantidade']}, Valor: {venda['valor']}")

    except:
        print('O arquivo "vendas.json" não existe!')

def relatorioProdutosMaisVendidos():
    try:
        with open('vendas.json', 'r', encoding='utf-8') as arq:
            vendas = json.load(arq)
            # Lógica para calcular os produtos mais vendidos
            produtosVendidos = {}
            for venda in vendas:
                produto = venda['produto']
                if produto in produtosVendidos:
                    produtosVendidos[produto] += venda['quantidade']
                else:
                    produtosVendidos[produto] = venda['quantidade']
            maisVendidos = sorted(produtosVendidos.items(), key=lambda x: x[1], reverse=True)
            for produto, quantidade in maisVendidos:
                print(f"Produto: {produto}, Quantidade vendida: {quantidade}")

    except:
        print('O arquivo "vendas.json" não existe!')

def relatorioEstoqueAtual():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            for produto in produtos:
                print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}")

    except:
        print('O arquivo "produtos.json" não existe!')


def cadastrarFornecedor():
    nome = input('Nome do fornecedor: ').lower()
    cnpj = input('CNPJ do fornecedor: ')

    if nome and cnpj:
        fornecedor = {'nome': nome, 'cnpj': cnpj}

        try:
            with open('fornecedores.json', 'r', encoding='utf-8') as file:
                fornecedores = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            fornecedores = []

        fornecedores.append(fornecedor)

        with open('fornecedores.json', 'w', encoding='utf-8') as file:
            json.dump(fornecedores, file, ensure_ascii=False, indent=4)

        print('Fornecedor cadastrado com sucesso!')
    else:
        print('Preencha todos os campos corretamente para realizar o cadastro do fornecedor.')

def editarFornecedor():
    try:
        with open('fornecedores.json', 'r', encoding='utf-8') as arq:
            fornecedores = json.load(arq)
            nome = input('Informe o nome do fornecedor: ').lower()
            if nome:
                for fornecedor in fornecedores:
                    if fornecedor['nome'] == nome:
                        print('Quais dados deseja alterar ? ')
                        print('[1] - Nome\n[2] CNPJ\n[3] - Sair')
                        opcao = input('Informe a opção desejada: ')
                        if opcao == '1':
                            novoNome = input('Informe o novo nome: ').lower()
                            fornecedor['nome'] = novoNome
                            print('Nome alterado com sucesso!')
                        elif opcao == '2':
                            novoCNPJ = input('Informe o novo CNPJ: ')
                            fornecedor['cnpj'] = novoCNPJ
                            print('CNPJ alterado com sucesso!')
                        elif opcao == '3':
                            print('Finalizado')
                            break
                        else:
                            print('Ocorreu um erro! ou informou algum dado inválido')       
            else:
                print('Nome não informado!')

        with open('fornecedores.json','w', encoding='utf-8') as arq:
            json.dump(fornecedores, arq, ensure_ascii=False, indent=4)
                
    except:
        print('O arquivo "fornecedores.json" não existe!')

def excluirFornecedor():
    try:
        with open('fornecedores.json', 'r', encoding='utf-8') as arq:
            fornecedores = json.load(arq)
            nome = input('Informe o nome do fornecedor a ser excluído: ').lower()
            if nome:
                fornecedores = [fornecedor for fornecedor in fornecedores if fornecedor['nome'] != nome]

                with open('fornecedores.json','w', encoding='utf-8') as arq:
                    json.dump(fornecedores, arq, ensure_ascii=False, indent=4)
                print('Fornecedor excluído com sucesso!')
            else:
                print('Nome não informado!')
                
    except:
        print('O arquivo "fornecedores.json" não existe!')


def cadastrarCliente():
    nome = input('Nome do cliente: ').lower()
    cpf = input('CPF do cliente: ')

    if nome and cpf:
        cliente = {'nome': nome, 'cpf': cpf}

        try:
            with open('clientes.json', 'r', encoding='utf-8') as file:
                clientes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            clientes = []

        clientes.append(cliente)

        with open('clientes.json', 'w', encoding='utf-8') as file:
            json.dump(clientes, file, ensure_ascii=False, indent=4)

        print('Cliente cadastrado com sucesso!')
    else:
        print('Preencha todos os campos corretamente para realizar o cadastro do cliente.')

def editarCliente():
    try:
        with open('clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            nome = input('Informe o nome do cliente: ').lower()
            if nome:
                for cliente in clientes:
                    if cliente['nome'] == nome:
                        print('Quais dados deseja alterar ? ')
                        print('[1] - Nome\n[2] CPF\n[3] - Sair')
                        opcao = input('Informe a opção desejada: ')
                        if opcao == '1':
                            novoNome = input('Informe o novo nome: ').lower()
                            cliente['nome'] = novoNome
                            print('Nome alterado com sucesso!')
                        elif opcao == '2':
                            novoCPF = input('Informe o novo CPF: ')
                            cliente['cpf'] = novoCPF
                            print('CPF alterado com sucesso!')
                        elif opcao == '3':
                            print('Finalizado')
                            break
                        else:
                            print('Ocorreu um erro! ou informou algum dado inválido')       
            else:
                print('Nome não informado!')

        with open('clientes.json','w', encoding='utf-8') as arq:
            json.dump(clientes, arq, ensure_ascii=False, indent=4)
                
    except:
        print('O arquivo "clientes.json" não existe!')

def excluirCliente():
    try:
        with open('clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            nome = input('Informe o nome do cliente a ser excluído: ').lower()
            if nome:
                clientes = [cliente for cliente in clientes if cliente['nome'] != nome]

                with open('clientes.json','w', encoding='utf-8') as arq:
                    json.dump(clientes, arq, ensure_ascii=False, indent=4)
                print('Cliente excluído com sucesso!')
            else:
                print('Nome não informado!')
                
    except:
        print('O arquivo "clientes.json" não existe!')
