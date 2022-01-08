'''Embora seja possível ter herança sem manifestações de polimorfismo, a associação entre ambas as
propriedades é um sinal de BOA programação.'''

class Publicacao:
    def __init__(self, codigo, autor, titulo):
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo


    def obtem_codigo(self):
        return self._codigo


    def obtem_entrada_bib(self):
        return '[' + self.obtem_codigo() + ']:' + self._titulo + ',' + self._autor


    def __str__(self):
        return self.obtem_entrada_bib()


class Livro(Publicacao):
    def __init__(self, codigo, autor, titulo, editor, ano):
        super().__init__(codigo, autor, titulo)
        self._editor = editor
        self._ano = ano


    def obtem_entrada_bib(self):
        return super().obtem_entrada_bib() + ' , ' + self._editor + ' , ' + str(self._ano)


class Revista(Publicacao):
    def __init__(self, codigo, autor, titulo, jornal, volume, numero, ano):
        super().__init__(codigo, autor, titulo)
        self._jornal = jornal
        self._volume = volume
        self._numero = numero
        self._ano = ano


    def obtem_entrada_bib(self):
        return super().obtem_entrada_bib() + ' , ' + self._jornal + ', ' + str(self._volume) + ', ' + str(self._numero) + ', ' + str(self._ano)


if __name__ == '__main__':
    pub = Publicacao('costa123', 'Ernesto Costa', 'Livros Estranhos')
    livro = Livro('antunes234', 'Carlos Antunes', 'Logo Sonho', 'Passado e Futuro', 2014)
    revista = Revista('borges345', 'Daniela Borges', 'Aves de Rapina', 'Biodiversidade', 5, 2, 2014)
    print(pub)
    print(livro)
    print(revista)
