class Conta:
    contador = 0


    def __init__(self):
        Conta.contador += 1

@staticmethod
def mostra_contador():
    print(Conta.contador)


if __name__ == '__main__':
    c_1 = Conta()
    c_2 = Conta()
    c_3 = Conta()
    Conta.mostra_contador()
    c_3.mostra_contador()