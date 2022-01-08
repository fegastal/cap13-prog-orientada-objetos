class Estudante:


    def __init__(self, nome):
        self.nome = nome.split()


    def obtem_nome(self):
        return " ".join(self.nome)


if __name__ == '__main__':
    est = Estudante('Fernanda Gastal')
    print(est.nome)
