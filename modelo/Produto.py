from modelo.Compra import Compra
from modelo.Venda import Venda


class Produto:
    def __init__(self, nome, qtdeEstoque, precoUnit, estoqueMinimo, estoqueMaximo):
        self._nome = nome
        self._qtdeEstoque = qtdeEstoque
        self._precoUnit = precoUnit
        self._estoqueMinimo = estoqueMinimo
        self._estoqueMaximo = estoqueMaximo
        self._historico = []

    def registrarHistorico(self, transacao):
        historico = "Data da transação: {}. Produto: {}. Quantidade: {}".format(transacao.getDataTransacao(), transacao.getNomeProduto(), transacao.getQtde())
        self._historico.append(historico)

    def exibirHistorico(self):
        for historico in self._historico:
            print(historico)

    def debitarEstoque(self, quantidade):
        self._qtdeEstoque = self._qtdeEstoque - quantidade

    def creditarEstoque(self, quantidade):
        self._qtdeEstoque = self._qtdeEstoque + quantidade


    def verificarEstoqueBaixo(self):
        if (self._qtdeEstoque < self._estoqueMinimo):
            return True
        else:
            return False

    def verificarEstoqueInsuficiente(self, quantidade):
        if (quantidade > self._qtdeEstoque):
            return True
        else:
            return False

    def verificarEstoqueExcedente(self, quantidade):
        soma = quantidade + self._qtdeEstoque
        if (soma > self._estoqueMaximo):
            return True
        else:
            return False

    def calcularValorVenda(self, quantidade):
        return self._precoUnit * quantidade

    def vender(self, dataVenda, cliente, qtdeVendida):
        venda = Venda(dataVenda, cliente, self, qtdeVendida)
        if (venda.vender(self, qtdeVendida)):
            self.registrarHistorico(venda)

    def comprar(self, dataCompra, fornecedor, qtdeCompra, precoUnit):
        compra = Compra(dataCompra, self, fornecedor, qtdeCompra, precoUnit)
        if (compra.comprar(self, qtdeCompra)):
            self.registrarHistorico(compra)

    def getNome(self):
        return self._nome