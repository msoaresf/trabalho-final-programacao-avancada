from Arquivar import ControleEstoque
from datetime import datetime
import pickle
import numpy as np
import random
from colorama import Fore, init
init()

estoque = ControleEstoque()


class Historico: 
    """
    Classe que representa uma venda finalizada.
    Armazena o código da transação, data, lista de produtos vendidos e o valor total.
    """
    def __init__(self,cod:int,data:str,produtos:str,valorTotal:float):
        """
        Inicializa um registro de histórico de venda.

        codigo: Código único da transação.
        data: Data e hora da venda.
        produtos: Lista de dicionários dos itens vendidos.
        total: Valor total da venda.
        """
        self.__cod = cod
        self._data = data
        self._produtos = produtos
        self._valorTotal = valorTotal
    def __str__(self):
        """
        Retorna uma representação em string formatada da venda para exibição no histórico.
        """
        saida = Fore.MAGENTA +f"\nResgistro de venda\nData: {self._data}\nProdutos comprados:\n"
        for i in self._produtos:
            saida += (
                f"Produto: {i['produto']} | "
                f"Valor por kg: {float(i['preco_unitario']):.2f} | "
                f"Quantidade: {i['quantidade']} | "
                f"Valor total por item: {float(i['subtotal']):.2f}\n"
            )

        saida += f"\nValor da Compra: {float(self._valorTotal):.2f}"
        return saida
    
class SistemaDeVendas:
    """
    Gerencia o processo de vendas, o carrinho de compras e o histórico de transações.
    Também é responsável pela análise estatística das vendas.
    """
    def __init__(self):
        self.__carrinho = []
        self.__registro = []
        self._precoTotal = []
        self._carregar_dados()

    def _carregar_dados(self): #carrega os dados do arquivo historico
        try:
            with open("historicoDeVendas", "rb") as historico:
                dadosCarregados = pickle.load(historico)
            self.__registro = dadosCarregados
        except FileNotFoundError:
            print(Fore.RED + "ERRO: Arquivo do estoque não encontrado!\n")
        except IOError:
            print(Fore.RED + "ERRO: Arquivo do estoque não pode ser acessado!\n")
        except pickle.PickleError:
            print(Fore.RED +"ERRO: Dados não podem ser carregados!\n")
        except EOFError:
            print(Fore.RED +"ERRO: Arquivo do estoque vazio ou corrompido!\n")
        except Exception as e:
            print(Fore.RED +f"Erro ao carregar dados: {e}.\n")

    def _salvar_dados(self):# salva os dados no arquivo historico
        try:
            with open("historicoDeVendas", "wb") as historico:
                pickle.dump(self.__registro, historico)
        except FileNotFoundError:
            print(Fore.RED +"ERRO: Arquivo do estoque não encontrado!\n")
        except IOError:
            print(Fore.RED +"ERRO: Arquivo do estoque não pode ser acessado!\n")
        except pickle.PickleError:
            print(Fore.RED +"ERRO: Dados não podem ser salvos!\n")
        except EOFError:
            print(Fore.RED +"ERRO: Arquivo do estoque vazio ou corrompido!\n")
        except Exception as e:
            print(Fore.RED + f"Erro ao salvar dados: {e}.\n")


    def adicionar(self): # adiciono itens na venda
        """
        Inicia o processo de venda, permitindo ao usuário adicionar produtos ao carrinho
        e verificar a disponibilidade em estoque.
        """

        while True:
            produto_nome = input("\nProduto para adicionar ao carrinho: ")
            produto = estoque._encontrar_produto_por_descricao(produto_nome) #procuro o produto
            if produto_nome == "0":
                break
            if produto:
                try:
                    quantidade = float(input("Quantidade em kg: ")) #recebo a quantidade de produto que vai ser vendida
                except ValueError:
                    print(Fore.RED +"ERRO: A OPCAO DEVE SER UM NUMERO")
                    continue
                except Exception as e:
                    print(Fore.RED +f"ERRO INESPERADO, DESCULPA :/ ->  {e}")
                    continue
                preco = float(produto.preco_venda)
                precoCompra = float(produto.preco_compra)

                estoque_disponivel = float(produto.quantidade)

                if quantidade > estoque_disponivel: #verifico disponibilidade
                    print(Fore.RED +"Estoque insuficiente.")
                    continue

                subtotal = preco * quantidade #calculo o valor por item 
                subtotalCompra = precoCompra * quantidade #salvando para analise 

                self._precoTotal.append(subtotal) # adiciono na lista o valor da quantidade do item tal

                #salfo o item como um dicionario
                item = {
                    "produto": produto.descricao,
                    "quantidade": quantidade,
                    "preco_unitario": produto.preco_venda,
                    "subtotal": subtotal,
                    "subtotalcompra": subtotalCompra
                }

                self.__carrinho.append(item) #adiciono no carrinho o item

                print(Fore.WHITE+f"Adicionado: {produto.descricao} | {quantidade}kg | R$ {subtotal:.2f}")
            else:
                print(Fore.RED+ "Entrada invalida, verifique se o produto esta cadastrado")
                continue
            
            try:
                op = int(input(Fore.MAGENTA + "1 - Continuar | 2 - Finalizar venda: "))
            except ValueError:
                print(Fore.RED +"ERRO: A OPCAO DEVE SER UM NUMERO")
                continue
            except Exception as e:
                print(Fore.RED +f"ERRO INESPERADO, DESCULPA :/ ->  {e}")
                continue
            if op == 2:
                self.finalizar_venda()
                return
            elif op ==1:
                continue
            else: 
                return

    def finalizar_venda(self):
        """
        Finaliza a venda atual, registra a transação no histórico e atualiza o estoque.
        """
        codigo = random.randint(1, 5000) #codigo aleatorio, para nao ter que criar um codigo para compra, ele e gerado alerotiamente 
        data = datetime.now() #pego a data e hora da compra
        total = np.sum(self._precoTotal) # e o valor total

        venda = Historico(codigo, data, self.__carrinho, total)
        self.__registro.append(venda)
        self._salvar_dados()
        #atualizar estoque 
        for item in self.__carrinho:#na lista carrinho tem os itens que foram vendidos nessa compra
            prod = estoque._encontrar_produto_por_descricao(item["produto"]) #procuta o produto que vai ter o valor alterado
            prod.quantidade = float(prod.quantidade) - float(item["quantidade"])#atualiza a quantidade

        estoque._salvar_dados()#salva a nova quantidae

        print(Fore.GREEN +"\nVENDA FINALIZADA")
        print(venda)

        self.__carrinho.clear()
        self._precoTotal.clear()#limpo carrinho

    def listar_vendas(self):#listo as vendas
        self._carregar_dados()
        print(Fore.CYAN + "\n--- HISTÓRICO DE VENDAS ---")
        if not self.__registro:
            print(Fore.RED + "Ainda não foi registrada nenhuma venda")
        else:
            for venda in self.__registro: 
                print(venda)

    def analise(self):
        """
        Realiza a análise estatística das vendas registradas, utilizando NumPy
        para calcular métricas como lucro total, média de lucro por item,
        e identificar o produto e a categoria mais lucrativos, alem do item que mais vende e o que menos vende.
        """
        if not self.__registro:
            print("Nenhuma venda registrada.")
            return

        print(Fore.RED + "\nAnalise das vendas\n")

        produtos = {}
        categorias = {}
        lucros = []

        for venda in self.__registro:#for no registro, que tem armazenado o historico de compras
            for item in venda._produtos:#Entro no proddutos vendidos
                #SALvo os dados em variaveis
                nome = item["produto"]
                quantidade = float(item["quantidade"])
                subtotal_venda = float(item["subtotal"])
                subtotal_compra = float(item.get("subtotalcompra", 0.0))#get aqui ferifica se tem valor se nao ele devolve o 0.0 e nao da erro
                
                lucro = subtotal_venda - subtotal_compra#calculo o luco por produto
                lucros.append(lucro)#adiciono o lucro na lista lucos

                prod_estoque = estoque._encontrar_produto_por_descricao(nome)#procuro o produto pelo nome
                #se produto estoque existir salvo a categirua
                if prod_estoque:
                    categoria = prod_estoque.categoria
                else:
                    categoria = "DESCONHECIDA"

                #se ainda nao existir em produtos o produto crio ele na lista em formato de dicionario
                if nome not in produtos:
                    produtos[nome] = {
                        "quantidade": 0.0,
                        "lucro": 0.0,
                        "receita": 0.0,
                        "categoria": categoria
                    }
                
                #adiciono os novos valores no dicionario
                produtos[nome]["quantidade"] += quantidade
                produtos[nome]["lucro"] += lucro
                produtos[nome]["receita"] += subtotal_venda
 
                #
                if categoria in categorias:# se categoria ja existe em categorias eu somo o lucro da categoria
                    categorias[categoria] = categorias[categoria] + lucro
                else:#se nao eu adiciono 
                    categorias[categoria] = 0.0 + lucro

        print(Fore.CYAN+'\n-----------Lucro geral--------------')
        lucro_total = np.sum(lucros)
        print(f"\nLucro total: R$ {lucro_total:.2f}")
        #numpy para ver a soma de todos os valores de lucro

        if lucros:
            media_lucro = np.mean(lucros)#media
        else:
            media_lucro = 0.0
        print(f"Média de lucro: R$ {media_lucro:.2f}")

        print('\n-----------Lucro por item--------------\n')
        for nome, dados in produtos.items(): #for nos produtos so para printar ele e os valores
            print(f"{nome} ({dados['categoria']}): R$ {dados['lucro']:.2f}")
        
        #para ver qual o produto com maior lucro
        if produtos:
            lucros_produtos =[]
            for dados in produtos.values():# cria um array com todos os lucros
                lucroProduto = dados["lucro"] 
                lucros_produtos.append(lucroProduto)

            
            maior_lucro_valor = np.max(lucros_produtos)  #descubro o maior valor        
            maior_lucro_nome = ""

            for nome, dados in produtos.items():
                if dados["lucro"] == maior_lucro_valor: #procuto o maior valor e acho o nome dele
                    maior_lucro_nome = nome
                    break 
            
            print(f"\nProduto com maior lucro: {maior_lucro_nome} (R$ {maior_lucro_valor:.2f})") #printo o nome e valor
                #para ver qual o produto com maior lucro
        if produtos:
            quantidadevendida =[]
            for dados in produtos.values():# cria um array com todos os lucros
                qtt = dados["quantidade"] 
                quantidadevendida.append(qtt)

            
            maisvendido = np.max(quantidadevendida)  #descubro o maior valor        
            maisvendidonome = ""
            menosvendido = np.min(quantidadevendida)  #descubro o maior valor        
            menosvendidonome = ""

            for nome, dados in produtos.items():
                if dados["quantidade"] == maisvendido: #procuto o maior valor e acho o nome dele
                    maisvendidonome = nome
                    break
            for nome, dados in produtos.items():
                if dados["quantidade"] == menosvendido: #procuto o maior valor e acho o nome dele
                    menosvendidonome = nome
                    break 
            
            print(f"\nProduto mais vendido: {maisvendidonome} ({maisvendido:.2f}KG)") #printo o nome e valor
            print(f"Produto menos vendido: {menosvendidonome} ({menosvendido:.2f}KG)") #printo o nome e valor

        print('\n-----------Lucro por categoria--------------')

        print("\nLucro por categoria:")#aqui eu printo o lucro por categoria
        for cat, valor in categorias.items():
            print(f"{cat}: R$ {valor:.2f}")
            
        if categorias:
            lucros_categorias = np.array(list(categorias.values()))#cria uma lista com os valores da categoria
            indice_maior_lucro_cat = np.argmax(lucros_categorias)#acha o indice do maior valor
            
            nomes_categorias = list(categorias.keys())#acha os nomes
            categoria_top = nomes_categorias[indice_maior_lucro_cat] #salvo o nome da categoria com maior valor
            
            print(f"\nCategoria mais lucrativa: {categoria_top} (R$ {categorias[categoria_top]:.2f})")#printo
            