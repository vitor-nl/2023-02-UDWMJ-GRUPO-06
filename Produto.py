from nis import cat
import Categoria

class Produto:
    def __init__(self, nome, descricao, data_fabricacao, esta_ativo, categoria: Categoria):
        self.nome = nome
        self.descricao = descricao
        self.data_fabricacao = data_fabricacao
        self.esta_ativo = esta_ativo
        self.categoria = categoria