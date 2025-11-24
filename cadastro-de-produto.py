# Esse código é responsável pelo cadastro dos produtos.
# Feito com classes do Python

# Cria uma classe 'Produto', no caso são os jogos, ela possui todas as informações que um jogo teria.
class Produto:
    def __init__(self, codigo_ID, nome_jogo, empresa_jogo, genero_jogo, lancamento_jogo, data_addEstoque):
        self.identificacao = codigo_ID
        self.nome = nome_jogo
        self.empresa = empresa_jogo
        self.genero = genero_jogo
        self.lancamento = lancamento_jogo
        self.data_adicao = data_addEstoque
        
    def __str__(self):
        return f"ID DO JOGO: {self.identificacao}\nNOME DO JOGO: {self.nome}\nEMPRESA DO JOGO: {self.empresa}\nGÊNERO DO JOGO: {self.genero}\nANO DE LANÇAMENTO: {self.lancamento}\nDATA DE ADIÇÃO AO ESTOQUE: {self.data_adicao}\n\n"
        
# --- Lista (vetor) para armazenar esses jogos cadastrados no estoque ---
# Por que lista? Porque ela permite ser mudada e também admite duplicatas.

jogos_no_estoque = []
    
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
print("\n")
print("Utilize o formato dd/mm/aaaa para datas!")
print("\n")
print("Digite SAIR no campo de CÓDIGO DE IDENTIFICAÇÃO para interromper o cadastro de um novo jogo.")
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
    empresa_do_jogo = input(f"Insira o nome da empresa do jogo {contador_jogos:02d}: ")
    genero_do_jogo = input(f"Insira o gênero do jogo {contador_jogos:02d}: ")
    lancamento_do_jogo = input(f"Insira o ano de lançamento do jogo {contador_jogos:02d}: ")
    adicao_do_jogo = input(f"Insira a data de adição do jogo {contador_jogos:02d} ao estoque: ")
    print("\n")
    
    # --- Instancia a classe "Produto" com os dados recebidos ---
    novo_jogo = Produto(ID_do_jogo, nome_do_jogo, empresa_do_jogo, genero_do_jogo, lancamento_do_jogo, adicao_do_jogo)

    # Adiciona objetos à lista (append)
    jogos_no_estoque.append(novo_jogo)
    print(f"Jogo {contador_jogos:02d} '{nome_do_jogo}' cadastrado com sucesso!\n")

    # Incrementa o nosso contador
    contador_jogos += 1

# --- Apresentação dos Dados ---
print(f"\n--- {len(jogos_no_estoque)} JOGOS FORAM CADASTRADOS COM SUCESSO!!! ---")
print("\n")

for produto in jogos_no_estoque:
    print(produto)