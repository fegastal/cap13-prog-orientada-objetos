class Mundo:
    def __init__(self, tamanho):
        self._tamanho = tamanho
        self._grelha = [['*'] * tamanho for i in range(tamanho)]

    def mostra_mundo(self):
        print('-' * self._tamanho * 7)
        print()
        for i in range(self._tamanho):
            linha = self._grelha[i]
            for j in range(self._tamanho):
                print('%-6s' % linha[j] + ' ', end='')
            print()
            print()
        print('-' * self._tamanho * 7)
        print()

    def regista(self, robo):
        x, y = robo.obtem_posicao()
        self._grelha[y][x] = robo

    def limpa_registro(self, x, y):
        self._grelha[y][x] = '*'

    def obtem_tamanho(self):
        return self._tamanho

    def calcula_vazia(self, x, y):
        return self._grelha[y][x] == '*'


class Robot:
    def __init__(self, nome, mundo, pos_x=0, pos_y=0):
        self._nome = nome
        self._mundo = mundo
        self._pos_x = pos_x
        self._pos_y = pos_y

    def obtem_mundo(self):
        return self._mundo

    def obtem_posicao(self):
        return self._pos_x, self._pos_y

    def define_posicao(self, x, y):
        self._pos_x = x
        self._pos_y = y

    def move(self):
        from random import choice
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        x, y = self.obtem_posicao()
        d_x, d_y = choice(delta)
        n_x = x + d_x
        n_y = y + d_y
        tamanho = self._mundo.obtem_tamanho()
        if (0 <= n_x < tamanho) and (0 <= n_y < tamanho):
            if self._mundo.celula_vazia(n_x, n_y):
                self._mundo.limpa_registo(x, y)
                self.define_posicao(n_x, n_y)
                self._mundo.regista(self)
            else:
                print('Célula Ocupada.')
        else:
            print('Movimento Impossível.')

    def __str__(self):
        return self._nome

    @staticmethod
    def simula(n, tamanho):
        m = Mundo(tamanho)
        r = Robot('R', m, tamanho // 2, tamanho // 2)
        m.regista(r)

        for i in range(n):
            m.mostra_mundo()
            r.move()
