class C1:
    def canta(self):
        return False


class C2:
    def canta(self):
        return False

    def voa(self):
        return True


class C3(C1, C2):
    pass


class C4(C2, C1):
    pass


if __name__ == '__main__':
    i_3 = C3()
    print(i_3.canta())
    print(i_3.voa())

    i_4 = C4()
    print(i_4.canta())
    print(i_4.voa())