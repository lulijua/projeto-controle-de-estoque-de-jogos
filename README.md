# projeto-controle-de-estoque-de-jogos
Este repositório foi criado para o projeto final da disciplina de Introdução à Programação, ministrada pelo prof. Me. Raphael Guedes, para a turma de Ciência da Computação do INF - UFG 2025.2. O projeto consiste num controle de estoque de jogos completo.

Aqui é possível encontrar:

 1. Slides do projeto — dão uma visão geral do planejamento, execução, desafios e resultados do projeto.
 2. Guia de testes realizados — controle de testes que foram feitos para o bom funcionamento do código.
 3. Arquivos de Código — contém os códigos feitos para este programa.
 4. Instruções - o que esperar desse programa e como executá-lo?

--- INSTRUÇÕES ---
__________________

1.0 Cadastrando jogos no estoque

Nosso código se inicia com o cadastro de jogos no estoque. O usuário recebe instruções escritas sobre como preencher os campos para cadastrar um ou mais jogos.
Assim, o usuário pode cadastrar quantos jogos quiser, definindo um código para o jogo, preço, nome, requisitos, avaliações e mais. Este estoque já começa com 5 jogos cadastrados, a franquia Dark Souls e a franquia The Last of Us, todos com informações completas e reais retiradas da plataforma Steam. O usuário pode então cadastrar mais jogos ou apenas não cadastrar nenhum, deixando o estoque com somente estes 5 jogos fixos. Ao final do código, será informado: a quantidade de jogos cadastrados, informações indiviuais sobre cada jogo, a quantidade de jogos total do estoque (inclui cópias por jogo) e o valor total do estoque (soma dos preços de todas as cópias).

1.1 Passo a passo | Como cadastrar um jogo no estoque?

   1. Defina um código de identificação (ID) para o jogo que será cadastrado. Pode usar letras, números e símbolos. Recomendado: Iniciais da empresa + código numérico.
   2. Insira o nome do jogo que será cadastrado.
   3. Insira o nome da empresa que desenvolveu o jogo.
   4. Insira o gênero do jogo - somente um, então utilize o gênero principal.
   5. Insira o ano de lançamento do jogo.
   6. Insira a data de adição do jogo ao estoque.
   7. Defina o preço do jogo em reais.
   8. Insira a avaliação do jogo de 1 a 5 estrelas. 1 - muito ruim . . . . 5 - muito bom.
   9. Insira uma breve descrição sobre o jogo.
   10. Insira a classificação indicativa do jogo.
   11. Defina a quantidade de cópias disponíveis desse jogo no estoque.
   12. Insira os requisitos para rodar esse jogo.
   13. Insira as plataformas que rodam esse jogo.

 1.2 Passo a passo | Interromper cadastro de jogos.

 Não quer cadastrar outro jogo?
    1. Finalize o cadastro do jogo atual.
    2. Quando o programa resetar, ele pedirá automaticamente para que você insira o código de ID do próximo jogo.
    3. Insira "sair" no campo de ID do jogo.
    4. Assim, o programa será finalizado e informará o registro do estoque.
 


2. Cadastrando usuários

Pensamos num código que atendesse tanto um vendedor de jogos quanto um cliente em busca de jogos para comprar. Portanto, desenvolvemos o cadastro de usuário, que permite
a realização de operações entre o nosso estoque e um possível cliente. O usuário se cadastra com informações pessoais, tais como nome, idade e e-mail, e também informações relacionadas ao universo dos jogos como estilo de jogo favorito e nickname. Durante o cadastro de usuário, também são informadas instruções e são feitas verificações para ter certeza que todos os dados foram preenchidos corretamente.

3. Busca de Produto


