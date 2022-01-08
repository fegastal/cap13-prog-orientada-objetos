class PessoaEscola:


    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome


    def obtem_nome(self):
        return self._nome


class Aluno(PessoaEscola):
    pass


class Funcionario(PessoaEscola):


    def __init__(self, salario):
        self._salario = salario

    def obtem_salario(self):
        return self._salario


class Docente(Funcionario):
    pass


class NaoDocente(Funcionario):
    pass


if __name__ == '__main__':
    pesc_1 = Docente(123456, 'Fernanda Gastal', 1500)
    print(pesc_1.obtem_nome()) #Fernanda Gastal
    print(pesc_1.obtem_salario()) #Fernanda Gastal

