class Produto:
    """
    Doc string
    """

    def __init__(self, codigo: int, descricao: str, categoria: str, preco_compra: float, preco_venda: float, quantidade: float):
        """
        Doc string
        """
        self.__codigo = codigo
        self.descricao = descricao.upper().replace(" ", "")
        self.categoria = categoria.lower().replace(" ", "")
        self.preco_compra = format(preco_compra, ".2f")
        self.preco_venda = format(preco_venda, ".2f")
        self.quantidade = format(quantidade, ".3f")

    @property
    def codigo(self):
        """
        Doc string
        """
        return self.__codigo

    def __str__(self):
        """
        Doc string
        """
        return (f"Código: {self.__codigo}\n"
                f"Descrição: {self.descricao}\n"
                f"Categoria: {self.categoria}\n"
                f"Preço de compra: R${self.preco_compra}\n"
                f"Preço de venda: R${self.preco_venda}\n"
                f"Quantidade: {self.quantidade} kg\n")

    def descricao(self, nova_descricao: str):
        self.descricao = nova_descricao.upper().replace(" ", "")

    def categoria(self, nova_categoria: str):
        if nova_categoria in ["fruta", "verdura", "legume"]:
            self.categoria = nova_categoria.lower().replace(" ", "")
        else:
            print("Categoria inválida!\n")

    def preco_compra(self, novo_preco_compra):
        self.preco_compra = format(novo_preco_compra, ".2f")

    def preco_venda(self, novo_preco_venda):
        self.preco_venda = format(novo_preco_venda, ".2f")

    def quantidade(self, nova_quantidade):
        self.quantidade = format(nova_quantidade, ".3f")