'''
Exercícios Teóricos | Capítulo 13

Extra: O que é o método __init__?

É por definição o inicializador de uma instância da sua classe.

class Cachorros:
    def __init__(self, patas, cor):
        self.patas = patas
        self.cor = cor

fido = Cachorros(4, "preto")
bidu = Cachorros(3, "marrom")

Fido e bidu são instâncias (objetos) da sua classe Cachorros, e ao definí-los caracterizando suas
patas e suas cores, o Python, por meio do init "inicializou" instâncias da classe. O self se refere
à instância, ou seja, o self de fido é o próprio fido.

Ou seja, você tem a classe Cachorros e fido e bidu são instâncias da sua classe que foram inicializadas pelo
__init__ quando você criou as instâncias.

Se você quiser saber os atributos de cada objeto, pode fazer:

fido.cor
retorna 'preto'

Por definição você deve usar o __init__ para criar objetos (instâncias) das suas classes.
E por isso geralmente a primeira função que você cria ao criar uma classe é o __init__.


1) Diga o que entende por encapsulamento. Qual a sua importância?

Quando definimos uma função, por exemplo, para o cálculo do fatorial de um número, criamos também uma abstração:
podemos usar essa função sem saber o modo como o cálculo é efetivamente feito.

O que temos que saber é que TIPOS de argumentos a função espera que lhe sejam passados (no exemplo de fatorial,
um inteiro não negativo), para fornecer o resultado desejado.Visto dessa maneira, a função pode ser reutilizada
em diferentes situações.

Quando definimos um tipo de dados através de uma classe, identificamos os atributos e os métodos dos objetos da classe.
Numa lógica de REUTILIZAÇÃO de uma classe em diferentes situações importa também definir aquilo que o utilizador
da classe sabe sobre a mesma, aquilo que ele "vê".

É claro que aquilo que a classe se disponibiliza, a sua INTERFACE, deve manter-se imutável do ponto de vista
do utilizador, independentemente de, ao longo do tempo, existirem modificações na sua implementação.

A esta distinção entre a INTERFACE (PÚBLICA) e a IMPLEMENTAÇÃO (PRIVADA), chamamos ENCAPSULAMENTO (sinônimo de
esconder informação = hiding). Esta separação é o SUPORTE a boas práticas de programação.

A INTERFACE é formada pelos métodos push, pop, top, is_empty e len, por exemplo.


2) Qual a diferença entre atributos de instâncias e atributos de classe? Para que serve essa distinção?

a) atributos de instâncias:

O que podemos fazer com objetos de instância? As únicas operações compreendidas por
objetos de instância são os atributos de referência. Existem duas maneiras válidas para nomear
atributos: atributos de dados e métodos.

Dados: correspondem a “variáveis de instância” em Smalltalk, e a “membros de dados” em C++.
Atributos de dados não precisam ser declarados. Assim como variáveis locais, eles passam a existir na primeira
vez em que é feita uma atribuição. Por exemplo, se x é uma instância da MyClass criada acima, o próximo
trecho de código irá exibir o valor 16, sem deixar nenhum rastro:

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

Métodos: Um método é uma função que “pertence” a um objeto instância. (Em Python, o termo método
não é aplicado exclusivamente a instâncias de classes definidas pelo usuário: outros tipos de objetos
também podem ter métodos. Por exemplo, listas possuem os métodos append, insert, remove, sort, entre outros.


3) O que são e para que servem os métodos estáticos?

Quando queremos um método que seja chamado via classe e via instância sem a necessidade de passar a
referência deste objeto. O Python resolve isso usando métodos estáticos.

Métodos estáticos não precisam de uma referência, não recebem um primeiro argumento especial (self).
É como uma função simples que, por acaso, reside no corpo de uma classe em vez de ser definida no nível do módulo.

Para que um método seja considerado estático, basta adicionarmos um decorador,
assim como fizemos com as propriedades no capítulo anterior. O decorador se chama @staticmethod:

@staticmethod
def get_total_contas():
    return Conta._total_contas

 c1 = Conta(100.0)
    c1.get_total_contas()
    #1
    c2 = Conta(200.0)
    c2.get_total_contas()
    #2
    Conta.get_total_contas()
    #2


4) O que são e para que servem os métodos de classe?

Métodos estáticos não devem ser confundidos com métodos de classe. Como os métodos estáticos, métodos de
classe não são ligados às instâncias, mas sim a classe. O primeiro parâmetro de um método de classe
é uma referência para a classe, isto é, um objeto do tipo class, que por convenção nomeamos como 'cls'.
Eles podem ser chamados via instância ou pela classe e utilizam um outro decorador, o @classmethod:

class Conta:

    _total_contas = 0

    def __init__(self):
        type(self)._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

c1 = Conta(100.0)
    c1.get_total_contas()
    #1
    c2 = Conta(200.0)
    c2.get_total_contas()
    #2
    Conta.get_total_contas()
    #2

OBS!!!: No início pode parecer confuso qual usar: @staticmethod ou @classmethod? Isso não é trivial.
Métodos de classe servem para definir um método que opera na classe, e não em instâncias.
Já os métodos estáticos utilizamos quando não precisamos receber a referência de um objeto especial
(seja da classe ou de uma instância) e funciona como uma função comum, sem relação.


5) O que são os decoradores de funções?

Um decorador em Python é um objeto que estende/modifica a funcionalidade de uma função (ou método) em tempo
de execução e conceitualmente está mais próximo da anotação do Java que do decorador da orientação a objetos.

Na prática, o decorador age como uma embalagem de presente, acondicionando a função sem alterar seu conteúdo
(ele continua sendo um presente) mas deixando-o mais bonito.

É bom lembrar que em Python as funções também são objetos…
Funções são argumentos: Elas podem ser passadas para outras funções como se fossem argumentos…

    minha_funcao = decora_funcao(minha_funcao)

Acontece que a linha onde a minha_funcao() é recebe a decoração por decora_funcao()…
…pode ser simplificada através da sintaxe do Python como…

...
    @decora_funcao
    def minha_funcao():
        print("### minha_funcao() ###")
    ...


6) O que entende por herança?

Por herança, você pode

prevalecer sobre as características de um pai ou superclasse.
alterar os recursos que você considera importantes.
adicione novas propriedades ao seu filho ou subclasse ou classe derivada.

Herança é o mecanismo pelo qual estendemos a funcionalidade de uma classe.
Por exemplo, suponha que a gente precise representar veículos de diferentes marcas e modelos em um programa.
Uma abordagem é criar uma classe para representar cada veículo diferente. Porém, existem informações que
são comuns a todos os veículos, como o tipo do veículo (motocicleta, carro, caminhão, etc.), chassi, marca,
modelo, ano, e etc. Uma abordagem mais elegante é usar herança de modo a criar uma classe que armazena
informações comuns a todos os tipos de veículos que precisamos representar e subsequentemente estender
essa classe para representar veículos específicos. O exemplo abaixo mostra a classe Veiculo.

class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

Agora que sabemos como representar um veículo genérico, desejamos estender essa classe de modo a
representar motocicletas. Suponha que, além das informações comuns a todos os veículos, motocicletas
também contenham dados sobre a cilindrada da motocicleta em questão. Para representar uma motocicleta,
podemos criar uma classe que herda o estado e comportamento da classe Veiculo e a estende de modo a adicionar
informação sobre a cilidrada. O exemplo abaixo ilustra como fazer isso em Python.

class Motocicleta(Veiculo): #	Indica que a classe Motocicleta herda da classe Veiculo.
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano) #Invoca o método init da super classe (ou classe base, Veiculo).
        self.cilindrada = cilindrada

No exemplo acima, dizemos que a classe Veiculo é uma classe base ou super classe e que Motocicleta é uma
classe derivada ou uma classe filha da classe Veiculo. Dizemos também que a classe Motocicleta herda da
classe Veiculo (daí o nome herança) ou que a classe Motocicleta estende a classe Veiculo.

Objetos da classe Motocicleta têm uma propriedade importante: eles possuem todas as funcionalidades de objetos
da classe Veiculo mais algumas funcionalidades extra (no nosso exemplo, informação sobre a cilindrada da
motocicleta). Em outras palavras, uma motocicleta é um veículo. Este é um conceito importantíssimo em OOP
porque sempre que uma função esperar receber como parâmetro um objeto do tipo Veiculo, podemos passar um objeto
do tipo Motocicleta, dado que uma motocicleta é um veículo.

Este conceito é tão importante em programação orientada a objetos que recebeu um nome específico:
"Princípio da Substituição de Liskov", em homenagem a Barbara Liskov, pioneira em Ciência da Computação e
ganhadora do Prêmio Turing (o "Prêmio Nobel da Computação").

Python nos permite verificar se um objeto é uma instância de uma determinada classe por meio da função isinstance(),
cujo comportamento é ilustrado no exemplo abaixo.

v = Veiculo('carro', '9BGRD08X04G117974', 'Ferrari', 'F112', '2017')
m = Motocicleta('motocicleta', '5AZKG01Z12A339037', 'Honda', 'CG', '2015')
print(isinstance(v, Veiculo), isinstance(v, Motocicleta))
print(isinstance(m, Veiculo), isinstance(m, Motocicleta))

#True False
#True True


7) Que problemas podem surgir num processo de herança?

O uso de herança aumenta o ACOPLAMENTO entre as classes, isto é, o quanto uma classe DEPENDE de outra.
A relação entre classe mãe e filha é muito forte e isso acaba fazendo com que o programador das classes
filhas tenha que conhecer a implementação da classe mãe e vice-versa - fica difícil fazer uma
mudança pontual no sistema.

Por exemplo, imagine se tivermos que mudar algo na nossa classe Funcionario, mas não quiséssemos que
todos os funcionários sofressem a mesma mudança. Precisaríamos passar por cada uma das filhas de Funcionario
verificando se ela se comporta como deveria ou se devemos sobrescrever o tal método modificado.

Esse é um problema da herança, e não do polimorfismo, que resolveremos mais tarde.


8) De que modo se podem relacionar as superclasses e as suas subclasses?

As Super classes às vezes também são chamadas de ancestrais.
A herança permite que você crie classes baseadas em classes existentes, e a subclasse construída por meio desse
método permite que você herde os recursos e métodos da superclasse. Isso significa que esse método oferece suporte
à reutilização de código. Geralmente, os procedimentos ou software herdados por uma subclasse são considerados
reutilizáveis na subclasse. Os relacionamentos de objetos ou classes por meio de herança dão origem a um
grafo direcionado.

Se tivermos várias classes semelhantes, podemos definir as funcionalidades comuns em uma classe e definir
as classes filho dessa classe pai e implementar funcionalidades específicas lá. Usando aqui super(),
uma função integrada do Python é um procedimento ligeiramente melhor para chamar a classe pai para inicialização.
O código a seguir é o melhor exemplo de relacionamento entre superclasse e subclasse.

class Animal(object):
  def __init__(self, animalName):
    print(animalName, 'color is white.')

class Cat(Animal):
  def __init__(self):
    print('Cat Name is Milo.')
    super().__init__('Milo')

catobject = Cat()

#Cat Name is Milo.
#Milo color is white.


9) O que é a classe object?

Uma classe Python é como um esboço para a criação de um novo objeto. Um objeto é qualquer coisa que você deseja
manipular ou alterar enquanto trabalha com o código. Cada vez que um objeto de classe é instanciado, que é
quando declaramos uma variável, um novo objeto é iniciado do zero. Os objetos de classe podem ser usados
repetidamente sempre que necessário.


10) O que entende por polimorfismo? Quais as vantagens e quando se deve usar?

É a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua superclasse, e o programa
saber qual método deve ser invocado, especificamente (da super ou sub).

Ou seja, o objeto tem a capacidade de assumir diferentes formas (polimorfismo).

Vamos criar a classe Superclasse que tem apenas um método, o hello(). Instanciamos um objeto e chamamos esse método:

class Super:
 def hello(self):
  print("Olá, sou a superclasse!")

teste = Super()
teste.hello()

#Olá, sou a superclasse!

Agora vamos criar outra classe, a Sub,  que vai herdar a Superclasse e vamos definir nela um método
de mesmo nome hello(), mas com um texto diferente:

class Super:
 def hello(self):
  print("Olá, sou a superclasse!")

class Sub (Super):
 def hello(self):
  print("Olá, sou a subclasse!")

teste = Sub()
teste.hello()

#Olá, sou a subclasse!

Veja bem, Sub herda a Superclasse, ou seja, tudo que nem na superclasse (atributos e métodos), vai ter na subclasse.
Porém, quando chamamos o método hello(), ele vai invocar o método da subclasse e não da superclasse!
O Python entende: "Opa, ele instanciou um objeto da subclasse. Por isso vou invocar o método da subclasse
e não da superclasse".

Ou seja, seu objeto assumiu a forma da subclasse, embora ele também seja uma superclasse.
Dizemos que o método da subclasse fez uma sobreposição, ele sobrepôs, passou por cima, do método da superclasse.

Vamos mais além agora, e criar a Subsubclasse, que vai herdar a Sub.
Hora, se a Subsubclasse herda a Sub, e a Sub herda a Super, então a Subsubclasse também herda tudo da Super.

Porém, quando instanciamos um objeto da Subsub e invocamos o método hello(), ele vai rodar o método da Subsub:

class Super:
 def hello(self):
  print("Olá, sou a superclasse!")

class Sub (Super):
 def hello(self):
  print("Olá, sou a subclasse!")

class Subsub (Sub):
 def hello(self):
  print("Olá, sou a subsubclasse!")

teste = Subsub()
teste.hello()

Embora estejamos chamando sempre o mesmo método (hello),
que está presente em todas as classes e nas herdadas, ele age de maneira diferente!


11) O que são diagramas de classe?

Diagramas de pilha: mostram o estado de um programa
Diagramas de objeto: mostram os atributos de um objeto e seus valores.
Ambos diagramas representam um retrato da execução de um programa, então eles mudam no decorrer da execução do programa.
Eles também são altamente detalhados; para alguns objetivos, detalhados demais.

Diagrama de classe é uma representação mais ABSTRATA da estrutura de um programa.
Em vez de mostrar objetos individuais, ele mostra classes e as relações entre elas.

_ Os objetos de uma classe podem conter referências a objetos em outra classe. Por exemplo, cada Rectangle
contém uma referência a um Point, e cada Deck contém referências a muitos Cards. Esse tipo de relação chama-se
composição. É uma relação do tipo HAS-A (tem um), com a ideia de “um Rectangle tem um Point”.

_ Uma classe pode herdar de outra. Esta relação chama-se IS-A (é um), com a ideia de “um Hand é um tipo de Deck”.

_ Uma classe pode depender de outra no sentido de que os objetos em uma classe possam receber objetos na
segunda classe como parâmetros ou usar esses objetos como parte de um cálculo. Este tipo de relação chama-se dependência.

Um diagrama de classe é uma representação gráfica dessas relações.


12) Que tipos de relações podem existir entre as classes?

a) Relação IS-A: entre uma classe-filho e sua classe-pai. Também chamada de herança.
b) Relação HAS-A: entre duas classes onde as instâncias de uma classe contêm referências a instâncias da outra.
Também chamada de composição.


13) O que entende por classes abstratas e para que servem?

Uma classe que contém um ou mais Métodos Abstratos é chamada de Classe Abstrata. Um método abstrato é um método
que possui uma declaração, mas não possui uma implementação. Enquanto estamos projetando grandes unidades funcionais,
usamos uma classe abstrata. Quando queremos fornecer uma interface comum para diferentes implementações de um
componente, usamos uma classe abstrata.

Pode ser considerada um projeto para outras classes. Ele permite que você crie um conjunto de métodos
que devem ser criados em qualquer classe filha construída a partir da classe abstrata.

Ao definir uma classe base abstrata, você pode definir uma Interface de Programa de Aplicativo (API)
comum para um conjunto de subclasses. Esse recurso é especialmente útil em situações em que um terceiro
fornecerá implementações, como plug-ins, mas também pode ajudá-lo ao trabalhar em uma grande equipe ou com uma
grande base de código onde é difícil manter todas as classes em sua mente ou não é possível.

Por padrão, o Python não fornece classes abstratas. Python vem com um módulo que fornece a base para
a definição de classes Abstract Base (ABC) e o nome do módulo é ABC.
abc funciona decorando métodos da classe base como abstratos e então registrando classes concretas
como implementações da base abstrata. Um método se torna abstrato quando decorado com a palavra-chave
@abstractmethod. Por exemplo:

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 3 lados")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 5 lados")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 6 lados")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 4 lados")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

Resultado:
Eu tenho 3 lados
Eu tenho 4 lados
Eu tenho 5 lados
Eu tenho 6 lados

Ou então...

from abc import ABC, abstractmethod

class Animal(ABC):
def move(self): pass
class Human(Animal):
def move(self): print("Eu posso andar e correr")
class Snake(Animal):
def move(self): print("Eu posso rastejar")
class Dog(Animal):
def move(self): print("Eu posso latir")
class Lion(Animal):
def move(self): print("Eu posso rugir")
Driver code
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()

Resultado:
Eu posso andar e correr
Eu posso rastejar
Eu posso latir
Eu posso rugir
'''