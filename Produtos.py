class Produto:
    """
    Classe que representa um produto de um estabelecimento que comercializa frutas, verduras e legumes.
    """

    def __init__(self, codigo: int, descricao: str, categoria: str, preco_compra: float, preco_venda: float, quantidade: float):
        """
        Construtor da classe Produto que inicializa um novo objeto produto.
        :param codigo: código único privado indentificador do produto (int)
        :param descricao: descrição única indentificadora do produto (str)
        :param categoria: categoria [fruta, verdura, legume] do produto (str)
        :param preco_compra: preço em R$ pago pela compra do kg do produto (float)
        :param preco_venda: preço definido para o kg de venda do produto (float)
        :param quantidade: quantidade em kg do produto (float)
        """
        self.__codigo = codigo
        self.descricao = descricao.upper().replace(" ", "")
        self.categoria = categoria.lower().replace(" ", "")
        self.preco_compra = format(preco_compra, ".2f")
        self.preco_venda = format(preco_venda, ".2f")
        self.quantidade = format(quantidade, ".3f")

    @property
    def codigo(self) -> int:
        """
        Método getter para possibilitar o acesso ao código (atributo privado)
        :return: códido do produto (int)
        """
        return self.__codigo

    def __str__(self) -> str:
        """
        Método __str__ sobrescrito
        :return: uma string editada com as informações do produto (str)
        """
        return (f"Código: {self.__codigo}\n"
                f"Descrição: {self.descricao}\n"
                f"Categoria: {self.categoria}\n"
                f"Preço de compra: R${self.preco_compra}\n"
                f"Preço de venda: R${self.preco_venda}\n"
                f"Quantidade: {self.quantidade} kg\n")

    def descricao(self, nova_descricao: str):
        """
        Método que habilita a edição da descrição do produto
        :param nova_descricao: nova descrição para o produto (str)
        """
        self.descricao = nova_descricao.upper().replace(" ", "")

    def categoria(self, nova_categoria: str):
        """
        Método que habilita a edição da cetegoria [fruta, verdura, legume] do produto
        :param nova_categoria: nova cetegoria [fruta, verdura, legume] para o produto (str)
        """
        if nova_categoria in ["fruta", "verdura", "legume"]:
            self.categoria = nova_categoria.lower().replace(" ", "")
        else:
            print("Categoria inválida!\n")

    def preco_compra(self, novo_preco_compra):
        """
        Método que habilita a edição do preço R$ pago na compra do produto
        :param novo_preco_compra: novo preço R$ pago na compra do produto (float)
        """
        self.preco_compra = format(novo_preco_compra, ".2f")

    def preco_venda(self, novo_preco_venda):
        """
        Método que habilita a edição do preço R$ de venda do produto
        :param novo_preco_venda: novo preço R$ de venda do produto (float)
        """
        self.preco_venda = format(novo_preco_venda, ".2f")

    def quantidade(self, nova_quantidade):
        """
        Método que habilita a edição da quantidade kg do produto
        :param nova_quantidade: nova quantidade kg do produto (float)
        """
        self.quantidade = format(nova_quantidade, ".3f")