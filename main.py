from modelo.Cliente import Cliente
from modelo.Produto import Produto
from modelo.Fornecedor import Fornecedor

cliente1 = Cliente("Marco", "123")
produto1 = Produto("Caneta", 100, 1.2, 10, 200)
produto1.vender("19/11/2020", cliente1, 95)
produto1.vender("20/11/2020", cliente1, 10)
fornecedor1 = Fornecedor("Antonio", "456")
produto1.comprar("21/11/2020", fornecedor1, 50, 1.1)
produto1.comprar("22/11/2020", fornecedor1, 150, 1.1)
produto1.exibirHistorico()