# ALUNO: ARTHUR DA SILVA MARIZ
# TADS 2026.1 - SISTEMAS OPERACIONAIS

## INTRODUÇÃO

A atividade feita em 23/03/2026 na disciplina de Sistemas Operacionais tem como objetivo criar uma aplicação Web com Django por meio do uso de Dockers.

## RELATO DAS ATIVIDADES
Para começar, tive de criar um Dockerfile e esse arquivo é tipo uma receita onde todos os conteiners criados a partir dela terão a mesma configuração.
![Dockerfile](img\dockerfile.png)

Após isso, construi uma imagem chamada atividade-django-dev com esse dockerfile.
![Dockerfile](img\build.png)

Por fim, criei um conteiner com essa imagem
![Dockerfile](img\run.png)

Quando terminei de configurar o docker, comecei a mexer com a aplicação Django. Para isso, criei um projeto django pelo terminal, criei a aplicação e, como ela vem com o SQLite3 configurado como padrão, não tive de configurar o banco de dados.
![Dockerfile](img\djangosettings.png)

Os próximos passos foram de adicionar a aplicação as configurações na lista INSTALLED_APPS, modificar ALLOWED_HOSTS para aceitar todos tipos de conexão e migrar o banco de dados e criar o superusuário.
![Dockerfile](img\superusuario.png)

Para finalizar essa seção, criei um view simples, página de apresentação, no script padrão para isso no django e configurei para URL padrão de entrada ser nessa view.

Agora no teste da aplicação, iniciei o servidor de teste com esse comando no terminal:
![Dockerfile](img\servidorteste.png)

E acessei a porta onde está hospedada nossa aplicação Django para testar e apágina inicial é esta:
![Dockerfile](img\inicial.png)

Esta é a página para entrar como admin:
![Dockerfile](img\adminlogin.png)

E o painel de admin:
![Dockerfile](img\homeadmin.png)

Assim que o servidor recebe as requisições:
![Dockerfile](img/servidor.png)


## CONSIDERAÇÕES FINAIS
Com essa atividade, aprendi como cria uma aplicação Web e não imaginava que dava para fazer de forma tão simples. Existe alguns passos a passos até que extensos para realizar, mas parece uma etapa bem documentada. A importância do Docker ficou mais evidente também e me deu algumas ideias de como usá-lo para otimizar essa etapa inicial de configuração do Django. Não tive dificuldades na atividade, tudo estava documentado.