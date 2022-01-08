from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def acao(self):
        pass
    

class Herdeiro(Super):
    pass


class Substitui(Super):
    def acao(self):
        print('Em ação. Substitui.')