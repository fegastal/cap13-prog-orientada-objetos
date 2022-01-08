class Estudante:


    def __init__(self, nome):
        self.nome = nome


    def obtem_nome(self):
        return self.nome


if __name__ == '__main__':
    est = Estudante('Fernanda Gastal')
    print(est.obtem_nome.lower())
