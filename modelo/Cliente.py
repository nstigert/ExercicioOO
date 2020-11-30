from modelo.Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self._cpf = cpf