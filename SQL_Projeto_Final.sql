create database Livraria;
use Livraria;
create table Livro(
id int auto_increment primary key not null,
titulo varchar (255),
genero varchar (255),
nome_autor varchar (255) not null,
ano_publicacao int
);
create table Clientes(
id int auto_increment primary key,
nome varchar (255),
cpf varchar (16),
email varchar (255)
);
insert into Livro values(
default,
"Código limpo",
"Tecnologia",
"Robert Cecil Martin",
"2008"
);
insert into Livro values(
default,
"O Códificador limpo",
"Tecnologia",
"Robert Cecil Martin",
"2011"
);
insert into Livro values(
default,
"O Programador Pragmatico: De Aprendiz A Mestre",
"Tecnologia",
"Andy Hunt, Dave Thomas",
"1999"
);
insert into Livro values(
default,
"Padrões de Projetos:
Soluções Reutilizáveis de Software Orientados a Objetos,",
"Tecnologia",
" Erich Gamma, John Vlissides, Richard Helm, Ralph Johnson",
"1994"
);
insert into Livro values(
default,
"Arquitetura
limpa: O guia do artesão para estrutura e design de software.",
"Tecnologia",
"Kevlin Henney",
"2019"
);
select * from Livro;
delete from Livro where id=4;
delete from Livro where id=5;