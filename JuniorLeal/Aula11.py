# CRIE UMA CLASSE CHAMADA ANIMAL QUE TEM COMO PARAMETRO
# ESPECIE, SEXO, RAÇA, COR, IDADE
# E QUE TENHA COMO FUNÇOES
# ANDAR, CORRER, DORMIR, COMER

# PEDE PRO USUÁRIO ESCREVER OS 4 PARAMETROS
# CRIA UMA VARIAVEL INSTANCIANDO O OBJETO
# E MOSTRA NA TELA UMA DEMOSNTRAÇÃO DE TODAS AS FUNÇÕES
# E TAMBÉM TODOS OS ATRIBUTOS

# class Animal():
#     def __init__(self,especie,sexo,raca,cor,idade):
#         self.especie = especie
#         self.sexo = sexo
#         self.raca = raca
#         self.cor = cor
#         self.idade = idade

#     def andar(self):
#         return f"o animal {self.especie} andando!"
#     def correr(self):
#         return f"o animal {self.especie} correndo!"
#     def domir(self):
#         return f"o animal {self.especie} dormindo!"
#     def comer(self):
#         return f"o animal {self.especie} comendo!"

# especie = input(str("Digite a especie do animal: "))
# sexo = input(str("Digite o sexo do animal: "))
# raca = input(str("Digite a raça do animal: "))
# cor = input(str("Digite a cor do animal: "))
# idade = input(str("Digite a idade do animal: "))

# animal01 = Animal(especie,sexo,raca,cor,idade)

# print(animal01.especie)
# print(animal01.sexo)
# print(animal01.raca)
# print(animal01.cor)
# print(animal01.idade)

# print(animal01.andar())
# print(animal01.correr())
# print(animal01.domir())
# print(animal01.comer())

# Crie uma classe chamada Fatura que possa ser utilizada por uma loja de
# suprimentos de informática para representar uma fatura de um item
# vendido na loja. Uma fatura deve incluir as seguintes informações como
# atributos:

# Sua classe deve ter um construtor que inicialize todos os atributos menos o
# valor total da fatura. Além disso, forneça um método chamado
# gerar_fatura que calcula o valor da fatura (isto é, multiplicar a quantidade
# pelo preço por item).

# o nome do item;
# o preço unitário do item;
# quantidade de item a ser faturado;
# valor total da fatura;


# class Fatura():
#     def __init__(self, produto,preco,quant):
#         self.produto = produto
#         self.preco = preco
#         self.quant = quant


#     def gerar_fatura(self):
#         calcular =  self.quant * self.preco
#         return calcular

# produto = str(input("Digite o nome do produto vendido: "))
# preco = float(input("Digite o valor do produto vendido: "))
# quantidade = int(input("Digite a qunatidade de produtos vendidos: "))


# fatura1 = Fatura(produto=produto,preco=preco,quant=quantidade)

# print(f"Valor Total da Fatura: R$:{fatura1.gerar_fatura()}")


# ATIVIDADE EXTRA
# FAÇA UMA CLASSE CHAMADA CONTA BANCARIA COM OS
# SEGUINTES ATRIBUTOS:
# NOME DO TITULAR
# SALDO DA CONTA
# E AS SEGUINTES FUNÇÕES
# DEPOSITAR (que aumenta o saldo)
# SACAR (que retira do saldo se for suficiente, se não
# mostra uma mensagem de saldo insuficiente)
# EXIBIR (que mostra o saldo atual)



class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return self.saldo
        else:
            print("Saldo insuficiente")
        
    def exibir(self):
        return f"Seu saldo atual é: R${self.saldo}"
    
nome = str(input("Digite seu nome: "))
saldo = float(input("Digite seu saldo: "))
conta1 = ContaBancaria(nome=nome, saldo=saldo)

while True:
    menu = int(input("""
            1 - Depositar
            2 - Sacar
            3 - Exibir saldo
            0 - Sair
    """))

    if menu == 1:
        valor = float(input("Digite o valor que você quer depositar: "))
        conta1.depositar(valor)
    elif menu == 2:
        valor = float(input("Digite o valor que você quer sacar: "))
        conta1.sacar(valor)
    elif menu == 3:
        print(conta1.exibir())
    elif menu == 0:
        break
    else:
        print("Opção inválida")






























