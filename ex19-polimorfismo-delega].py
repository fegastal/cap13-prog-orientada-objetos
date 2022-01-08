'''Embora seja possível ter herança sem manifestações de polimorfismo, a associação entre ambas as
propriedades é um sinal de BOA programação.'''

class Super:
    def metodo(self):
        print("Estou em Super.method()")

    def delega(self):
        self.accao()


class Fornecedor(Super):
    def accao(self):
        print("Em accao.Fornecedor")


class Herdeiro(Super):
    def accao(self):
        print("Em accao.Herdeiro")


if __name__ == '__main__':
    f = Fornecedor()
    f.delega() # Em accao.Fornecedor
    h = Herdeiro()
    h.delega() # Em accao.Herdeiro
