import Order, Produto

class OrderItem:
    def __init__(self, quantidade, preco_unitario, order: Order, produto: Produto):
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.order = order
        self.produto = produto

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def setPreco_unitario(self, preco_unitario):
        self.preco_unitario = preco_unitario

    def setOrder(self, order):
        self.order = order
    
    def setProduto(self, produto):
        self.produto = produto

    def getQuantidade(self):
        return self.quantidade

    def getPreco_unitario(self):
        return self.preco_unitario

    def getOrder(self):
        return self.order

    def getProduto(self):
        return self.produto    