from modelo.Transacao import Transacao


class Compra(Transacao):
    def __init__(self, dataCompra, produto, fornecedor, qtdeCompra, precoUnit):
        Transacao.__init__(self, dataCompra, produto, qtdeCompra)
        self._fornecedor = fornecedor
        self._precoUnit = precoUnit

    def comprar(self, produto, qtdeCompra):
        if (produto.verificarEstoqueExcedente(qtdeCompra)):
            print("Falha! A quantidade de compra não pode exceder o estoque")
            return False
        else:
            produto.creditarEstoque(qtdeCompra)
            return True
