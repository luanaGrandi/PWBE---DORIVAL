#Exercicio 1
'''class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14
     
    def calcular(self):
      self.calc = self.pi * self.raio**2
      print(f"o valor da area do circulo é: {self.calc}")


dados_circulo = Circulo(5)
dados_circulo.calcular()
'''
##########################################

# Exercicio 2
'''class ContaBancaria:
    def __init__(self, numeroConta, nome, saldo):
        self.numeroConta = numeroConta
        self.nome = nome
        self.saldo = saldo
        print(f"Olá {self.nome}, o numero da conta é {self.numeroConta}. \nSeu saldo é: {self.saldo}")

    def deposito(self):
        deposito = float(input("Digite o quanto deseja depositar: "))
        self.calc = self.saldo + deposito
        print(f"o seu saldo total é: {self.calc}")

    def saques(self):
        saques = float(input("Digite o quanto deseja sacar: "))
        self.calc = self.saldo - saques
        print(f"o seu saldo total é: {self.calc}")

conta = ContaBancaria(12345, "Luana", 200)

usuario = int(input("O que voce deseja fazer: \n1- saquar \n2- depositar \n:"))
if usuario == 1:
    print(conta.saques())
else:
    print(conta.deposito())'''

###################################################

#Exercicio 3
'''class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        self.calc = self.largura * self.altura
        print(f"A area do retangulo é: {self.calc}")

    def perimetro(self):
        self.calc = (self.altura + self.altura ) + (self.largura + self.largura)
        print(f"O perimetro do retangulo é: {self.calc}")

dados_retangulo = Retangulo(10,5)
dados_retangulo.area()
dados_retangulo.perimetro()'''

########################################################

# Exercicio 4
'''class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
        print(f"Nome aluno(a): {self.nome} \nMatriclua: {self.matricula}")
    
    def media(self):
        nota1 = float(input("Digite sua nota: "))
        nota2 = float(input("Digite sua nota: "))
        nota3 = float(input("Digite sua nota: "))
        nota4 = float(input("Digite sua nota: "))

        self.calc = (nota1 + nota2 + nota3 + nota4) /4
        print(f"Sua media é: {self.calc}")
        if self.calc <=5:
            print("Você está reprovado")
        else:
            print("Voce está aprovado!")


informacao = Aluno("Luana", 5834676)
informacao.media()
   '''
##################################################################

# Exercicio 5

'''class Funcionario:
    def __init__(self, nome, salario, cargo, imposto, beneficios):
        self.nome = nome
        self.salrio = salario
        self.cargo = cargo
        self.imposto = imposto
        self.beneficios = beneficios
        print(f"Nome Funcionario: {self.nome} \nSalario: R${self.salrio} \nCargo: {self.cargo} \nValor de Impostos: R${self.imposto} \nValor de baneficios: R${self.beneficios}")
    def Descontos(self):
        self.calc =  self.salrio - (self.imposto + self.beneficios)
        print(f"O seu salario liquido é: R${self.calc}")

dados_funcionario = Funcionario("Luana", 1400, "Desenvolvedor web", 100, 200)
dados_funcionario.Descontos()
'''

#############################################################

# Exercicio 6

'''class Produto:
    def __init__ (self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        print(f"Nome do produt: {self.nome} \nPreço do prduto: R${self.preco} \nQuantidade: R${self.quantidade}")

    def calcular(self):
        self.calc = self.preco * self.quantidade
        print(f"O valor total do estoque é: {self.calc}")

    def verifificar(self):
        if self.quantidade <=0:
            print(f"O produto {self.nome} está indisponivel!")
        else:
            print(f"O produto {self.nome} está disponivel!")

info_produto = Produto("Arroz", 47, 20)
info_produto.calcular()
info_produto.verifificar()
'''
#############################################################

# Exercicio 7

'''class Triangulo:
    def __init__ (self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def valido (self):
        if self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado3 + self.lado2 > self.lado1:
            print("O triangulo é valido!")
        else:
            print("Trinagulo invalido")

    def area(self):
        self.calc = (self.base * self.altura)/ 2
        print(f"A area do triangulo é: {self.calc}")

dados_triangulo = Triangulo(100, 103, 2, 15, 20)
dados_triangulo.valido()
dados_triangulo.area()'''

########################################################

# Exercicio 8

'''class Carro:
    def __init__ (self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
        print(f"Marca do carro: {self.marca} \nModelo: {self.modelo} \nVelocidade: {self.velocidade}")
        
    def acelerar (self):
        self.calc = self.velocidade + 200
        
        print(f"A velocidade atual: {self.calc}")
    def frear (self):
        self.calc = self.velocidade - 300
        print(f"A velocidade atual: {self.calc}")

velocidade = Carro("Honda", "Civic", 120)

usuario = int(input("O que voce deseja: \n1- acelerar \n2- frear \n: "))
if usuario == 1:
    print(velocidade.acelerar())
else:
    print(velocidade.frear())
'''

#########################################################

# Exercicio 9
'''
class Paciente:
    def __init__ (self, nome, idade, historico):
        self.nome = nome
        self.idade = idade
        self.historico = historico
        print(f"Nome do paciente: {self.nome} \nIdade: {self.idade} \nHistorico de consultas: {self.historico}")

    def criarHistorico(self):
        escolha = str(input("Digite qual consulta ira realizar: "))
        escolha2 = int(input("Qual a data que sera realizada a consulta:  "))
        print(f"\nHistorico de consulta: {self.historico} | {escolha}")

informacoes = Paciente("Luana", 16, "Dermatologia") 

usuario = str(input("Você deseja fazer uma nova consulta? s/n:  "))
if usuario == 's':
    print(informacoes.criarHistorico())
else:
    print("Muito obrigado")'''

##########################################################

# Exercicio 10

class Livro:
    def __init__(self,titulo,autor,numPaginas):
        self.titulo = titulo
        self.autor = autor
        self.numPaginas = numPaginas
        self.estoque = 1

    def emprestar(self):
        escolha = str(input("voce deseja emprestar o livro? s/n: "))
        if escolha == 'n':
            print(Livro.devolver())
        elif escolha == 's':
            self.titulo = str(input("Qual o nome do titulo: "))
            self.autor = str(input("Qual o nome do autor: "))
            self.numPaginas =str(input("Digite o total de numero de paginas: "))
            if self.estoque >=1:
                print("\nO livro está disponovel!")
            else:
                print("\nO livro não está disponivel!")

    def devolver(self):
        escolha = str(input("Você deseja devolver o livro?: s/n"))
        if escolha == 's':
            print(f"Verifique se é esse o livro que deseja devolver: \ntitulo: {self.titulo} \nNome Autor: {self.autor} \nNumero de Paginas: {self.numPaginas}")
            verdadeiro =str(input("escolher: sim/nao:"))
            if verdadeiro == 'sim':
                print("Livro devolvido")
           
info = Livro("Depois das cinco", "Bruno", "100")
info.emprestar()
info.devolver()