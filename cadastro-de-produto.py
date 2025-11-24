#Esse código é responsável pelo cadastro dos produtos.
#Feito com classes do Python

class Produto:
    def __init__(self,codigo_ID,nome_jogo,empresa_jogo,genero_jogo,lancamento_jogo, data_addEstoque):
        self.identificacao = codigo_ID
        self.nome = nome_jogo
        self.empresa = empresa_jogo
        self.genero = genero_jogo
        self.lancamento = lancamento_jogo
        self.data_adicao = data_addEstoque
        
    def cadastro(self):
        #Como esse cadastro será mostrado
        print(f"ID DO JOGO:\n{self.identificacao}\n")
        print(f"NOME DO JOGO:\n{self.nome}\n")
        print(f"EMPRESA DO JOGO:\n{self.empresa}\n")
        print(f"GÊNERO DO JOGO:\n{self.genero}\n")
        print(f"DATA DE LANÇAMENTO DO JOGO:\n{self.lancamento}\n")
        print(f"DATA DE ADIÇÃO AO ESTOQUE:\nB{self.data_adicao}\n")
        pass
    
# --- Interação com o Usuário ---
print("ESTOQUE DE JOGOS")
print("Você está prestes a cadastrar um jogo no ESTOQUE.")
print("Siga o passo a passo corretamente:")
print("1. Código de identificação do jogo.")
print("2. Nome do jogo.")
print("3. Nome da empresa do jogo.")
print("4. Gênero do jogo.")
print("5. Data de lançamento do jogo.")
print("6. Data de adição do jogo ao estoque.")
print("\n")

# --- Solicita os dados ---

ID_do_jogo = input("Informe o código de identificação do jogo:")
nome_do_jogo = input("Informe o nome do jogo:")
empresa_do_jogo = input("Insira o nome da empresa do jogo:")
genero_do_jogo = input("Insira o gênero do jogo:")
lancamento_do_jogo = input("Insira a data de lançamento do jogo:")
adicao_do_jogo = input("Insira a data de adição desse jogo ao estoque no formato (dd/mm/aaaa):")

# --- Instancia a classe "Produto" com os dados recebidos

jogo1 = Produto(ID_do_jogo, nome_do_jogo, empresa_do_jogo, genero_do_jogo,lancamento_do_jogo,adicao_do_jogo)

# --- Apresentação dos Dados ---
print("\nJOGO CADASTRADO COM SUCESSO!!!")
print("\n")
jogo1.cadastro()