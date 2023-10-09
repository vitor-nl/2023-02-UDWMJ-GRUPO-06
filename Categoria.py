class Categoria():
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def setId(self, id):
        self.id = id
    
    def setNome(self, nome):
        self.nome = nome

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getID(self):
        return self.id
   
    def getNome(self):
        return self.nome
    
    def getDescricao(self):
        return self.descricao