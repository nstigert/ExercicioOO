from modelo.Transacao import Transacao


class Venda(Transacao):
    def __init__(self, dataVenda, cliente, produto, qtdeVendida):
        Transacao.__init__(self, dataVenda, produto, qtdeVendida)
        self._cliente = cliente

    def vender(self, produto, qtdeVendida):
        if (produto.verificarEstoqueInsuficiente(qtdeVendida)):
            print("Falha! A quantidade de venda não pode ser maior que a quantidade no estoque")
            return False
        else:
            produto.debitarEstoque(qtdeVendida)
            print("Valor da venda:", produto.calcularValorVenda(qtdeVendida))
            if(produto.verificarEstoqueBaixo()):
                print("Alerta: Estoque abaixo do mínimo.")
            return True
