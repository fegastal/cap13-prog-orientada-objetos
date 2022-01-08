class Conta:
    contador = 0

    def __init__(self):
        Conta.contador += 1


    def mostra_contador():
        print(Conta.contador)


class ListaInstancias:
    instancias = []

    def __init__(self):
        ListaInstancias.instancias.append(self)

    def mostra_instancias():
        print(ListaInstancias.instancias)


if __name__ == '__main__':
    c_1 = Conta()
    c_2 = Conta()
    c_3 = Conta()
    Conta.mostra_contador()

    l_1 = ListaInstancias()
    l_2 = ListaInstancias()
    l_3 = ListaInstancias()
    ListaInstancias.mostra_instancias()
