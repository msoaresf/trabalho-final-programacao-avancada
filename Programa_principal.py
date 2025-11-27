from Arquivar import ControleEstoque
from sistemaVendas import SistemaDeVendas

controle_estoque = ControleEstoque()
controle_vendas = SistemaDeVendas()


while True:
    print("----------------------------------------------------------------------\n"
    "==========================MENU PRINCIPAL===========================\n"
    "----------------------------------------------------------------------\n"
    "\n"
    "1 - Gerenciamento de estoque\n"
    "2 - Sistema de vendas\n"
    "0 - sair\n")
    try:
        opcao= int(input("Escolha: "))
    except ValueError:
        print("ERRO: A OPCAO DEVE SER UM NUMERO")
        continue
    except Exception as e:
        print(f"ERRO INESPERADO, DESCULPA :/ ->  {e}")
        continue
    match opcao:
        case 1:
                while True:

                    print("----------------------------------------------------------------------\n"
                    "====================SISTEMA DE CONTROLE DE ESTOQUE====================\n"
                    "----------------------------------------------------------------------\n"
                    "\n"
                    "1 - Cadastrar produto\n"
                    "2 - Listar produtos cadastrados\n"
                    "3 - Editar produto\n"
                    "4 - Excluir produto\n"
                    "5 - Gerar relatório\n"
                    "0 - Voltar ao menu principal")

                    try:
                        a = int(input("Escolha: "))
                        print("\n")

                        if a == 1:
                            controle_estoque.cadastrar_produto()
                        elif a == 2:
                            controle_estoque.listar_produtos()
                        elif a == 3:
                            controle_estoque.editar_produto()
                        elif a == 4:
                            controle_estoque.excluir_produto()
                        elif a == 5:
                            controle_estoque.gerar_relatorio()
                        elif a == 0:
                            print("SISTEMA ENCERRADO!")
                            break
                        else:
                            print("Valor inválido!\n")
                    except ValueError:
                        print("ERRO: Entrada inválida!\n"
                            "Por favor, digite um número.\n")
                    except Exception as e:
                        print(f"Ocorreu um erro inesperado: {e}.\n")
        case 2:
                while True:

                    print("----------------------------------------------------------------------\n"
                    "====================SISTEMA DE COTROLE DE VENDAS====================\n"
                    "----------------------------------------------------------------------\n"
                    "\n"
                    "1 - Realizar Venda\n"
                    "2 - Listar Vendas\n"
                    "3 - Analise das vendas\n"
                    "0 - Voltar ao menu principal\n")
                    try:
                        c = int(input("Escolha: "))
                        print("\n")
                        if c == 1:
                            controle_estoque.listar_produtos()
                            controle_vendas.adicionar()
                        elif c == 2:
                            controle_vendas.listar_vendas()
                        elif c == 3:
                            controle_vendas.analise()
                        elif c == 0:
                            print("SISTEMA ENCERRADO!")
                            break
                        else:
                            print("Valor inválido!\n")
                    except ValueError:
                        print("ERRO: Entrada inválida!\n"
                            "Por favor, digite um número.2\n")
                    except Exception as e:
                        print(f"Ocorreu um erro inesperado: {e}.\n")
        case 0:
                break 
        case _:
                print("Opção inválida! Tente novamente.")