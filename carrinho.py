from cadastro_de_produto import jogos_no_estoque, Produto
import random


carrinho = [] # lista que representa o carrinho de compras  
vendas_no_dia = []  # Lista para registrar as vendas do dia
total_arrecadado = 0.0  # inicializa total do dia

# produto a ser adicionado ao carrinho
def adicionar_ao_carrinho(nome_produto):
    
    produto_encontrado = None

    for jogo in jogos_no_estoque:
        if jogo.nome.lower().strip() == nome_produto.lower().strip():
            produto_encontrado = jogo
            break

    #Verifica se o produto foi encontrado
    if produto_encontrado is None:
        print("Produto não encontrado no estoque.")
        return False
        
    #Verifica se o produto está em estoque
    if produto_encontrado.quantidade <= 0:
        print("Produto fora de estoque.")
        return False    
        
    #Adiciona o produto ao carrinho
    carrinho.append(produto_encontrado)

    #Reduz a quantidade em estoque
    produto_encontrado.quantidade -= 1
    print(f"Produto {produto_encontrado.nome} adicionado ao carrinho.")
    return True

# função que decide (aleatoriamente) se aplica desconto a um item e retorna o preço a usar
def aplicar_desconto_item(item, taxa_desconto=0.10, probabilidade=0.3):
    
    preco_base = getattr(item, "preco_jogo", getattr(item, "preco", 0.0))
    if random.random() < probabilidade:
        novo_preco = round(preco_base * (1.0 - taxa_desconto), 2)
        return novo_preco, True
    
    return preco_base, False

def finalizar_compra():

    global total_arrecadado

    if not carrinho:
        print("Carrinho vazio. Adicione produtos antes de finalizar a compra.")
        return

    total_carrinho = 0.0

    for item in carrinho:
        
        preco_venda, ganhou = aplicar_desconto_item(item)
        if ganhou:
            print(f"Você ganhou um desconto no item: {item.nome}! Novo preço: R$ {preco_venda:.2f}")

        total_carrinho += preco_venda

        vendas_no_dia.append({"nome": item.nome, "preco": preco_venda})  # Adiciona registro da venda
        total_arrecadado += preco_venda # Atualiza o total arrecadado no dia
    
    print(f"Total da compra: R$ {total_carrinho:.2f}")
    carrinho.clear()  # Limpa o carrinho após a finalização da compra

def obter_vendas_do_dia():
    return list(vendas_no_dia)

def obter_total_arrecadado():
    return total_arrecadado

if __name__ == "__main__":
    print("--- Teste do Carrinho ---")

    # Tenta adicionar alguns jogos
    adicionar_ao_carrinho("Dark Souls II")
    adicionar_ao_carrinho("FIFA 23")
    adicionar_ao_carrinho("jogo inexistente")

    # Finaliza
    print("\nFinalizando compra:")
    finalizar_compra()