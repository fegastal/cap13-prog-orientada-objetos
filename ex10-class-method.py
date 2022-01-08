class Conta:
    contador = 0


    def __init__(self):
        Conta2.contador += 1

    @classmethod
    def mostra_contador(cls):
        print(cls.contador)


if __name__ == '__main__':
    c_1 = Conta2()
    c_2 = Conta2()
    c_3 = Conta2()
    Conta2.mostra_contador()
    c_3.mostra_contador()