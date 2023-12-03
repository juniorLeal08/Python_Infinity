import mysql.connector

db_config = {
    "host":"localhost",
    "user": "root",
    "password": "Nethan123@",
    "database": "Livraria"
}


def mexer_no_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_o_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    lista_de_livros = cursor.fetchall()
    cursor.close()
    conexao.close()
    return lista_de_livros


while True:
    menu = int(input("""
        Escolha uma opção:
        1 - Inserir Livro
        2 - Ver livros cadastrados
        3 - Editar Livro
        4 - Deletar Livro
        0 - Sair
    """))
    
    if menu ==1:
        nome_do_livro = str(input("Digite O Nome Do Livro: "))
        genero_do_livro = str(input("Digite O Gênero Do Livro: "))
        autor_do_livro = str(input("Digite O Autor Do Livro: "))
        ano_do_livro = int(input("Digite O Ano De Lançamento Do Livro: "))


        mexer_no_banco(f'''
        insert into Livro values(
        default,
        "{nome_do_livro}",
        "{genero_do_livro}",
        "{autor_do_livro}",
        "{ano_do_livro}"
        );
        ''')
    elif menu == 2:
        print(consultar_o_banco("SELECT * FROM Livro"))
    
    elif menu == 3:
        print("Livro Atualizado")
    elif menu == 4:
        print(consultar_o_banco("SELECT * FROM Livro"))
        escolha = int(input("Digite o ID do livro que deseja deletar: "))
        mexer_no_banco(f"Delete FROM Livro WHERE ID ={escolha}")

    elif menu == 0:
        break
    else:
        print("Opção Invalida!!")









