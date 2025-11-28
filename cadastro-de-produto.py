# Esse código é responsável pelo cadastro dos produtos no ESTOQUE.
# Feito com classes e objetos do Python
# Autora: Luiza Juá

import datetime

# Cria uma classe 'Produto', no caso são os jogos, ela possui todas as informações que um jogo teria.
class Produto:
    def __init__(self, codigo_ID, nome_jogo, empresa_jogo, genero_jogo, lancamento_jogo, data_addEstoque, preco_jogo, avaliacao_jogo, descricao_jogo, classificacao_jogo, quantidade_jogo, requisitos_jogo, plataformas_jogo):
        
        self.identificacao = codigo_ID          # Código de identificação. 
        self.nome = nome_jogo                   # Nome do jogo.
        self.empresa = empresa_jogo             # Nome da empresa do jogo.
        self.genero = genero_jogo               # Gênero do jogo (FPS, RPG, MOBA...)
        self.lancamento = lancamento_jogo       # Ano de lançamento do jogo.
        self.data_adicao = data_addEstoque      # Data de adição ao estoque.
        self.preco = preco_jogo                 # Preço do jogo.
        self.avaliacao = avaliacao_jogo         # Avaliação de 1 a 5 estrelas do jogo.
        self.descricao = descricao_jogo         # Descrição breve do jogo.
        self.classificacao = classificacao_jogo # Classificação indicativa do jogo.
        self.quantidade = quantidade_jogo       # Quantidade de cópias desse jogo no estoque.
        self.requisitos = requisitos_jogo       # Requisitos mínimos para rodar esse jogo.
        self.plataformas = plataformas_jogo     # Plataformas que podem rodar esse jogo (PC, Xbox,Ps4 ...)
        
    def __str__(self):
        return f"ID DO JOGO: {self.identificacao}\nNOME DO JOGO: {self.nome}\nEMPRESA DO JOGO: {self.empresa}\nGÊNERO DO JOGO: {self.genero}\nANO DE LANÇAMENTO: {self.lancamento}\nDATA DE ADIÇÃO AO ESTOQUE: {self.data_adicao}\nPREÇO DO JOGO: {self.preco}\nAVALIAÇÃO DO JOGO (1 a 5 estrelas): {self.avaliacao}\nDESCRIÇÃO DO JOGO: {self.descricao}\nCLASSIFICAÇÃO INDICATIVA DO JOGO: {self.classificacao}\nQUANTIDADE DE CÓPIAS DISPONÍVEIS NO ESTOQUE: {self.quantidade}\nREQUISITOS MÍNIMOS PARA RODAR O JOGO (1. CPU, 2.RAM, 3.GPU, 4.Armazenamento): {self.requisitos}\nPLATAFORMAS DISPONÍVEIS: {self.plataformas}"

        # Converte avaliação para estrelinhas de avaliação (mto fofas)
    def exibir_formatado(self):
        estrelas = "★" * self.avaliacao + "☆" * (5 - self.avaliacao)
        
        # Formatar classificação --> indica que 0 = LIVRE.
        if self.classificacao == 0:
            classificacao_str = "LIVRE"
        else:
            classificacao_str = f"{self.classificacao} anos"
            
        # Formatar preço --> adiciona as barrinhas da tabela
        preco_formatado = f"R$ {self.preco:.2f}"
        
        print(f"╔{'═' * 70}╗")
        print(f"║ {'JOGO CADASTRADO - ' + self.nome.upper():^68} ║")
        print(f"╠{'═' * 70}╣")
        print(f"║ {'INFORMAÇÕES BÁSICAS:':<68} ║")
        print(f"║ {'• ID:':<15} {self.identificacao:<52} ║")
        print(f"║ {'• Nome:':<15} {self.nome:<52} ║")
        print(f"║ {'• Empresa:':<15} {self.empresa:<52} ║")
        print(f"║ {'• Gênero:':<15} {self.genero:<52} ║")
        print(f"╠{'─' * 70}╣")
        print(f"║ {'DETALHES TÉCNICOS:':<68} ║")
        print(f"║ {'• Lançamento:':<15} {self.lancamento:<52} ║")
        print(f"║ {'• Data no Estoque:':<15} {self.data_adicao:<52} ║")
        print(f"║ {'• Classificação:':<15} {classificacao_str:<52} ║")
        print(f"║ {'• Plataformas:':<15} {self.plataformas:<52} ║")
        print(f"╠{'─' * 70}╣")
        print(f"║ {'INFORMAÇÕES COMERCIAIS:':<68} ║")
        print(f"║ {'• Preço:':<15} {preco_formatado:<52} ║")
        print(f"║ {'• Quantidade:':<15} {self.quantidade} cópias{' ' * 42} ║")
        print(f"║ {'• Avaliação:':<15} {estrelas} ({self.avaliacao}/5){' ' * 35} ║")
        print(f"╠{'─' * 70}╣")
        print(f"║ {'DESCRIÇÃO:':<68} ║")
        # Quebrar a descrição em linhas de no máximo 65 caracteres
        descricao_quebrada = []
        palavras = self.descricao.split()
        linha_atual = ""
        for palavra in palavras:
            if len(linha_atual + " " + palavra) <= 65:
                linha_atual += " " + palavra if linha_atual else palavra
            else:
                descricao_quebrada.append(linha_atual)
                linha_atual = palavra
        if linha_atual:
            descricao_quebrada.append(linha_atual)
        
        for linha in descricao_quebrada:
            print(f"║ {linha:<68} ║")
        print(f"╠{'─' * 70}╣")
        print(f"║ {'REQUISITOS MÍNIMOS:':<68} ║")
        # Quebrar os requisitos também
        requisitos_quebrados = []
        palavras_req = self.requisitos.split()
        linha_req = ""
        for palavra in palavras_req:
            if len(linha_req + " " + palavra) <= 65:
                linha_req += " " + palavra if linha_req else palavra
            else:
                requisitos_quebrados.append(linha_req)
                linha_req = palavra
        if linha_req:
            requisitos_quebrados.append(linha_req)
            
        for linha in requisitos_quebrados:
            print(f"║ {linha:<68} ║")
        print(f"╚{'═' * 70}╝")

# --- Função para verificar se uma data é válida ---
def verificar_data(data_str, tipo_data="data"):
    try:
        # Divide a string da data
        dia, mes, ano = map(int, data_str.split('/'))
        
        # Verifica se o ano está no intervalo permitido
        if ano < 1980 or ano > 2025:
            print(f"ERRO: O ano deve estar entre 1980 e 2025. Ano informado: {ano}")
            return None
        
        # Tenta criar um objeto date para validar a data
        data_obj = datetime.date(ano, mes, dia)
        
        # Verifica se a data não é futura (para data de adição ao estoque)
        if tipo_data == "data_adicao" and data_obj > datetime.date.today():
            print("ERRO: A data de adição ao estoque não pode ser uma data futura.")
            return None
            
        return data_str
    except ValueError:
        print(f"ERRO: Data '{data_str}' inválida. Use o formato dd/mm/aaaa e certifique-se de que é uma data real.")
        return None

# --- Lista (vetor) para armazenar esses jogos cadastrados no estoque ---
# Por que lista? Porque ela permite ser mudada e também admite duplicatas.

jogos_no_estoque = [
     Produto(
        codigo_ID="FS001",
        nome_jogo="Dark Souls: Remastered",
        empresa_jogo="FromSoftware",
        genero_jogo="RPG",
        lancamento_jogo=2018,
        data_addEstoque="28/11/2025",
        preco_jogo=154.90,
        avaliacao_jogo=5,
        descricao_jogo="Mas então, fez-se o jogo. Experimente novamente o jogo aclamado pela crítica! Belamente remasterizado, volte a Lordran com detalhes em alta definição!",
        classificacao_jogo=14,
        quantidade_jogo=10,
        requisitos_jogo="Intel Core i5, 6GB RAM, NVIDIA GTX 660, 8GB",
        plataformas_jogo="PC, PlayStation, Xbox"
    ),
    Produto(
        codigo_ID="FS002",
        nome_jogo="Dark Souls II",
        empresa_jogo="FromSoftware",
        genero_jogo="RPG",
        lancamento_jogo=2014,
        data_addEstoque="28/11/2025",
        preco_jogo=154.90,
        avaliacao_jogo=4,
        descricao_jogo="Dark Souls II é a tão esperada sequência do sucesso avassalador Dark Souls.",
        classificacao_jogo=14,
        quantidade_jogo=10,
        requisitos_jogo="AMD Phenom II X2, 8GB RAM, NVIDIA GeForce 9600GT, 12GB",
        plataformas_jogo="PC, PlayStation, Xbox"
    ),
    Produto(
        codigo_ID="FS003",
        nome_jogo="Dark Souls III",
        empresa_jogo="FromSoftware",
        genero_jogo="RPG",
        lancamento_jogo=2016,
        data_addEstoque="28/11/2025",
        preco_jogo=229.90,
        avaliacao_jogo=5,
        descricao_jogo="Dark Souls continua a ultrapassar seus próprios limites em um ambicioso novo capítulo da série!",
        classificacao_jogo=14,
        quantidade_jogo=10,
        requisitos_jogo="Intel Core i5, 8GB RAM, NVIDIA GTX750 TI, 25GB",
        plataformas_jogo="PC, PlayStation, Xbox"
    ),
    Produto(
        codigo_ID="ND001",
        nome_jogo="The Last of Us Part I",
        empresa_jogo="Naughty Dog LLC",
        genero_jogo="Survival",
        lancamento_jogo=2023,
        data_addEstoque="28/11/2025",
        preco_jogo=249.90,
        avaliacao_jogo=5,
        descricao_jogo="Descubra o jogo premiado que inspirou a série de TV aclamada pela crítica.",
        classificacao_jogo=18,
        quantidade_jogo=10,
        requisitos_jogo="Intel Core i7, 16GB RAM, AMD Radeon RX 470, 100GB",
        plataformas_jogo="PC, PlayStation, Xbox"
    ),
    Produto(
        codigo_ID="ND002",
        nome_jogo="The Last of Us Part II Remastered",
        empresa_jogo="Naughty Dog LLC",
        genero_jogo="Survival",
        lancamento_jogo=2025,
        data_addEstoque="28/11/2025",
        preco_jogo=199.90,
        avaliacao_jogo=5,
        descricao_jogo="Experimente o vencedor de mais de 300 prêmios de Jogo do Ano, agora no PC.",
        classificacao_jogo=18,
        quantidade_jogo=10,
        requisitos_jogo="Intel Core i3, 16GB RAM, NVIDIA GeForce GTX 1650, 150GB",
        plataformas_jogo="PC, PlayStation"
    )
]
    
# --- Interação com o Usuário ---
print("ESTOQUE DE JOGOS")
print("Você está prestes a cadastrar um jogo no ESTOQUE.")
print("Siga o passo a passo corretamente:")
print("1. Código de identificação do jogo.")
print("2. Nome do jogo.")
print("3. Nome da empresa do jogo.")
print("4. Gênero do jogo.")
print("5. Ano de lançamento do jogo.")
print("6. Data de adição do jogo ao estoque.")
print("7. Preço do jogo. ")
print("8. Avaliação do jogo - 1 a 5 estrelas.")
print("9. Descrição breve do jogo.")
print("10. Classificação indicativa do jogo.")
print("11. Quantidade de cópias disponíveis no estoque.")
print("12. Requisitos mínimos para rodar o jogo.")
print("13. Plataforams que rodam o jogo.")
print("\n")
print("--- AVISOS ---")
print("1. Utilize o formato dd/mm/aaaa para datas!")
print("2. Siga a sequência correta de requisitos: 1.CPU, 2.RAM, 3.GPU, 4.Armazenamento.")
print("3. Classificações indicativas do Brasil: 0 anos (livre), 10 anos, 12 anos, 14 anos, 16 anos e 18 anos.")
print("4. Digite SAIR no campo de CÓDIGO DE IDENTIFICAÇÃO para interromper o cadastro de um novo jogo.")
print("\n")

# --- Contador de Jogos ---
# Assim o cadastro fica mais organizado e o usuário sabe quantos jogos está cadastrando.

contador_jogos = 1

# --- Solicita os dados do usuário ---
while True:
    print(f"\n--- Cadastrando Jogo {contador_jogos:02d} ---")
    ID_do_jogo = input(f"Informe o código de identificação do jogo {contador_jogos:02d}: ")
    # Verificação: O usuário quer cadastrar mais um jogo ou não?
    
    if ID_do_jogo.lower() == 'sair':  # lower() vai ajudar a ler todas as variações.Ex.: sair, Sair, SAIR, SaIr...
        break

    nome_do_jogo = input(f"Informe o nome do jogo {contador_jogos:02d}: ")
    empresa_do_jogo = input(f"Informe o nome da empresa do jogo {contador_jogos:02d}: ")
    
    # --- Verifica se o jogo está dentro dos gêneros suportados pela plataforma ---
    
    genero_do_jogo = input(f"Informe o gênero do jogo {contador_jogos:02d} (MOBA, FPS, RPG...): ")
    
    # Validação do ano de lançamento do jogo
    while True:
        try:
            lancamento_do_jogo = input(f"Insira o ano de lançamento do jogo {contador_jogos:02d}: ")
            if lancamento_do_jogo > 1980:
                break
            else: 
                print("Ano inválido! Só possuímos jogos produzidos a partir de 1980.")
        except ValueError:
            print("Ano inválido, pois é mais antigo que 1980!")
       
    # Validação da data de adição ao estoque
    while True:
        adicao_do_jogo = input(f"Insira a data de adição do jogo {contador_jogos:02d} ao estoque: ")
        adicao_validada = verificar_data(adicao_do_jogo, "data_adicao")
        if adicao_validada:
            break
        else:
            print("Por favor, insira uma data de adição válida.")
    
    # Validação do preço do jogo
    while True:
        try:
            preco_do_jogo = float(input(f"Informe o preço do jogo {contador_jogos:02d} :"))
            if preco_do_jogo > 0:
                break
            else:
                print("Preço inválido! Por favor, digite um valor maior que 0.")
        except ValueError:
            print("Preço inválido! Por favor, digite um valor maior que 0.")     
        
    # Validação da avaliação (1-5)
    while True:
        try:
            print("--- AVALIAÇÃO POR ESTRELAS ---")
            print("1 Estrela - Muito Ruim")
            print("2 Estrelas - Ruim")
            print("3 Estrelas - Razoável")
            print("4 Estrelas - Bom")
            print("5 Estrelas - Muito Bom")
            avaliacao_do_jogo = int(input(f"Insira uma avaliação para o jogo {contador_jogos:02d}: "))
            if 1 <= avaliacao_do_jogo <= 5:
                break
            else:
                print("ERRO: A avaliação deve ser entre 1 e 5.")
        except ValueError:
            print("ERRO: Digite um número inteiro entre 1 e 5.")
    
    descricao_do_jogo = input(f"Escreva uma breve descrição sobre o jogo {contador_jogos:02d}:")
    
    # Validação da Classificação Indicativa 
    while True:
        try:
            classificacao_do_jogo = int(input(f"Informe a classificação indicativa do jogo {contador_jogos:02d}:"))
            if classificacao_do_jogo == 0 or classificacao_do_jogo == 10 or classificacao_do_jogo == 12 or classificacao_do_jogo == 14 or classificacao_do_jogo == 16 or classificacao_do_jogo == 18:
                break
            else:
                print("Classificação indicativa inválida! As classificações indicativas possíveis no Brasil são: 0(Livre), 10, 12, 14, 16 e 18 anos.")
        except ValueError:
            print("Classificação indicativa inválida no Brasil! Tente: 0, 10, 12, 14, 16 ou 18 anos.")
            
    # Validação da quantiadade de cópias do jogo no estoque:
    while True:
        try:
            quantidade_do_jogo = int(input(f"Informe quantas cópias do jogo {contador_jogos:02d} estão disponíveis no Estoque: "))
            if quantidade_do_jogo > 0:
                break
            else:
                print("Quantidade de cópias inválida! Insira um valor maior que 0.")
        except ValueError:
            print("Insira um valor maior que zero (0)!")
            
    requisitos_do_jogo = input(f"Informe os requisitos mínimos do jogo {contador_jogos:02d} nessa ordem: 1.PROCESSADOR 2.MEMÓRIA RAM  3.PLACA DE VÍDEO  4.ARMAZENAMENTO: ")
    plataformas_do_jogo = input(f"Informe quais plataformas rodam o jogo {contador_jogos:02d} (Xbox, PC, PlayStation...): ")
    print("\n")
    
    
    # --- Instancia a classe "Produto" com os dados recebidos ---
    novo_jogo = Produto(ID_do_jogo, nome_do_jogo, empresa_do_jogo, genero_do_jogo, lancamento_do_jogo, adicao_validada, preco_do_jogo, avaliacao_do_jogo, descricao_do_jogo, classificacao_do_jogo, quantidade_do_jogo, requisitos_do_jogo, plataformas_do_jogo)
    # Adiciona objetos à lista (append)
    jogos_no_estoque.append(novo_jogo)
    print(f"Jogo {contador_jogos:02d} '{nome_do_jogo}' cadastrado com sucesso!\n")

    # Incrementa o nosso contador
    contador_jogos += 1

# --- Apresentação dos Dados ---
print(f"\n╔{'═' * 70}╗")
print(f"║ {'ESTOQUE DE JOGOS - RELATÓRIO FINAL':^68} ║")
print(f"╠{'═' * 70}╣")
print(f"║ {f'TOTAL DE JOGOS CADASTRADOS: {len(jogos_no_estoque)}':^68} ║")
print(f"╚{'═' * 70}╝")
print("\n")

for i, produto in enumerate(jogos_no_estoque, 1):
    print(f"\n{'=' * 72}")
    print(f"JOGO {i:02d} DE {len(jogos_no_estoque)}")
    print(f"{'=' * 72}")
    produto.exibir_formatado()
    print("\n" + " " * 20 + "─" * 32 + "\n")  # Separador entre jogos

# Resumo final
if jogos_no_estoque:
    total_copias = sum(produto.quantidade for produto in jogos_no_estoque)
    valor_total_estoque = sum(produto.preco * produto.quantidade for produto in jogos_no_estoque)
    
    print(f"\n╔{'═' * 70}╗")
    print(f"║ {'RESUMO DO ESTOQUE':^68} ║")
    print(f"╠{'═' * 70}╣")
    print(f"║ {'• Total de jogos diferentes:':<35} {len(jogos_no_estoque):>32} ║")
    print(f"║ {'• Total de cópias em estoque:':<35} {total_copias:>32} ║")
    print(f"║ {'• Valor total do estoque:':<35} R$ {valor_total_estoque:>28.2f} ║")
    print(f"╚{'═' * 70}╝")
