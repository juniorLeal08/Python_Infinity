# [PY-A12]  Crie um código em Python que contenha as seguintes classes:
# A classe principal será chamada de "Material" e terá um construtor que recebe dois parâmetros:
# "titulo" e "autor_ou_editora". Essa classe também terá um método chamado "exibir_informacoes" que
# imprimirá na saída o título e o autor/editora do material.
# A classe "Livro" será uma subclasse da classe "Material" e terá um construtor que recebe três parâmetros:
# "titulo", "autor_ou_editora" e "genero". Essa classe também terá um método "exibir_informacoes" que chamará o método
# correspondente na classe "Material" e imprimirá o gênero do livro.
# A classe "Revista" será outra subclasse da classe "Material" e terá um construtor que recebe três parâmetros:
# "titulo", "autor_ou_editora" e "edicao". Essa classe também terá um método "exibir_informacoes" que chamará o método
# correspondente na classe "Material" e imprimirá a edição da revista.
# Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método "exibir_informacoes"
# para mostrar os detalhes de cada material.

class Material():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacoes(self):
        return f"""
        Informações Do Material:
        Titulo: {self.titulo}
        Autor: {self.autor}
        """

class Livro(Material):
    def __init__(self,titulo , autor,genero):
        super().__init__(titulo,autor)
        self.genero =genero

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"""
        Titulo:{self.titulo}
        Autor: {self.autor}
        Gênero:{self.genero}
        """)

livro = Livro(titulo= "O Hobbit",autor="J.R.R.Tolkien",genero="Aventura")
livro.exibir_informacoes()


class Revista(Material):
    def __init__(self,titulo,autor,edicao):
        super().__init__(titulo,autor)
        self.edicao =edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"""
        Titulo:{self.titulo}
        Autor: {self.autor}
        Edição:{self.edicao}
        """)

revista = Revista(titulo="Os Cavaleiros Do Zodiaco",autor="Masami Kurumada",edicao= 1)
revista.exibir_informacoes()

