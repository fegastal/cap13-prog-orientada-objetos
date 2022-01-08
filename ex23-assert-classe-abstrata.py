class Super:
    def acao(self):
        assert False, 'Método acao deve estar definido...'

class Super1:
    def acao(self):
        raise NotImplementedError('Método acao deve estar definido...')

class Fornecedor(Super):
    def acao(self):
        print('Em acao.Fornecedor')

class Herdeiro(Super):
    pass