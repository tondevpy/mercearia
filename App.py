import sys
from Funcoes import (
    cadastrarFuncionario, editarFuncionario, cadastrarCliente, cadastrarFornecedor, cadastrarProduto, editarCliente, editarFornecedor,
    editarProduto, excluirProduto, excluirFornecedor, registrarEntradaSaida, atualizarEstoque, relatorioEstoqueAtual, excluirCliente, 
    exibirBaixoEstoque, registrarVenda, gerarRelatorioVendas, relatorioProdutosMaisVendidos, gerarRecibo
)

def menu():
    while True:
        print('--- Menu Principal ---')
        print('[1] - Cadastro de Funcionários')
        print('[2] - Cadastro de Produtos')
        print('[3] - Gerenciamento de Estoque')
        print('[4] - Venda de Produtos')
        print('[5] - Relatórios')
        print('[6] - Cadastro de Fornecedores')
        print('[7] - Cadastro de Clientes')
        print('[0] - Sair')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            menuFuncionarios()
        elif opcao == '2':
            menuProdutos()
        elif opcao == '3':
            menuEstoque()
        elif opcao == '4':
            menuVendas()
        elif opcao == '5':
            menuRelatorios()
        elif opcao == '6':
            menuFornecedores()
        elif opcao == '7':
            menuClientes()
        elif opcao == '0':
            print('Saindo...')
            sys.exit()
        else:
            print('Opção inválida!')

def menuFuncionarios():
    while True:
        print('--- Cadastro de Funcionários ---')
        print('[1] - Cadastrar Funcionário')
        print('[2] - Editar Funcionário')
        print('[0] - Voltar')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrarFuncionario()
        elif opcao == '2':
            editarFuncionario()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

def menuProdutos():
    while True:
        print('--- Cadastro de Produtos ---')
        print('[1] - Cadastrar Produto')
        print('[2] - Editar Produto')
        print('[3] - Excluir Produto')
        print('[0] - Voltar')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrarProduto()
        elif opcao == '2':
            editarProduto()
        elif opcao == '3':
            excluirProduto()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

def menuEstoque():
    while True:
        print('--- Gerenciamento de Estoque ---')
        print('[1] - Atualizar Estoque')
        print('[2] - Exibir Produtos em Baixo Estoque')
        print('[3] - Registrar Entrada/Saída de Produtos')
        print('[0] - Voltar')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            atualizarEstoque()
        elif opcao == '2':
            exibirBaixoEstoque()
        elif opcao == '3':
            registrarEntradaSaida()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

def menuVendas():
    while True:
        print('--- Venda de Produtos ---')
        print('[1] - Registrar Venda')
        print('[2] - Gerar Recibo')
        print('[0] - Voltar')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            registrarVenda()
        elif opcao == '2':
            gerarRecibo()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

def menuRelatorios():
    while True:
        print('--- Relatórios ---')
        print('[1] - Relatório de Vendas')
        print('[2] - Relatório de Produtos Mais Vendidos')
        print('[3] - Relatório de Estoque Atual')
        print('[0] - Voltar')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            periodo = input('Informe o período (diário, semanal, mensal, anual): ')
            gerarRelatorioVendas(periodo)
        elif opcao == '2':
            relatorioProdutosMaisVendidos()
        elif opcao == '3':
            relatorioEstoqueAtual()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

def menuFornecedores():
    while True:
        print('--- Cadastro de Fornecedores ---')
        print('[1] - Cadastrar Fornecedor')
        print('[2] - Editar Fornecedor')
        print('[3] - Excluir Fornecedor')
        print('[0] - Voltar')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrarFornecedor()
        elif opcao == '2':
            editarFornecedor()
        elif opcao == '3':
            excluirFornecedor()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

def menuClientes():
    while True:
        print('--- Cadastro de Clientes ---')
        print('[1] - Cadastrar Cliente')
        print('[2] - Editar Cliente')
        print('[3] - Excluir Cliente')
        print('[0] - Voltar')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrarCliente()
        elif opcao == '2':
            editarCliente()
        elif opcao == '3':
            excluirCliente()
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()
