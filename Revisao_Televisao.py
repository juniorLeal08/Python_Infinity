# FAÇA UMA CLASSE CHAMADA TELEVISAO QUE TEM OS ATRIBUTOS:
# NOME
# GÊNERO
# LANÇAMENTO
# E O MÉTODO:
# ASSISTIR (QUE RETORNA, VOCÊ ESTÁ ASSISTINDO {NOME})
# VER INFORMAÇÕES (QUE RETORNA TODAS AS INFORMAÇÕES EM QUESTÃO)

# CRIE UMA CLASSE FILHA CHAMADA FILME QUE HERDE TUDO DE TELEVISAO E CRIE UM NOVO ATRIBUTO CHAMADO duração
# E UM NOVO MÉTODO CHAMADO em_cartaz QUE RETORNA (O FILME {NOME} ESTÁ EM CARTAZ)
# POLIMORFISMO DO MÉTODO VER INFORMAÇÕES ADICIONANDO NO RETORNO A DURAÇÃO

# CRIE UMA CLASSE FILHA CHAMADA SERIE QUE HERDE TUDO DE TELEVISAO E CRIE UM NOVO ATRIBUTO CHAMADO temporadas 
# E UM NOVO MÉTODO CHAMADO maratonar QUE RETORNA (VOCÊ ESTÁ MARATONANDO A SÉRIO {NOME})
# POLIMORFISMO DO MÉTODO VER INFORMAÇÕES ADICIONANDO NO RETORNO AS TEMPORADAS


# FAÇA UM PROGRAMA COM UM MENU QUE PERGUNTA:
# 1 - ADICIONAR FILME
# 2 - VER FILMES
# 3 - DELETAR FILME
# 4 - ADICIONAR SÉRIE
# 5 - VER SÉRIES
# 6 - DELETAR SÉRIES
# 0 - SAIR

class Televisao:
    def __init__(self,nome, genero,lancamento,):
        self.__nome = nome
        self.__genero = genero
        self.__lancamento = lancamento

    def getnome(self):
        return self.__nome
    def setnome(self):
        return self.__nome

    def getgenero(self):
        return self.__genero
    def setgenero(self):
        return self.__genero

    def getlancamento(self):
        return self.__lancamento
    def setlancamento(self):
        return self.__lancamento


    def assistir(self):
        return f" Você Esta Assistindo {self.getnome()}"

    def ver_informacao(self):
        return f"""
        Nome: {self.getnome()}
        Gênero: {self.getgenero()}
        Lançamento: {self.getlancamento()}
        
        """

class Filme(Televisao):
    def __init__(self, nome, genero, lancamento,duracao):
        super().__init__(nome, genero, lancamento)
        self.__nome = nome
        self.__genero = genero
        self.__lancamento = lancamento
        self.__duracao = duracao

    
    def getnome(self):
        return self.__nome
    def setnome(self):
        return self.__nome

    def getgenero(self):
        return self.__genero
    def setgenero(self):
        return self.__genero

    def getlancamento(self):
        return self.__lancamento
    def setlancamento(self):
        return self.__lancamento

    def getduracao(self):
        return self.__duracao
    def setduracao(self):
        return self.__duracao


    def em_cartaz(self):
        return f" O Filme {self.getnome} Está Em Cartaz. "

    def ver_informacao(self):
        return f"""
        Nome: {self.getnome()}
        Gênero: {self.getgenero()}
        Lançamento: {self.getlancamento()}
        Duração: {self.getduracao()}
        """
    
class Serie(Televisao):
    def __init__(self, nome, genero, lancamento,temporadas):
        super().__init__(nome, genero, lancamento)
        self.__nome = nome
        self.__genero = genero
        self.__lancamento = lancamento
        self.__temporadas = temporadas


    def getnome(self):
        return self.__nome
    def setnome(self):
        return self.__nome

    def getgenero(self):
        return self.__genero
    def setgenero(self):
        return self.__genero

    def getlancamento(self):
        return self.__lancamento
    def setlancamento(self):
        return self.__lancamento
    
    def gettemporadas(self):
        return self.__temporadas
    def settemporadas(self):
        return self.__temporadas


    def maratonar(self):
        return f" Você Está Maratonando Á Serie {self.getnome()} "

    def ver_informacao(self):
        return f"""
        Nome: {self.getnome()}
        Gênero: {self.getgenero()}
        Lançamento: {self.getlancamento()}
        Temporadas: {self.gettemporadas()}
        """

lista_filme = []
lista_series = []


while True:
    menu = int(input(f"""
        Escolha Uma Opção:

     1 - ADICIONAR FILME
     2 - VER FILMES
     3 - DELETAR FILME
     4 - ADICIONAR SÉRIE
     5 - VER SÉRIES
     6 - DELETAR SÉRIES
     0 - SAIR

    """))
    match menu:
        case 1:
            nome = str(input(" Digite o Nome do Filme: "))
            genero = str(input(" Genero: "))
            lancamento = int(input(" Ano de Lançamento: "))
            duracao = str(input(" Tempo de Duração: "))
            filme1 = Filme(nome=nome,genero=genero,lancamento=lancamento,duracao=duracao)
            lista_filme.append(filme1)
        case 2:
            for titulo in lista_filme:
                print(f"""
                Nome do Filme: {titulo.getnome()}
                Gênero: {titulo.getgenero()}
                Ano de Lançamento: {titulo.getlancamento()}
                Duração: {titulo.getduracao()}

                """)
        case 3:
            contador = 1
            for titulo in lista_filme:
                print(f"""
                Titulo N°{contador}
                Nome do Filme: {titulo.getnome()}
                Gênero: {titulo.getgenero()}
                Ano de Lançamento: {titulo.getlancamento()}
                Duração: {titulo.getduracao()}
                
                """)
                contador += 1
                selecionar = int(input(" Digite o Numero Do Filme Que Você Quer Deletar: "))
                lista_filme.pop(selecionar-1)
        case 4:
            nome = str(input(" Digite o Nome da Serie: "))
            genero = str(input(" Genero: "))
            lancamento = int(input(" Ano de Lançamento: "))
            temporadas = int(input(" Temporada: "))
            serie1 = Serie(nome=nome,genero=genero,lancamento=lancamento,temporadas=temporadas)
            lista_series.append(serie1)
        
        case 5:
            for titulo in lista_series:
                print(f"""
                Nome do Serie: {titulo.getnome()}
                Gênero: {titulo.getgenero()}
                Ano de Lançamento: {titulo.getlancamento()}
                Temporadas: {titulo.gettemporadas()}

                """)

        case 6:
            contador = 1
            for titulo in lista_series:
                print(f"""
                Titulo N°{contador}
                Nome do Serie: {titulo.getnome()}
                Gênero: {titulo.getgenero()}
                Ano de Lançamento: {titulo.getlancamento()}
                Temporadas: {titulo.gettemporadas()}
                
                """)
                contador += 1
                selecionar = int(input(" Digite o Numero Da Serie Que Você Quer Deletar: "))
                lista_series.pop(selecionar-1)

        case 0:
            print(" Encerrando o Programa ........")
            break