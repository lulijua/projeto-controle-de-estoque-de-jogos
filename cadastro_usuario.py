# Código responsável pela parte do perfil do usuário.

# Lista para armazenar todos os clientes cadastrados
clientes_cadastrados = []

# Contador de clientes
contador_clientes = 1

# Instruções para o usuário
print("\n=====INSTRUÇÕES PARA CADASTRO=====\n")
print("1- Digite o nome completo do cliente.")
print("2- Digite o nome de usuário do cliente.")
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
        "Nome de usuario": None,
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

    # Nome de usuário
    perfil_cliente["Nome de usuario"] = input(f"Digite o nome de usuario do cliente {contador_clientes}: ")

    # Email e verificação
    perfil_cliente["Email"] = input(f"Digite o email do cliente {contador_clientes}: ")

    while "@gmail" not in perfil_cliente["Email"].lower() or perfil_cliente["Email"].startswith("@"):
        perfil_cliente["Email"] = input("Email inválido! Tente novamente: ")

    # Telefone
    perfil_cliente["Numero"] = input(f"Digite o número de telefone do cliente {contador_clientes}: ")

    while True:
        if len(perfil_cliente["Numero"]) == 12 and perfil_cliente["Numero"][2] == " ":
            break
        else:
            perfil_cliente["Numero"] = input("Número inválido! Tente novamente: ")

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
    perfil_cliente["jogo_genero"]["Genero2"] = input("Genero 2: ")
    perfil_cliente["jogo_genero"]["Genero3"] = input("Genero 3: ")  # Corrigido: estava "Genero 2"

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
    print(f"║ {'USUÁRIO:':<20} {cliente['Nome de usuario']:<28} ║")
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
    print(f"│ USUÁRIO: {cliente['Nome de usuario']}")
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

print("teste :P")