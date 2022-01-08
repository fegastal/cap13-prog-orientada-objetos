class ContaBancaria:
    numero_conta = 0

    def __init__(self, nome):
        self._nome = nome
        ContaBancaria.numero_conta += 1
        self._numero = ContaBancaria.numero_conta


    def obtem_numero(self):
        return self._numero


if __name__ == '__main__':
    c_1 = ContaBancaria('fernanda')
    print(ContaBancaria.numero_conta)
    c_2 = ContaBancaria('vladimir')
    print(c_2.numero_conta)
    c_3 = ContaBancaria('halina')
    print(c_3.obtem_numero())
    print(c_1.obtem_numero())