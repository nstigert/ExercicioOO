from modelo.Pessoa import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome, cnpj):
        Pessoa.__init__(self, nome)
        self._cnpj = cnpj