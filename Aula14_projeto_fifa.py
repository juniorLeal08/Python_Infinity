# Nesta aula vamos desenvolver um sistema para a FIFA.
# A FIFA te contratou para desenvolver um sistema em Python para cadastro dos
# times de um novo campeonato.
# Nesse sistema deve ser possível cadastrar times, jogadores e comissão técnica.
# O sistema deve apresentar um menu para escolha de cadastro de jogador, time ou
# comissão técnica.
# O sistema deve pedir para cadastro do time: O nome do time, a cidade onde o time
# fará os jogos como mandante e o nome do mascote do time.
# Para os jogadores, deverá ser possível cadastrar o nome do jogador, o nome do
# time cujo ele atua, e o número da camisa.
# Para a comissão técnica, teremos o técnico, o auxiliar e o preparador físico
# Para o técnico, o sistema deve cadastrar: O nome do técnico, o nome do time que
# ele comanda, e o esquema tático preferido (4-3-3 ou 4-4-2 por exemplo), o técnico
# deverá ter um método chamado dar_coletiva que retorna uma string: "O técnico
# está dando uma coletiva de imprensa".
# Para o auxiliar, deverá pedir os mesmos atributos e o método dar_coletiva retorna "O
# auxiliar está dando uma coletiva de imprensa".
# Para o preparador físico, o sistema deverá pedir o nome do preparador, o nome do
# time que ele prepara e, pedir qual parte do elenco ele prepara, "jogadores de linha"
# ou os "goleiros", deverá ter também o método dar_coletiva que retorna: "O
# preparador físico está dando uma coletiva de imprensa".
# Para desenvolver esse sistema, utilize todos os conceitos de programação
# orientada a objetos que foram estudados

#Projeto_FIFA

class Time:
    def __init__(self,nome:str,cidade:str,mascote:str):
        self.__nome = nome
        self.__cidade = cidade
        self.__mascote = mascote

    def getNome(self):
        return self.__nome
    def setNome(self,novo_nome):
        self.__nome=novo_nome
        return self.__nome
    
    def getCidade(self):
        return self.__cidade
    def setCidade(self,novo_cidade):
        self.__cidade=novo_cidade
        return self.__cidade
    
    def getMascote(self):
        return self.__mascote
    def setMascote(self,novo_mascote):
        self.__mascote=novo_mascote
        return self.__mascote


class Jogador:
    def __init__(self,nome:str,time:str,numero_camisa:int):
        self.__nome = nome
        self.__time = time
        self.__numero_camisa = numero_camisa

    def getNome(self):
        return self.__nome
    def setNome(self,novo_nome):
        self.__nome=novo_nome
        return self.__nome
    
    
    def getTime(self):
        return self.__time
    def setTime(self,novo_time):
        self.__time=novo_time
        return self.__time
    

    def getNumero_camisa(self):
        return self.__numero_camisa
    def setNumero_camisa(self,novo_numero_camisa):
        self.__numero_camisa=novo_numero_camisa
        return self.__numero_camisa
    

class Comissao_tecnica:
    def __init__(self,nome:str,time:str,esquema_tatico:str):
        self.__nome = nome
        self.__time = time
        self.__esquema_tatico = esquema_tatico
    def dar_coletiva(self):
        return ""

    def getNome(self):
        return self.__nome
    def setNome(self,novo_nome):
        self.__nome=novo_nome
        return self.__nome
    
    def getTime(self):
        return self.__time
    def setTime(self,novo_time):
        self.__time=novo_time
        return self.__time
    
    def getEsquema_tatico(self):
        return self.__esquema_tatico
    def setEsquema_tatico(self,novo_esquema_tatico):
        self.__esquema_tatico=novo_esquema_tatico
        return self.__esquema_tatico


class Tecnico(Comissao_tecnica):
    def __init__(self, nome:str, time:str, esquema_tatico:str):
        super().__init__(nome, time, esquema_tatico)
        
    def dar_coletiva(self):
        return f"O técnico {self.__nome} Esta Dando Uma Coletiva De Imprensa Agora"
    
class Aux_tecnico(Comissao_tecnica):
    def __init__(self, nome:str, time:str, esquema_tatico:str):
        super().__init__(nome, time, esquema_tatico)
    def dar_coletiva(self):
        return f"O Auxiliar técnico {self.__nome} Esta Dando Uma Coletiva De Imprensa Agora"

class Preparador_fisico(Comissao_tecnica):
    def __init__(self, nome:str, time:str,part_elenco:str):
        super().__init__(nome, time,part_elenco)
        self.__part_elenco = part_elenco
    def dar_coletiva(self):
        return f"O Preparador Fisico {self.__nome} Esta Dando Uma Coletiva De Imprensa Agora"


while True:
    menu = int(input(f"""
            Registro Fifa
        Escolha Uma Opção:
        1. Cadastrar Time
        2. Cadastrar Jogador
        3. Cadastrar Comissão Técnica
        4. Sair      
    """))

    match menu:
        case 1:
            nome = str(input("Digite o Nome Do Time: "))
            cidade = str(input("Digite A Cidade Do Time: "))
            mascote = str(input("Digite o Nome Do Mascote Do Time: "))
            time = Time(nome=nome,cidade=cidade,mascote=mascote)
        case 2:
            nome = str(input("Digite o Nome do Jogador: "))
            time = str(input("Digite o Time do Jogador: "))
            numero_camisa = int(input("Digite o Numero Da Camisa do Jogador: "))
            jogador = Jogador(nome=nome,time=time,numero_camisa=numero_camisa)
        case 3:
            nome_tecnico = str(input("Digite o Nome do Tecnico: "))
            time_tec = str(input("Digite o Time do Tecnico: "))
            esquema_tatico = str(input("Digite o Esquema Tatico do Tecnico(4-3-3 ou 4-4-2): "))
            tecnico = Tecnico(nome=nome_tecnico,time=time_tec,esquema_tatico=esquema_tatico)

            nome_aux_tecnico = str(input("Digite o Nome do Auxiliar Tacnico: "))
            time_aux = str(input("Digite o Time Do Auxiliar Tecnico: "))
            esquema_tatico_aux = str(input("Digite o Esquema Tatico Do Auxiliar Tecnico: "))
            aux_tecnico = Aux_tecnico(nome=nome_aux_tecnico,time=time_aux,esquema_tatico=esquema_tatico_aux)

            nome_pre_fisico = str(input("Digite o Nome do Preparador Fisico: "))
            time_pre_fisico = str(input("Digite o Time do Preparador Fisico: "))
            part_elenco = str(input("Digite Qual A Parte Do Elenco O Preparador Fisico Treina:(Jogador Linha ou Goleiro) "))
            pre_fisico = Preparador_fisico(nome=nome_pre_fisico,time=time_pre_fisico,part_elenco=part_elenco)
        case 4:
            print("Encerrando O Programa.....")
            break
            


















