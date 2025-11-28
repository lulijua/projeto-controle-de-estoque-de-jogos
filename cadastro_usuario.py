# Código responsavel pela parte do perfil do usuário.


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

    #Dicionário para guardar as infos do cliente
    perfil_cliente = {

        "Nome": None,
        "Nome de usuario": None,
        "Email": None,
        "Numero": None,
        "Idade": None,
       
    "jogo_genero" : {
           "Genero1": None,
           "Genero2": None,
           "Genero3": None,
       }

    }

    print(f"\n====CADASTRO DO CLIENTE {contador_clientes}====\n")


    # Nome do cliente

    perfil_cliente["Nome"] = input(f"Digite o nome do cliente {contador_clientes}: ")

    remover_espacos = perfil_cliente["Nome"].replace(" ", "")
    if remover_espacos.isalpha() == True:
        break
    else:
        while remover_espacos.isalpha() == False:
            perfil_cliente["Nome"] = input("Nome inválido! Digite novamente: ")
            remover_espacos = perfil_cliente["Nome"].replace(" ", "")



    # Encerrar cadastro

    if perfil_cliente["Nome"].lower() == 'sair':
        break


    perfil_cliente["Nome de usuario"] = input(f"Digite o nome de usuario do cliente {contador_clientes}: ")


    #Email e verificação

    perfil_cliente["Email"] = input(f"Digite o email do cliente {contador_clientes}: ")

    while "@gmail" not in perfil_cliente["Email"].lower() or perfil_cliente["Email"].startswith("@"): #usamos .lower para a string ficar em minusculo e realizar a verificacao do "@gmail"
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

        if idade_str.isdigit(): #verificar se a string atribuida a idade é realmente um numero
            idade = int(idade_str)

            if 0 < idade < 120:
                perfil_cliente["Idade"] = idade
                break
            else:
                perfil_cliente["Idade"] = input("Idade inválida! Digite novamente: ")
        else:
            perfil_cliente["Idade"] = input("Valor inválido! Digite um número para idade: ")
    

    # Genero de jogo
    #Analisar as opcoes de genero depois

    print(f"Preferências de gênero do cliente {contador_clientes}:")
    perfil_cliente["jogo_genero"]["Genero1"] = input("Genero 1: ")
    perfil_cliente["jogo_genero"]["Genero2"] = input("Genero 2: ")
    perfil_cliente["jogo_genero"]["Genero3"] = input("Genero 2: ")


    # Salvar cliente
    clientes_cadastrados.append(perfil_cliente)
    contador_clientes += 1

# Apresentação dos dados
print(f"\n====={contador_clientes - 1} CLIENTES ESTÃO REGISTRADOS=====\n")

for cliente in clientes_cadastrados:
    print(cliente)

    #testando
