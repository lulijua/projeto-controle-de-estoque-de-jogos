from cadastro_de_produto import jogos_no_estoque, Produto

# lista que representa o carrinho de compras
carrinho = []

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
    if produto_encontrado.quantidade_estoque <= 0:
        print("Produto fora de estoque.")
        return False    
        
    #Adiciona o produto ao carrinho
    carrinho.append(produto_encontrado)

    #Reduz a quantidade em estoque
    produto_encontrado.quantidade_estoque -= 1
    print(f"Produto {produto_encontrado.nome} adicionado ao carrinho.")
    return True

def finalizar_compra():

    if not carrinho:
        print("Carrinho vazio. Adicione produtos antes de finalizar a compra.")
        return

    total_carrinho = 0.0

    for item in carrinho:
        preco = item.preco
        total_carrinho += item.preco
        print(f"Item: {item.nome} - Preço: R$ {preco:.2f}")
    
    print(f"Total da compra: R$ {total_carrinho:.2f}")
    carrinho.clear()  # Limpa o carrinho após a finalização da compra