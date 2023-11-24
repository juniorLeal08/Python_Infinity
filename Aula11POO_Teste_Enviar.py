# [PY-A11] Você foi contratado para desenvolver o software de controle de um elevador inteligente. A classe Elevador foi
# criada para modelar esse sistema e possui os seguintes atributos: totalCapacidade, atualCapacidade,
# totalAndar e atualAndar, que representam, respectivamente, a capacidade máxima do elevador, a capacidade atual,
# o total de andares do prédio e o andar atual do elevador.
# A classe Elevador também possui os seguintes métodos:
# Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo".
# Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".
# Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo".
# Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".
# Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas
# presentes no elevador e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".
# Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes
# e exibe "Saindo uma pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".

class Elevador():
    def __init__(self,totalcapacidade,atualcapacidade,totalandar,andaratual):
        self.totalcapacidade = totalcapacidade
        self.atualcapacidade = 0
        self.totalandar = totalandar
        self.andaratual = 0

    def subir(self):
        if self.andaratual < self.totalandar:
            self.andaratual += 1
            print("Subindo...")
        else:
            print("Você Está No Andar Mais Alto!! ")

    def descer(self):
        if self.andaratual >0:
            self.andaratual -=1
            print("Descendo....")
        else:
            print("Você Está No Terreo!! ")

    def entrar(self):
        if self.atualcapacidade < self.totalcapacidade:
            self.atualcapacidade += 1
            print("Entrando Uma Pessoa. ")
        else:
            print("O Elevador Está Cheio!Aguarde...")

    def sair(self):
        if self.atualcapacidade >0:
            self.atualcapacidade-=1
            print("Saindo Uma Pessoa. ")
        else:
            print("Não Tem Ninguem No Elevador. ")