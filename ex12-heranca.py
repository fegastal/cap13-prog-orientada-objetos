class PessoaEscola:


    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome

    def obtem_nome(self):
        return self._nome


class Aluno(PessoaEscola):
    pass


class Funcionario(PessoaEscola):
    pass


class Docente(Funcionario):
    pass


class NaoDocente(Funcionario):
    pass


if __name__ == '__main__':
    pesc_1 = Docente(123456, 'Fernanda Gastal')
    print(pesc_1.obtem_nome()) #Fernanda Gastal
    print(pesc_1._nome) #Fernanda Gastal
    print(type(pesc_1)) #<class '__main__.Docente'>

