class Mundo:
    def __init__(self, tamanho):
        self._tamanho = tamanho
        self._grelha = [['*'] * tamanho for i in range(tamanho)]

    def mostra_mundo(self):
        for i in range(self._tamanho):
            linha = self._grelha[i]
            for j in range(self._tamanho):
                print('%-6s' % linha[j] + ' ', end='')
            print()
            print()

    def regista(self, robo):
        x, y = robo.obtem_posicao()
        self._grelha[y][x] = robo


class Robot:
    def __init__(self, nome, mundo, pos_x=0, pos_y=0):
        self._nome = nome
        self._mundo = mundo
        self._pos_x = pos_x
        self._pos_y = pos_y

    def obtem_nome(self):
        return self._nome

    def obtem_posicao(self):
        return self._pos_x, self._pos_y

    def obtem_mundo(self):
        return self._mundo

    def __str__(self):
        return self._nome


if __name__ == '__main__':
    m = Mundo(5)
    m.mostra_mundo()
    r1 = Robot('R1', m)
    m.regista(r1)
    r2 = Robot('R2', m, 3, 4)
    print('Nome: ' + r2.obtem_nome() + '\n' + 'Posicao: ' + str(r2.obtem_posicao()))
    m.regista(r2)
    m.mostra_mundo()