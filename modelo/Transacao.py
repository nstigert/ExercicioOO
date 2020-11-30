class Transacao:
    def __init__(self, dataTransacao, produto, qtde):
        self._dataTransacao = dataTransacao
        self._produto = produto
        self._qtde = qtde

    def getDataTransacao(self):
        return self._dataTransacao

    def getNomeProduto(self):
        return self._produto.getNome()

    def getQtde(self):
        return self._qtde
