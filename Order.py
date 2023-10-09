import Cliente

class oder:
    def __init__(self, preco_total, status, cliente: Cliente):
        self.preco_total = preco_total
        self.status = status
        self.cliente = cliente

    def setPreco_total(self, preco_total):
        self.preco_total = preco_total
    
    def setStatus(self, status):
        self.status = status

    def setCliente(sef, cliente):
        self.cliente = cliente

    def getPreco_total(self):
        return self.preco_total
    
    def getStatus(self):
        return self.status
    
    def getCliente(self):
        return cliente

    
    

        