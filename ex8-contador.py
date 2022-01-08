def mostra_contador():
    print(Conta.contador)


class Conta:
    contador = 0


    def __init__(self):
        Conta.contador += 1


if __name__ == '__main__':
    c_1 = Conta()
    c_2 = Conta()
    c_3 = Conta()
    print(Conta.contador)
    mostra_contador()