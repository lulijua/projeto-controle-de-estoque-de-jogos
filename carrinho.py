import random
from cadastro_de_produto import produto, jogos_no_estoque
from cadastro_usuario import clientes_cadastrados
from cadastro_usuario import perfil_cliente

def aplicar_cupom(valor, cupom_usado):
    if cupom_usado:
        return valor, cupom_usado

    chance = random.random()

    if chance <= 0.3:
        desconto = valor * 0.10
        valor -= desconto
        print(f"╔════════════════════════════════════════╗")
        print(f"║  CUPOM DE 10% APLICADO!               ║")
        print(f"║  Desconto: R${desconto:>26.2f} ║")
        print(f"╚════════════════════════════════════════╝")
        cupom_usado = True

    return valor, cupom_usado

def adicionar_carrinho(jogo_nome):
    jogo_encontrado = None

    for jogo in jogos_no_estoque:
        if jogo.nome.lower().strip() == jogo_nome.lower().strip():
            jogo_encontrado = jogo
            break

    if jogo_encontrado is None:
        print(f"╔{'═'*40}╗")
        print(f"║{'PRODUTO NÃO ENCONTRADO!':^40}║")
        print(f"╚{'═'*40}╝")
        return 0
    
    if jogo_encontrado.quantidade <= 0:
        print(f"╔{'═'*40}╗")
        print(f"║{'ESTOQUE ESGOTADO!':^40}║")
        print(f"╚{'═'*40}╝")
        return 0
    
    carrinho.append(jogo_encontrado)
    jogo_encontrado.quantidade -= 1

    print(f"╔{'═'*60}╗")
    print(f"║{'PRODUTO ADICIONADO':^60}║")
    print(f"╠{'═'*60}╣")
    print(f"║ {jogo_encontrado.nome:<40} R${jogo_encontrado.preco:>15.2f} ║")
    print(f"╚{'═'*60}╝")
    return jogo_encontrado.preco

def remover_carrinho(jogo_nome):
    for jogo in carrinho:
        if jogo.nome.lower().strip() == jogo_nome.lower().strip():
            carrinho.remove(jogo)
            jogo.quantidade += 1
            print(f"╔{'═'*60}╗")
            print(f"║{'PRODUTO REMOVIDO':^60}║")
            print(f"╠{'═'*60}╣")
            print(f"║ {jogo.nome:<40} R${jogo.preco:>15.2f} ║")
            print(f"╚{'═'*60}╝")
            return jogo.preco
    
    print(f"╔{'═'*40}╗")
    print(f"║{'ITEM NÃO ESTÁ NO CARRINHO':^40}║")
    print(f"╚{'═'*40}╝")
    return 0

def mostrar_carrinho():
    if len(carrinho) == 0:
        print(f"╔{'═'*40}╗")
        print(f"║{'CARRINHO VAZIO':^40}║")
        print(f"╚{'═'*40}╝")
        return
    
    print(f"╔{'═'*60}╗")
    print(f"║{'SEU CARRINHO':^60}║")
    print(f"╠{'═'*60}╣")
    for i, item in enumerate(carrinho, 1):
        print(f"║ {i:>2}. {item.nome:<40} R${item.preco:>15.2f} ║")
    print(f"╠{'═'*60}╣")
    total = sum(item.preco for item in carrinho)
    print(f"║ {'TOTAL:':<44} R${total:>15.2f} ║")
    print(f"╚{'═'*60}╝")

carrinho = []
vendas_no_dia = []
total_arrecadado = 0.0
total_itens_vendidos = 0

print(f"\n╔{'═'*40}╗")
print(f"║{'CARRINHO DE COMPRAS':^40}║")
print(f"╚{'═'*40}╝")

for cliente_idx, cliente in enumerate(clientes_cadastrados):
    # Supondo que o cliente é um dicionário com chave 'Nome'
    nome_cliente = cliente.get('Nome', f'Cliente {cliente_idx+1}')
    
    print(f"\n╔{'═'*40}╗")
    print(f"║{'COMPRAS DO CLIENTE':^40}║")
    print(f"╠{'═'*40}╣")
    print(f"║ {nome_cliente:^38} ║")
    print(f"╚{'═'*40}╝")
    
    carrinho.clear()
    total_cliente = 0.0
    cupom_usado = False
    
    while True:
        print(f"\n╔{'═'*40}╗")
        print(f"║{'MENU PRINCIPAL':^40}║")
        print(f"╠{'═'*40}╣")
        print(f"║{'1- Adicionar itens ao carrinho':<40}║")
        print(f"║{'2- Remover itens do carrinho':<40}║")
        print(f"║{'3- Ver carrinho':<40}║")
        print(f"║{'4- Finalizar compra':<40}║")
        print(f"╚{'═'*40}╝")
        print(f"Usuário: {perfil_cliente['Nome']}")
        
        try:
            escolha_carrinho = int(input("\nEscolha: "))
            
            if escolha_carrinho < 1 or escolha_carrinho > 4:
                print(f"╔{'═'*40}╗")
                print(f"║{'ESCOLHA INVÁLIDA!':^40}║")
                print(f"╚{'═'*40}╝")
                continue
        except ValueError:
            print(f"╔{'═'*40}╗")
            print(f"║{'DIGITE UM NÚMERO VÁLIDO':^40}║")
            print(f"╚{'═'*40}╝")
            continue
        
        if escolha_carrinho == 1:
            escolha_jogo = input("Qual jogo deseja comprar? ")
            valor = adicionar_carrinho(escolha_jogo)
            
            if valor > 0:
                total_cliente += valor
        
        elif escolha_carrinho == 2:
            if len(carrinho) == 0:
                mostrar_carrinho()
            else:
                mostrar_carrinho()
                escolha_jogo = input("\nQual jogo deseja retirar? ")
                valor_removido = remover_carrinho(escolha_jogo)
                total_cliente -= valor_removido
        
        elif escolha_carrinho == 3:
            mostrar_carrinho()
        
        elif escolha_carrinho == 4:
            print(f"\n╔{'═'*50}╗")
            print(f"║{'FINALIZANDO COMPRA':^50}║")
            print(f"╚{'═'*50}╝")
            
            if len(carrinho) > 0:
                valor_final, cupom_usado = aplicar_cupom(total_cliente, cupom_usado)
                total_cliente = valor_final
            
            qtd_itens = len(carrinho)
            
            print(f"\n╔{'═'*50}╗")
            print(f"║{'RESUMO DA COMPRA':^50}║")
            print(f"╠{'═'*50}╣")
            print(f"║ {'Total de itens:':<30} {qtd_itens:>18} ║")
            print(f"║ {'Valor total:':<30} R${total_cliente:>15.2f} ║")
            print(f"╚{'═'*50}╝\n")
            
            vendas_no_dia.append({
                "cliente": nome_cliente,
                "qtd_itens": qtd_itens,
                "total_gasto": total_cliente
            })
            
            total_itens_vendidos += qtd_itens
            total_arrecadado += total_cliente
            break

print(f"\n╔{'═'*70}╗")
print(f"║{'RELATÓRIO FINAL DO DIA':^70}║")
print(f"╠{'═'*70}╣")
print(f"║ {'CLIENTE':<30} {'ITENS':^10} {'VALOR GASTO':>25} ║")
print(f"╠{'═'*70}╣")

for venda in vendas_no_dia:
    print(f"║ {venda['cliente']:<30} {venda['qtd_itens']:^10} R${venda['total_gasto']:>22.2f} ║")

print(f"╠{'═'*70}╣")
print(f"║ {'TOTAL GERAL:':<40} {total_itens_vendidos:^10} R${total_arrecadado:>16.2f} ║")
print(f"╚{'═'*70}╝\n")