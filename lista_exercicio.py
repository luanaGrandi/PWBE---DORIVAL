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

'''class Livro:
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
        escolha = str(input("\nVocê deseja devolver o livro?: s/n: "))
        if escolha == 's':
            print(f"Verifique se é esse o livro que deseja devolver: \ntitulo: {self.titulo} \nNome Autor: {self.autor} \nNumero de Paginas: {self.numPaginas}")
            verdadeiro =str(input("\nescolher: sim/nao: "))
            if verdadeiro == 'sim':
                print("Livro devolvido")
            else:
                print("\nMuito obrigado(a)")
           
info = Livro("Depois das cinco", "Bruno", "100")
info.emprestar()
info.devolver()'''

##########################################################################################################################

# EXERCICIO 11

'''class Banco:
    def __init__(self, saldo ):
       self.saldo = saldo
       self.clientes = []
      

    def Entrar(self):
        print("SEJA BEM VINDO AO BANCO:")
        verificar = str(input("\nVocê possui uma conta?: s/n "))
        if verificar == 's':
            print("Abrir conta:")
            nome = str(input("\nDigite seu nome: "))
            agencia = int(input("Digite sua agencia: "))
            senha = int(input("Digite sua senha: "))
        else:
            print("\nAbrir sua conta no banco: ")
            nome = str(input("Digite seu nome: "))
            cpf = int(input("Digite seu CPF: "))
            nascimento = str(input("Digite sua data de nascimento: "))
            senha =  int(input("Digite sua senha: "))
            input("Aperte 'Enter' para entrar")
            agencia = 12345
            
        
        print("\n--------------------------------------------------")
        print(f"\nolá {nome}                   agencia: {agencia}")
        print("\nO que deseja fazer?")
        escolha = int(input("1- Sacar \n2-Depositar \n3-transferencia \n:"))
        if escolha == 1:
            print(self.sacar())
        elif escolha == 2:
            print(self.depositar())
        else:
            print(self.transferencia())

    def sacar(self):
        print("\n-------------------------------")
        self.saque = float(input("Quanto você deseja sacar?: "))
        self.saldo = self.saldo - self.saque
        print(f"Você sacou: R${self.saque}")
        print(f"O seu saldo agora é: {self.saldo}")

    def depositar(self):
        print("\n-------------------------------")
        self.deposita = float(input("Quanto você desja depositar:  "))
        self.saldo = self.saldo + self.deposita
        print(f"Você depositou: R${self.deposita}")
        print(f"O seu saldo é: R${self.saldo}")

    def transferencia(self):
        print("\n-------------------------------")
        self.transferir = float (input("Quanto você deseja depositar:  "))
        self.quem = str(input("Quem voce deseja transferir o dinheiro (nome): "))
        self.saldo = self.saldo - self.transferir
        print("\nTransferencia feita com sucesso!")
        print(f"Você transferiu R${self.transferir} para a conta de {self.quem}")

teste = Banco(1400)    
teste.Entrar()'''

#####################################################################

# EXERCICIO 12

'''class LojaVirtual:
    def __init__(self, nome, senha ):
        self.nome = nome
        self.senha = senha
        self.lista_produtos = []
        self.carrinho_compras = []

        # print para o inico da loja
        print("BEM VINDOS(AS) A LOJA VIRTUAL DA LU \n\n-Aqui vendemos peças de roupas para todos os tipos de estilos!! \n-Todos são divos e divas!!!")
        
    def cadastrar(self):
        while True:
            print("------------------------------------------")
            escolha = str(input("Você deseja cadastrar algum produto: (s/n): "))
            if escolha == 'n':
                print("Cadastro dos produtos encerrado")
                break

            if escolha == 's':
                self.nome_produto = str(input("\nDigite o nome do produto que deseja cadastrar: "))
                self.num_produto = int(input("Digite o numero do produto: "))
                self.preco_produto = float(input("Digite o preço do produto: "))
                self.desconto_produto = int(input("Digite o desconto do produto: "))

            produtos = {
                'nome': self.nome_produto,
                'ID produto': self.num_produto,
                'preço' : self.preco_produto,
                'desconto' : self.desconto_produto
            }
            self.lista_produtos.append(produtos) #adiciona o prduto na lista
            print("\n--------------------------------------")
            print(f"Produto {self.nome_produto} cadastrado!")
            # print(self.lista_produtos) #print dos produtos


    def mostrar_produtos(self):
        # conta do preço do produto com o desconto
        self.preco_desconto = self.preco_produto * (1 - self.desconto_produto / 100)
        print("-------------------------------------")
        print("\nProdutos Cadastrados!")
        for produtos in self.lista_produtos:
            print(f"\nNome: {produtos['nome']} \nID: {produtos['ID produto']} \nPreço: R$ {produtos['preço']} \nDesconto: {produtos['desconto']}% \nPreço do produto com desconto: { self.preco_desconto:.2f} ")

    def adicionar_carrinho(self):
        print("\n--------------------------------------")
        escolha = str(input("Qual produto você deseja adicionar no carrinho: "))
        for produtos in self.lista_produtos:
            if produtos['nome'].lower() == self.nome_produto.lower():
                self.carrinho_compras.append(produtos)
                print(f"Produto {self.nome_produto} adiconado no carrinho!")

    
    def exibir_carrinho(self):
        print("-------------------------------------")
        print("\nSeu carrinho")
        for produtos in self.carrinho_compras:
            print(f"\nNome: {produtos['nome']} \nID: {produtos['ID produto']} \nPreço: R$ {produtos['preço']} \nDesconto: {produtos['desconto']}% \nPreço do produto com desconto: { self.preco_desconto:.2f} ")
          


loja = LojaVirtual("Luana", 12345)
loja.cadastrar()
loja.mostrar_produtos()
loja.adicionar_carrinho()                         # NÃO ESTA TERMINADO AINDA - VOLTAR DEPOIS
loja.exibir_carrinho()'''

#################################################################################################################################################

# exercicio 13

'''class Agenda():
    def __init__(self):
        self.contatos = []

        print("---AGENDA TELEFONICA---")
        print("Veja seus contatos!")

    def menu(self):
        while True:
            opcoes = int(input("\nO que deseja fazer? \n1 Adicionar \n2 Remover \n3 visualizar contatos \n: "))
            if opcoes == 1:
                self.adicionar()
            elif opcoes == 2:
                self.remover()
            else:
                self.buscar_contatos()

    
    def adicionar(self):
        escolha = str(input("\nVocê deseja adicionar um contato novo? (s/n) "))
        if escolha == 's':
            nome = str (input("Digite o nome do contato: "))
            numero = str(input("Digite o numero do contato: "))
            self.contatos.append({'nome': nome, 'numero': numero})
            print(f"Contato {nome} cadastrado com sucesso!")
            print("---------------------------------")
        else:
            print("muito obg")
            

    def remover(self):
        print("\n------------------------")
        print("Remover contatos")
        removerContato = str(input("\nDigite o contato que voce deseja remover: "))
        for contato in self.contatos:
            if contato['nome'] == removerContato:
                self.contatos.remove(contato)
                print(f"Contato {removerContato} removido com sucesso!")

    def buscar_contatos(self):
       print("\n-----------------------------")
       print("Contatos cadastrados")
       if not self.contatos:
            print("Nenhum contato encontrado")
       else:
        for contato in self.contatos:
            print(f"\nNome: {contato['nome']} \nNumero: {contato['numero']}")

        
agendaTelefonica = Agenda()
agendaTelefonica.menu()'''

#############################################################################

# Exercicio 14

'''class MaquinaDeVendas():

    def __init__(self):
        self.lista_produtos = []
        self.quantidadeEstoque = []
        self.selecionar = []

    print("Bem vindo(a) a maquina de vendas da DS16!!!!")
    print("Aqui você encontra tudoooo que precisaaaaaa")

    def menu(self):
        while True:
            opcoes = int(input("\nO que deseja fazer? \n1 cadastrar produto \n2 selcionar para compra \n3 Pagamento \n4 Visualizar estoque \n: "))
            if opcoes == 1:
                self.cadastrarProduto()
            elif opcoes == 2:
                self.selcionarProduto()
            elif opcoes == 3:
                self.pagamento()
            else:
                self.estoque()

    def cadastrarProduto(self):
        self.nome_produto = str(input("\nDigite o nome do produto que deseja cadastrar: "))
        self.preco_produto = float(input("Digite o preço do produto: "))
        self.estoqueProdutos = int(input("Digite a quantidade em estoque: "))
        produtos = {
            'nome': self.nome_produto,
            'preço' : self.preco_produto,
            'estoque' : self.estoqueProdutos
        }
        self.lista_produtos.append(produtos) #adiciona o prduto na lista
        print("\n--------------------------------------")
        print(f"Produto {self.nome_produto} cadastrado!")
       

    def selcionarProduto(self):
        escolha = str(input("Digite qual produto você deseja comprar: "))
        for produtos in self.lista_produtos:
            if produtos['nome'].lower() == self.nome_produto.lower():
                self.selecionar.append(produtos)
                print(f"Produto {self.nome_produto} adicionada para compra")
                self.estoqueProdutos -= 1

    def pagamento(self):
        print("----Pagamento dos produtos----")
        print("\nSeus produtos:")
        totalCompra = 0
        for produtos in self.selecionar:
            print(f"\nNome: {produtos['nome']} \nPreço: R$ {produtos['preço']} ")
            totalCompra += produtos['preço']
            print(f"\nO total da sua compra é: {totalCompra}")
            pagar = float(input("digite o valor para o pagamento:  "))
            if pagar >= totalCompra:
                troco = pagar - totalCompra
                print(f"Pagamento efetuado com sucesso! \nSeu troco é {troco:.2f}")
            
    def estoque(self):
        print("\n-------------------------------")
        print("---Estoque---")
        for produto in self.lista_produtos:
            print(f"Produto: {produto['nome']} \nEstoque: {self.estoqueProdutos}")

maquina = MaquinaDeVendas()
maquina.menu()'''

########################################################################

# exercicio  15

# class JogoCartas():


# exercicio 16

class Redessocias():
    def __init__(self):
        self.amigos = []
        self.usuarios = []
        self.postagem = []

    def menu(self):
        print("Bem vindo(a)  ao instaDIVA")
        print("\n👩🏽| Luana              Bem vinda")

        while True:
            escolha = int(input("\nO que você deseja fazer? \n1- Adicionar Amigos \n2- Publicar mensagem \n3- Comentar \n4- Buscar Usuario \n5- sair \n:"))
            if escolha == 1:
                self.adicionarAmigos()
            elif escolha == 2:
                self.publicarMensagem()
            elif escolha == 3:
                self.comentar()
            elif escolha == 4:
                self.buscarUsuario()
            else:
                print("Saindo do instaDIVA...")
                break

    def adicionarAmigos(self):
        nome = input("\nDigite o nome de um amigo, que deseja adicionar: ")
        if nome not in self.amigos:
            self.amigos.append(nome)
            print(f"{nome} foi adicionado(a) aos seus amigos DIVOS")
        else:
            print(f"{nome} já é seu(sua) BESTDIVO")

    def publicarMensagem(self):
        print("\n--------------------MENSAGENS--------------------")
        nomeUsuario = input("Digite seu nome para publicar sua mensagem diva: ")
        mensagem = input("Digite a mensagem: ")
        self.postagem.append({'usuario': nomeUsuario, 'mensagem': mensagem})
        # Adiciona o usuário aos usuários registrados, caso não esteja na lista
        if nomeUsuario not in self.usuarios:
            self.usuarios.append(nomeUsuario)
        print(f"\nMensagem publicada por {nomeUsuario}: \n{mensagem}")

    def comentar(self):
        nomeUsuario = input("Digite seu nome para comentar em algum post: ")
        if nomeUsuario not in self.usuarios:
            print(f"Usuário {nomeUsuario} não encontrado. Registre-se antes de comentar.")
            return
        print(f"\nPostagens de {nomeUsuario}:")
        # Exibe as postagens de um usuário específico
        for postagem in self.postagem:
            if postagem['usuario'] == nomeUsuario:
                print(f"\nMensagem: {postagem['mensagem']}")
                comentario = input("Deixe aqui seu comentário DIVO: ")
                print(f"O comentário: '{comentario}' foi adicionado ao post de {nomeUsuario}.")

    def buscarUsuario(self):
        busca = input("\nDigite o nome do usuário que deseja buscar: ")
        encontrados = [usuario for usuario in self.usuarios if busca.lower() in usuario.lower()]
        if encontrados:
            print(f"Usuários encontrados: {', '.join(encontrados)}")
        else:
            print("Nenhum usuário encontrado com esse nome.")

redes = Redessocias()
redes.menu()