# Código responsável pela parte do perfil do usuário.

#---Funções---
#Funções para identificar se o estilo de jogo escolhido pelo usuário é possível.
def genero_jogo1 (Genero1):

    if Genero1.lower() in ['rpg', 'fps', 'survival', 'puzzle', 'chill', 'gacha', 'esportes', 'moba', 'terror', 'coop']:
        return 0
    else:
        print(f"Genero de jogo indisponível. Tente novamente. ")
        return 1

def genero_jogo2 (Genero2):

    if Genero2.lower() in ['rpg', 'fps', 'survival', 'puzzle', 'chill', 'gacha', 'esportes', 'moba', 'terror', 'coop']:
        return 0
    else:
        print(f"Genero de jogo indisponível. Tente novamente.")
        return 1

def genero_jogo3 (Genero3):

    if Genero3.lower() in ['rpg', 'fps', 'survival', 'puzzle', 'chill', 'gacha', 'esportes', 'moba', 'terror', 'coop']:
        return 0
    else:
        print(f"Genero de jogo indisponível. Tente novamente.")
        return 1
    
#funções para verificar os nomes de usuario, email e numero de telefone, caso haja algum em comum com outro usuario

def verificar_usuario(Usuario):

    if len(clientes_cadastrados) >0:
        for i in range(0, len(clientes_cadastrados)):
            if Usuario.lower() == clientes_cadastrados[i]["Usuario"]:
                print("O nome de usuário já está em uso. Tente novamente.")
                return 1
    return 0

def verificar_email(Email):
    
    if len(clientes_cadastrados) > 0:
        for i in range (0, len(clientes_cadastrados)):
            if Email.lower() == clientes_cadastrados[i]["Email"]:
                print("O Email já está em uso. Tente novamente.")
                return 1
    return 0

def verificar_numero(Numero):

    if len(clientes_cadastrados) > 0:
        for i in range (0, len(clientes_cadastrados)):
            if Numero.lower() == clientes_cadastrados[i]["Numero"]:
                print("O número de telefone já está em uso. Tente novamente.")
                return 1
    return 0

# Lista para armazenar todos os clientes cadastrados
clientes_cadastrados = []

# Contador de clientes
contador_clientes = 1

# Instruções para o usuário
print("\n=====INSTRUÇÕES PARA CADASTRO=====\n")
print("1- Digite o nome completo do cliente.")
print("2- Digite o  usuário do cliente.")
print("3- Digite o email do cliente.")
print("4- Digite o numero de telefone do cliente.")
print("5- Digite a idade do cliente.")
print("\n")
print("====ATENÇÃO====")
print("O email deve conter '@gmail' para ser válido.")
print("O número de telefone deve ser escrito da seguinte forma: 99 999999999.")
print("Para encerrar o cadastro, digite SAIR no campo do NOME do cliente.")
print("\n")

# Preencher os dados dos clientes
while True:

    # Dicionário para guardar as infos do cliente
    perfil_cliente = {
        "Nome": None,
        "Usuario": None,
        "Email": None,
        "Numero": None,
        "Idade": None,
        "jogo_genero": {
            "Genero1": None,
            "Genero2": None,
            "Genero3": None,
        }
    }

    print(f"\n====CADASTRO DO CLIENTE {contador_clientes}====\n")

    # Nome do cliente
    perfil_cliente["Nome"] = input(f"Digite o nome do cliente {contador_clientes}: ")

    # Encerrar cadastro
    if perfil_cliente["Nome"].lower() == 'sair':
        break

    # Validação do nome
    remover_espacos = perfil_cliente["Nome"].replace(" ", "")
    if remover_espacos.isalpha() == False:
        while remover_espacos.isalpha() == False:
            perfil_cliente["Nome"] = input("Nome inválido! Digite novamente: ")
            remover_espacos = perfil_cliente["Nome"].replace(" ", "")
            # Verificar se o usuário quer sair após correção
            if perfil_cliente["Nome"].lower() == 'sair':
                break
        
        if perfil_cliente["Nome"].lower() == 'sair':
            break

    #  usuário e função para verificar o usuario
    perfil_cliente["Usuario"] = input(f"Digite o nome de usuario do cliente {contador_clientes}: ")

    while verificar_usuario(perfil_cliente["Usuario"]) != 0:
        perfil_cliente["Usuario"] = input(f"Digite o nome de usuario do cliente {contador_clientes}: ")

    # Email e verificação
    perfil_cliente["Email"] = input(f"Digite o email do cliente {contador_clientes}: ")
    
    while verificar_email(perfil_cliente["Email"]) != 0 or "@gmail" not in perfil_cliente["Email"].lower() or perfil_cliente["Email"].startswith("@"):
        print("Email inválido ou já cadastrado. Tente novamente.")

        perfil_cliente["Email"] = input(f"Digite o email do cliente {contador_clientes}: ")

    # Telefone
    perfil_cliente["Numero"] = input(f"Digite o número de telefone do cliente {contador_clientes}: ")

    while verificar_numero(perfil_cliente["Numero"]) != 0 or len(perfil_cliente["Numero"]) != 12 or perfil_cliente["Numero"][2] != " ":
            print("Número inválido ou já cadastrado! Tente novamente.")

            perfil_cliente["Numero"] = input(f"Digite o número de telefone do cliente {contador_clientes}: ")

    # Idade
    perfil_cliente["Idade"] = input(f"Digite a idade do cliente {contador_clientes}: ")

    while True:
        idade_str = perfil_cliente["Idade"]

        if idade_str.isdigit():  # verificar se a string atribuída à idade é realmente um número
            idade = int(idade_str)

            if 0 < idade < 120:
                perfil_cliente["Idade"] = idade
                break
            else:
                perfil_cliente["Idade"] = input("Idade inválida! Digite novamente: ")
        else:
            perfil_cliente["Idade"] = input("Valor inválido! Digite um número para idade: ")

    # Gênero de jogo
    print(f"Preferências de gênero do cliente {contador_clientes}:")

    perfil_cliente["jogo_genero"]["Genero1"] = input("Genero 1: ")

    while genero_jogo1(perfil_cliente["jogo_genero"]["Genero1"]) != 0:
        perfil_cliente["jogo_genero"]["Genero1"] = input("Genero 1: ")

    perfil_cliente["jogo_genero"]["Genero2"] = input("Genero 2: ")

    while genero_jogo2(perfil_cliente["jogo_genero"]["Genero2"]) != 0:
        perfil_cliente["jogo_genero"]["Genero2"] = input("Genero 2: ")

    perfil_cliente["jogo_genero"]["Genero3"] = input("Genero 3: ")

    while genero_jogo3(perfil_cliente["jogo_genero"]["Genero3"]) != 0:
        perfil_cliente["jogo_genero"]["Genero3"] = input("Genero 3: ")

    # Salvar cliente
    clientes_cadastrados.append(perfil_cliente)
    contador_clientes += 1             


# Apresentação dos dados - FORMA MELHORADA
print(f"\n====={contador_clientes - 1} CLIENTES ESTÃO REGISTRADOS=====\n")

for i, cliente in enumerate(clientes_cadastrados, 1):
    print(f"╔{'═' * 50}╗")
    print(f"║ {'CLIENTE ' + str(i):^48} ║")
    print(f"╠{'═' * 50}╣")
    print(f"║ {'NOME:':<20} {cliente['Nome']:<28} ║")
    print(f"║ {'USUÁRIO:':<20} {cliente['Usuario']:<28} ║")
    print(f"║ {'EMAIL:':<20} {cliente['Email']:<28} ║")
    print(f"║ {'TELEFONE:':<20} {cliente['Numero']:<28} ║")
    print(f"║ {'IDADE:':<20} {cliente['Idade']:<28} ║")
    print(f"╠{'─' * 50}╣")
    print(f"║ {'PREFERÊNCIAS DE GÊNERO:':<48} ║")
    print(f"║ {'• Gênero 1:':<20} {cliente['jogo_genero']['Genero1']:<28} ║")
    print(f"║ {'• Gênero 2:':<20} {cliente['jogo_genero']['Genero2']:<28} ║")
    print(f"║ {'• Gênero 3:':<20} {cliente['jogo_genero']['Genero3']:<28} ║")
    print(f"╚{'═' * 50}╝")
    print()  # Linha em branco entre clientes

# Alternativa mais simples (se preferir)
"""
print(f"\n====={contador_clientes - 1} CLIENTES ESTÃO REGISTRADOS=====\n")

for i, cliente in enumerate(clientes_cadastrados, 1):
    print(f"┌────────────────── CLIENTE {i} ──────────────────")
    print(f"│ NOME: {cliente['Nome']}")
    print(f"│ USUÁRIO: {cliente['Usuario']}")
    print(f"│ EMAIL: {cliente['Email']}")
    print(f"│ TELEFONE: {cliente['Numero']}")
    print(f"│ IDADE: {cliente['Idade']}")
    print(f"│ PREFERÊNCIAS DE GÊNERO:")
    print(f"│   • Gênero 1: {cliente['jogo_genero']['Genero1']}")
    print(f"│   • Gênero 2: {cliente['jogo_genero']['Genero2']}")
    print(f"│   • Gênero 3: {cliente['jogo_genero']['Genero3']}")
    print(f"└────────────────────────────────────────────────")
    print()
"""