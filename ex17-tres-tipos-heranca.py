class Super:
    def metodo(self):
        print("Estou em Super.method()")


class Herdeiro(Super):
    pass


class Substituto(Super):
    def metodo(self):
        print("Estou em Substituto.method()")


class Extensor(Super):
    def metodo(self):
        print("Começo do Extensor.method()")
        super().metodo()
        print("Fim do Extensor.method()")


if __name__ == '__main__':
    for classe in (Herdeiro, Substituto, Extensor):
        print('\n' + classe.__name__)
        classe().metodo()
