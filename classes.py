class Cachorro: 
    def  __init__(self, nome, raca, cor, idade):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.orelhas = 2
    
    def latir(self):
        print(f" {self.nome} diz: AU AU")
    
    def correr(self, kms):
        print(f"{self.nome} correu {kms} Km")
    
class Livro:
    def __init__(self, categoria, titulo, autor,personagens, indicacao):
        self.genero = categoria
        self.titulo = titulo
        self.autor = autor
        self.personagens = personagens
        self.indicacao = indicacao

    def abrir(self, pagina):
        print(f"O livro {self.titulo} foi aberto na pagina {pagina}")

    def __str__(self):
        return f"o nome do livro é {self.titulo}, do genero {self.genero}, escrita por {self.autor}."

    def __eq__(self, value):
        if(isinstance(value, Livro)):
            titulo_igual = self.titulo == value.titulo
            autores_iguais = self.autor == value.autor
            return titulo_igual and autores_iguais
        else:
            return False



livro_kamila = Livro("romance", "crepusculo", "J.K Rowling", ["Bela", "Edware"], "14 anos")
livro_kamila.abrir(10)
print(livro_kamila)