class Estudante:


    def __init__(self, nome):
        self._nome = nome
        

    def obtem_nome(self):
        return self._nome

    def muda_nome(self, nome):
        self._nome = nome


if __name__ == '__main__':
    est = Estudante('Fernanda Gastal')
    print(est.nome)
