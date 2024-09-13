#Curso DS - Semana 23 - Objeto: conhecendo OOP - Teoria e Prática
#criando a class chamada Produto
class Produto:
    def __init__(self, nome, marca, preco):
        #Definindo os atributos
        self.nome = nome
        self.marca = marca
        self.preco = preco

    # Definindo Metodos
    #Método Exibir dados
    def exibir_informacoes(self):
        print(f"Nome: {self.nome} - Marca: {self.marca} - Preco: R${self.preco:.2f}")

    #Criando Método exibir 10 vezes
    def exibir_10vezes(self):
        n=1
        while n<=10:
            print("Nome - ",n,"  ",self.nome)
            n+=1
    #Criando Método Calcular Juros
    def desconto_10(self):
        print(f"Produto: {self.nome}, Valor "
              f"Produto: {self.preco}, "
              f"Desconto 10% : {self.preco*.10}")

prod2 = Produto("SmartTV", "Philips", 4500)
print(prod2.nome)
prodx = Produto("Notebook","Samsung",3600)
print(prodx.nome,prodx.preco)
prodx.exibir_10vezes()
prodx.exibir_informacoes()
print("Valor parcelado em 3 vezes",prodx.preco/3)

















#prod2.exibir_10vezes()

