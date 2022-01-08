class Rational:


    def __init__(self, n, d):
        self.numerador, self.denominador = Rational.reduce(n, d)

    @staticmethod
    def mdc(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.mdc(n1, n2)
        return(n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerador)+'/'+str(self.denominador)

if __name__ == '__main__':
    frac = Rational(9, 36)
    print(frac)


if __name__ == '__main__':
    c_1 = Conta2()
    c_2 = Conta2()
    c_3 = Conta2()
    Conta2.mostra_contador()
    c_3.mostra_contador()