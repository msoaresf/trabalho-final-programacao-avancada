import pickle

from Produtos import Produto

class ControleEstoque:

    n_arquivo = "estoque.pkl"

    def __init__(self):
        self.produtos = []
        self.descricoes_registradas = {}
        self.codigos_registrados = set()
        self._carregar_dados()

    def _carregar_dados(self):
        try:
            with open(self.n_arquivo, "rb") as estoque:
                self.produtos = pickle.load(estoque)
            self.codigos_registrados = {produto.codigo for produto in self.produtos}
            self.descricoes_registradas  = {produto.descricao for produto in self.produtos}
            print("DADOS CARREGADOS COM SUCESSO!")
        except FileNotFoundError:
            print("ERRO: Arquivo do estoque não encontrado!\n")
        except IOError:
            print("ERRO: Arquivo do estoque não pode ser acessado!\n")
        except pickle.PickleError:
            print("ERRO: Dados não podem ser carregados!\n")
        except EOFError:
            print("ERRO: Arquivo do estoque vazio ou corrompido!\n")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}.\n")

    def _salvar_dados(self):
        try:
            with open(self.n_arquivo, "wb") as estoque:
                pickle.dump(self.produtos, estoque)
        except FileNotFoundError:
            print("ERRO: Arquivo do estoque não encontrado!\n")
        except IOError:
            print("ERRO: Arquivo do estoque não pode ser acessado!\n")
        except pickle.PickleError:
            print("ERRO: Dados não podem ser salvos!\n")
        except EOFError:
            print("ERRO: Arquivo do estoque vazio ou corrompido!\n")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}.\n")

    def cadastrar_produto(self):
        try:
            descricao = input("Descrição: ").upper().replace(" ", "")
            if descricao in self.descricoes_registradas:
                print("Produto já registrado!")
                return
            codigo = int(input("Código: "))
            if codigo in self.codigos_registrados:
                print("Código já registrado!")
                return
            categoria = input("Categoria: ")
            if categoria.lower().replace(" ", "") not in ["fruta", "verdura", "legume"]:
                print("Categoria inválida!")
                return
            preco_compra = float(input("Preço de compra: "))
            preco_venda = float(input("Preço de venda: "))
            quantidade = float(input("Quantidade: "))

            novo_produto = Produto(codigo, descricao, categoria, preco_compra, preco_venda, quantidade)
            self.produtos.append(novo_produto)
            self.descricoes_registradas = {produto.descricao for produto in self.produtos}
            self.codigos_registrados.add(codigo)
            self._salvar_dados()
            print("Novo produto cadastrado com sucesso!\n")

        except ValueError:
            print("ERRO: Tipo de dado inválido.\n")
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}.\n")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.\n")
            return
        print("---------------------------\n"
              "------ LISTA DE PRODUTOS ------\n"
              "---------------------------")
        for i, produto in enumerate(self.produtos):
            print(f"Produto {i+1}: \n{produto}")
        print("---------------------------\n")

    def _encontrar_produto_por_codigo(self, codigo: int):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def _encontrar_produto_por_descricao(self, descricao: str):
        for produto in self.produtos:
            if produto.descricao == descricao.upper().replace(" ", ""):
                return produto
        return None

    def editar_produto(self):
        try:
            edicao = int(input("Deseja pesquisar o produto por:\n"
                               "1 - Código\n"
                               "2 - Descrição\n"
                               "Escolha: "))
            if edicao == 1:
                produto_editar = int(input("Código do produto que deseja editar: "))
                produto_para_editar = self._encontrar_produto_por_codigo(produto_editar)
            elif edicao == 2:
                produto_editar = input("Descrição do produto que deseja editar: ").upper().replace(" ", "")
                produto_para_editar = self._encontrar_produto_por_descricao(produto_editar)
            else:
                print("Entrada inválida!")
                return 

            if not produto_para_editar:
                print(f"Produto \"{produto_editar}\" não encontrado!\n")
                return

            print(f"Produto atual: \n{produto_para_editar}")
            editar = int(input("Deseja editar:\n" 
                               "1 - Descrição\n" 
                               "2 - Categoria\n" 
                               "3 - Preço de compra\n" 
                               "4 - Preço de venda\n"
                               "5 - Quantidade\n" 
                               "Número: "))

            if editar == 1:
                nova_descricao = input("Nova descrição: ").upper().replace(" ", "")
                if nova_descricao != produto_para_editar.descricao:
                    if nova_descricao in self.descricoes_registradas:
                        print(f"ERRO: O produto \"{nova_descricao}\" já está registrado.\n")
                        return
                    produto_para_editar.descricao = nova_descricao
                else:
                    print("A nova descrição do produto é a mesma que a atual.\n")
            elif editar == 2:
                nova_categoria = input("Nova categotia (fruta, verdura, legume): ")
                if nova_categoria not in ["fruta", "verdura", "legume"]:
                    print("Categoria inválida!\n")
                    return
                produto_para_editar.categoria = nova_categoria
            elif editar == 3:
                novo_preco_compra = float(input("Novo preço de compra: "))
                if novo_preco_compra >= 0:
                    produto_para_editar.preco_compra = format(novo_preco_compra, ".2f")
                else:
                    print("Preço não pode ser negativo!")
                    return
            elif editar == 4:
                novo_preco_venda = float(input("Novo preço de venda: "))
                if novo_preco_venda >= 0:
                    produto_para_editar.preco_venda = format(novo_preco_venda, ".2f")
                else:
                    print("Preço não pode ser negativo!")
                    return
            elif editar == 5:
                nova_quantidade = float(input("Quantidade (kg) adicionada ou retirada: "))
                produto_para_editar.quantidade = format(nova_quantidade, ".3f")
            else:
                print("ERRO: Valor inválido!\n")
                return

            self._salvar_dados()
            print("Produto editado e salvo com sucesso!\n")
            print(f"Resumo do produto editado: \n{produto_para_editar}\n")
        except ValueError:
            print("ERRO: Entrada inválida.\n")
        except Exception as e:
            print(f"Erro ao editar produto: {e}.\n")

    def excluir_produto(self):
        try:
            excluir = int(input("Deseja pesquisar o produto por:\n"
                               "1 - Código\n"
                               "2 - Descrição\n"
                               "Escolha: "))
            if excluir == 1:
                produto_excluir = int(input("Código do produto que deseja excluir: "))
                produto_para_excluir = self._encontrar_produto_por_codigo(produto_excluir)
            elif excluir == 2:
                produto_excluir = input("Descrição do produto que deseja excluir: ").upper().replace(" ", "")
                produto_para_excluir = self._encontrar_produto_por_descricao(produto_excluir)
            else:
                print("Entrada inválida!")
                return

            if not produto_para_excluir:
                print(f"Produto \"{produto_excluir}\" não encontrado!\n")
                return

            print(f"Produto atual: \n{produto_para_excluir}")

            escolha = int(input("Deseja realmente excuir o produto acima?\n"
                                "1 - SIM\n"
                                "2 - NÃO\n"))

            if escolha == 1:
                self.produtos.remove(produto_para_excluir)
                self.descricoes_registradas = {produto.descricao for produto in self.produtos}
                self.codigos_registrados.remove(produto_para_excluir.codigo)
                self._salvar_dados()
                print(f"Produto \"{produto_excluir}\" excluído com sucesso!\n")
            elif escolha == 2:
                print("AÇÃO CANCELADA!")
                return
            else:
                print("Entrada inválida!")
                return

        except ValueError:
            print("ERRO: O código deve ser um número inteiro.\n")
        except Exception as e:
            print(f"Erro ao excluir produto: {e}\n")

    def gerar_relatorio(self):
        if not self.produtos:
            print("Nenhum produto cadastrado!\n")
            return

        preco_compra = [float(produto.preco_compra) for produto in self.produtos]
        preco_venda = [float(produto.preco_venda) for produto in self.produtos]
        quantidade_estoque = [float(produto.quantidade) for produto in self.produtos]

        i = fruta = verdura = legume = 0

        for produto in self.produtos:
            if produto.categoria == "fruta":
                fruta += 1
            elif produto.categoria == "verdura":
                verdura += 1
            else:
                legume += 1

        print(f"----------------------------- Relatório dos Produtos -----------------------------\n"
              f"Total de produtos cadastrados: {len(self.produtos)}\n"
              f"Total de frutas: {fruta}\n"
              f"Total de verduras: {verdura}\n"
              f"Total de legumes: {legume}\n"
              f"__________________________________________________________________________________\n"
              f"| Descrição | Quantidade (kg) | Valor compra total (R$) | Valor venda total (R$) |")
        for produto in self.produtos:

            preco_compra_estoque = format(preco_compra[i] * quantidade_estoque[i], ".2f")
            preco_venda_estoque = format(preco_venda[i] * quantidade_estoque[i], ".2f")
            i += 1

            print(f"__________________________________________________________________________________\n"
                  f"|{produto.descricao:^{11}}|{produto.quantidade:^{17}}|{preco_compra_estoque:^{25}}|{preco_venda_estoque:^{24}}|\n"
                  f"__________________________________________________________________________________")