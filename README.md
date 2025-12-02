# projeto-controle-de-estoque-de-jogos
Este repositório foi criado para o projeto final da disciplina de Introdução à Programação, ministrada pelo prof. Me. Raphael Guedes, para a turma de Ciência da Computação do INF - UFG 2025.2. O projeto consiste num controle de estoque de jogos completo.

Através desse arquivo é possível compreender o funcionamento do código e como preencher os campos de dados para uma experiência completa e de bom funcionamento. Apresentaremos as respostas esperadas, limitações e possibilidades de entrada de dados, indicando com um passo a passo intuitivo que acompanha o workflow do código completo. Este arquivo está separado em sessões.

I. Introdução
II. Cadastro de Produtos no Estoque
III. Cadastro de Usuário
IV. Busca de Produtos
V. Carrinho de Compras
VI. Considerações finais
________________________________________________________________________________________________________________________________________________________________________

I. INTRODUÇÃO

O objetivo geral desse repositório é realizar o controle de um estoque de jogos. A princípio, pensamos nas bases do projeto, que seriam voltadas à um possível empreendedor do ramo de jogos de videogame, então organizamos primeiro o nosso estoque. Um bom estoque permite um cadastro de produtos simplificado e completo, que registre cada dado de maneira certa e organizada, então focamos em obter uma ótima visualização de dados e delimitar bem as restrições de cada entrada de dados, pois, se o estoque é bagunçado, consequentemente o resto do empreendimento também será. Após a realização dessa etapa, decidimos expandir: um código que atenda o empreendedor e também o cliente. E assim nasceu o nosso cadastro de usuário, que coleta dados pessoais e dados do universo dos jogos, como preferências por gênero de jogo e "nicknames"! Dessa forma conseguimos desenvolver dois cadastros completos, e esses dois se convergem no nosso algortimo de busca no estoque. A busca une os dados do estoque e do usuário e consegue informar com precisão se aquele jogo buscado existe, quais os melhores jogos de acordo com a preferência de gênero do cliente e até mesmo um sistema de recomendações. Portanto, para finalizar, adicionamos o código do carrinho e compras para uma experiência imersiva mais completa e que complementa o nosso código de estoque com relatórios dos jogos que saíram do estoque.

________________________________________________________________________________________________________________________________________________________________________

II. CADASTRO DE PRODUTOS NO ESTOQUE

Nosso código se inicia com o cadastro de jogos no estoque. O usuário recebe instruções escritas sobre como preencher os campos para cadastrar um ou mais jogos.
Assim, o usuário pode cadastrar quantos jogos quiser, definindo um código de identificação para o jogo, preço, nome, requisitos, avaliações e mais. Este estoque já começa com 5 jogos cadastrados, a franquia Dark Souls e a franquia The Last of Us, todos com informações completas e reais retiradas da plataforma Steam. O usuário pode então cadastrar mais jogos ou apenas não cadastrar nenhum, deixando o estoque com somente estes 5 jogos fixos. Ao final do código, será informado: a quantidade de jogos cadastrados, informações indiviuais sobre cada jogo, a quantidade de jogos total do estoque (inclui cópias por jogo) e o valor total do estoque (soma dos preços de todas as cópias).

 1. Passo a passo | Como cadastrar um jogo no estoque?

   1. Defina um código de identificação (ID) para o jogo que será cadastrado.

Pode-se usar letras, números e símbolos. Recomendado: Iniciais da empresa + código numérico.
Ex.: FS001 (Empresa: FromSoftware; Primeiro jogo cadastrado dessa empresa), FS002, FS003 ...


   2. Insira o nome do jogo que será cadastrado.

Pode-se usar letras, números e símbolos, afinal, nomes de jogos podem variar bastante.
Recomendado: colocar o nome do jogo de maneira organizada, utilizando espaços e letras maiúsculas/minúsculas se necessário.
Ex.:
NÃO FAÇA - darksouls
FAÇA - Dark Souls 

   3. Insira o nome da empresa que desenvolveu o jogo.
Pode-se usar letras, números e símbolos.
Recomendado: colocar o nome completo da empresa de maneira organizada, utilizando espaços e letras maiúsculas/minúsculas se necessário.
Ex.: Riot Games, Blizzard Entertainment, EA, Naughty Dog ...


   4. Insira o gênero do jogo - somente um, então utilize o gênero principal.
Utilizar letras e obedecer às regras da plataforma de gêneros contemplados, que são:  "rpg", "fps","survival","moba","gacha","terror","puzzle","esportes","chill","coop".
O código verifica se o gênero digitado se configura em uma dessas opções, caso o usuário falhe, ele é conduzido à tentar novamente com o auxílio da lista de gêneros suportados.

   5. Insira o ano de lançamento do jogo.
Utilizar números INTEIROS.
Esse código restringe o usuário a informar um ano igual ou maior que 1980, pois a plataforma não suporta jogos de anos anteriores.

   6. Insira a data de adição do jogo ao estoque.
Utilizar números INTEIROS que atendam ao estilo DD/MM/AAAA.
O código verifica se o usuário colocou a data no formato indicado, caso não, ele é orientado à repetir a ação de maneira correta.
Ex.: 19/11/2025 - válido!
     32/01/2025 - inválido!

   7. Defina o preço do jogo em reais.
Utilizar números com ponto flutuante - FLOAT!
Aqui o usuário informa o preço do jogo, em reais, que é automaticamente adaptado para o formato: R$0.00.
Ex.: entrada - 175
     saída - R$175.00

   8. Insira a avaliação do jogo de 1 a 5 estrelas.
Aqui o usuário é orientado sobre como o sistema de avaliação por estrelas funciona:
1. Muito Ruim / 2. Ruim / 3. Mediano / 4. Bom / 5. Muito Bom
Qualquer número ou caractere que não sejam os números: 1, 2, 3, 4, 5; é invalidado.
Os números são transformados em estrelinhas (emojis) por uma função simples.

   9. Insira uma breve descrição sobre o jogo.
Aqui o usuário tem um momento para descrever o jogo, informando mais sobre sua história ou seus objetivos. 
 
   10. Insira a classificação indicativa do jogo.
Aqui o usuário é orientado a indicar a idade permitida para jogar, seguindo os padrões brasileiros: 0, 10, 12, 14, 16 e 18 anos.
Há uma verificação, números que fugirem desse padrão são invalidados. O número 0 é identificado como classificação LIVRE e posteriormente é trocado por L.

   11. Defina a quantidade de cópias disponíveis desse jogo no estoque.
Aqui o usuário insere um número INTEIRO, correspondente às cópias existentes desse jogo no estoque.

   12. Insira os requisitos para rodar esse jogo.
O usuário deve informar os requisitos para rodar esse jogo. É informada uma sequência a ser seguida:
1. Processador (CPU)
2. Memória RAM
3. Placa de Vídeo (GPU)
4. Armazenamento
Não há uma verificação ou limitação dessa etapa, visto as diversas variáveis existentes para esses componentes, mas as instruções são claras e definidas DUAS VEZES ao longo do programa.
   
   13. Insira as plataformas que rodam esse jogo.
Aqui o usuário informa quais plataformas podem rodar esse jogo.
Ex.: PC, Xbox, Playstation, Wii, Nintendo Switch, Android, iOS...

Como interromper cadastro de jogos?
O programa continua rodando num loop, para que seja possível cadastrar vários jogos de uma vez. Caso queira interromper o cadastro de jogos após ter atingido a quantidade desejada, basta finalizar o cadastro do jogo atual (preenchendo todos os campos corretamente) e, quando o loop recomeçar, da parte de código de identificação, basta inserir: "sair" que o código será encerrado e o registro do estoque será impresso, informando a quantidade de jogos cadastrados e jogos diferentes, informações individuais por jogo, total de cópias no estoque e valor total ($$$) do estoque.
 
________________________________________________________________________________________________________________________________________________________________________


III. CADASTRO DE USUÁRIO

Pensamos num código que atendesse tanto um vendedor de jogos quanto um cliente em busca de jogos para comprar. Portanto, desenvolvemos o cadastro de usuário, que permite a realização de operações entre o nosso estoque e um possível cliente. O usuário se cadastra com informações pessoais, tais como nome, idade e e-mail, e também informações relacionadas ao universo dos jogos como estilo de jogo favorito e nickname. Durante o cadastro de usuário, também são informadas instruções e são feitas verificações para ter certeza que todos os dados foram preenchidos corretamente.


1. Nome completo
Aqui o usuário informa o seu nome completo para o cadastro.

2. Nome de usuário
Aqui o usuário informa o seu "nickname", ou seja, apelido no jogo. Muito comum na comunidade gamer!

3. E-mail
Aqui o usuário deve informar o seu e-mail. O nosso código verifica se o e-mail atende ao formato: email@gmail.com
Caso haja falhas nesse formato, o usuário é alertado e conduzido a preencher este campo novamente da maneira correta.
O código verifica se esse e-mail já foi cadastrado e informa ao usuário.

5. Número de telefone
Aqui o usuário informa o seu número de telefone que deve atender ao formato: 62 123456789
Os números utilizados foram figurados, para indicar que deve haver o DDD, espaço e uma sequência de 9 dígitos.
O código verifica se esse telefone já foi cadastrado e informa ao usuário.

6. Idade
Aqui o usuário informa a sua idade em anos.
O programa verifica a idade informada pelo usuário, idades válidas respeitam o limite 0 < idade < 120.

7. Preferências de gênero de jogo
Aqui o programa pergunta pelos 3 gêneros de jogo favoritos do usuário.
Esse código atende aos gêneros suportados pela plataforma, então caso o usuário tente digitar algo diferente, ele será informado do erro.

Como interromper cadastro de usuários?
O programa continua rodando num loop, para que seja possível cadastrar vários usuários de uma vez. Caso queira interromper o cadastro de usuários após ter atingido a quantidade desejada, basta finalizar o cadastro do usuário atual (preenchendo todos os campos corretamente) e, quando o loop recomeçar, da parte de nome completo do usuário, basta inserir: "sair" que o código será encerrado e o registro dos usuários será impresso, informando os dados devidamente inseridos.
________________________________________________________________________________________________________________________________________________________________________

IV. BUSCA DE PRODUTOS 

O nosso código de busca de produtos reúne informações do código de cadastro de produtos e do cadastro de usuário, importando as listas e dicionários que contém os dados necessários para conectar esses dois algoritmos. Na busca, podemos buscar jogos por diveras informações diferentes e inclusive requisitar recomendações com base no usuário.

BUSCAS
1. Busca por nome do jogo
Aqui o usuário deve inserir o nome do jogo ou parte dele, como o começo, e o código retornará uma lista com os jogos disponíveis, contendo seus nomes completos, gênero, preço e avaliação. O usuário então pode digitar o nome completo para obter informações gerais sobre aquele jogo.
Caso não haja um jogo com o nome inserido, o usuário será informado.

2. Busca por gênero do jogo
Aqui o usuário insere o gênero desejado. Mais uma vez a lista de gêneros suportados pela plataforma é mostrado. Caso o usuário digite um gênero não suportado, ele é avisado e o programa encerra, fazendo o usuário escolher essa opção no menu novamente. Se o usuário escolher um gênero válido, TODOS os jogos desse gênero serão exibidos com nome, gênero, preço e avaliação.

3. Busca por empresa do jogo
Aqui o usuário digite o nome de uma empresa e todos os jogos vinculados à ela serão mostrados.
O usuário deve digitar o nome correto da empresa, a fim de achar os jogos esperados. Caso não haja nenhum jogo daquela empresa, o usuário será alertado que nenhum jogo foi encontrado no estoque.

4. Busca por avaliação exata
O usuário escolhe um nível de avaliação específico e todos os jogos com aquela avaliação serão mostrados. Portanto, se o usuário escolher jogos de nota 3, todos os jogos de nota 3 serão mostrados e somente eles.
Caso o usuário digite um número fora da classificação adotada, ou seja, um número que não seja 1,2,3,4 ou  5, ele será alertado do erro e o programa será reiniciado.

5. Busca por preço máximo
Usuário insere um preço máximo para buscar.
Os jogos com preço inferior e até o preço inserido são listados, dos preços mais baixos para os mais caros.
Caso não haja um jogo mais barato ou do exato preço inserido, o usuário é alertado e o programa reinicia.

6. Busca por ano de lançamento exato
Usuário insere um ano para buscar.
Os jogos lançados naquele ano são listados com as suas informações b.
Caso não hajam jogos lançados naquele ano ou seja um ano inválido (menor que 1980) o usuário é alertado e o programa reinicia.

7. Recomendações personalizadas
Aqui é informada uma lista com os usuários cadastrados. O usuário digita o nome de usuário da pessoa alvo e então a plataforma recomenda jogos dos genêros de preferência escolhidos pelo usuário durante seu cadastro. É possível escolher quantas recomendações deseja receber, o padrão é 5.

8. Ver todos os jogos disponíveis
Mostra uma lista do estoque, mostrando as informações de todos os jogos cadastrados.

9. Ver todos os usuários cadastrados
Mostra uma lista dos usuários cadastrados com todas as suas informações.

0. Encerra o programa.

CONTROLE DO MENU DA BUSCA

O menu é orientado por números, cada número equivale a uma busca como foi supracitado. Ao finalizar uma busca, o programa te oferece duas opções: digite "V" para voltar ao menu ou "S" para fazer uma nova busca. Assim, o usuário pode ter uma liberdade maior.
________________________________________________________________________________________________________________________________________________________________________

V. CARRINHO DE COMPRAS
________________________________________________________________________________________________________________________________________________________________________

VI. CONSIDERAÇÕES FINAIS

Esse código foi pensado para proporcionar uma experiência mais imersiva e completa dentro dos limites do nosso conhecimento. Enfrentamos diversos desafios que, honestamente, foram essenciais para o nosso crescimento e desenvolvimento profissional. Aprendemos melhor fazendo e esse projeto é prova disso. Esse código é bem interessante e divertido, com diversas possibilidades, com certeza poderíamos adicionar ainda mais detalhes para torná-lo impecável e funcional. Porém, nosso objetivo foi cumprido e ficamos felizes com o nosso trabalho.

