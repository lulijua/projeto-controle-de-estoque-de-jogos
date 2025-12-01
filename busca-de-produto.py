from cadastro_de_produto import Produto, jogos_no_estoque
from cadastro_usuario import clientes_cadastrados

class SistemaBusca:
    def __init__(self):
        self.estoque = jogos_no_estoque
        self.usuarios = clientes_cadastrados
    
    # ========== MÉTODOS DE BUSCA ==========
    
    def buscar_por_nome(self, termo_busca):
        """Busca jogos pelo nome (busca parcial)"""
        resultados = []
        termo = termo_busca.lower()
        
        for jogo in self.estoque:
            if termo in jogo.nome.lower():
                resultados.append(jogo)
        
        return resultados
    
    def buscar_por_genero_exato(self, genero_busca):
        """Busca jogos por gênero EXATO (um gênero por jogo)"""
        resultados = []
        genero = genero_busca.strip().lower()
        
        for jogo in self.estoque:
            if jogo.genero.strip().lower() == genero:
                resultados.append(jogo)
        
        return resultados
    
    def buscar_por_empresa(self, empresa_busca):
        """Busca jogos por empresa desenvolvedora"""
        resultados = []
        empresa = empresa_busca.lower()
        
        for jogo in self.estoque:
            if empresa in jogo.empresa.lower():
                resultados.append(jogo)
        
        return resultados
    
    def buscar_por_avaliacao_exata(self, avaliacao_busca):
        """Busca jogos com avaliação EXATA"""
        resultados = []
        
        for jogo in self.estoque:
            if jogo.avaliacao == avaliacao_busca:
                resultados.append(jogo)
        
        return resultados
    
    def buscar_por_preco(self, max_preco):
        """Busca jogos até um preço máximo"""
        resultados = []
        
        for jogo in self.estoque:
            if jogo.preco <= max_preco:
                resultados.append(jogo)
        
        resultados.sort(key=lambda x: x.preco)
        return resultados
    
    def buscar_por_lancamento_exato(self, ano_busca):
        """Busca jogos com ano de lançamento EXATO"""
        resultados = []
        
        for jogo in self.estoque:
            if jogo.lancamento == ano_busca:
                resultados.append(jogo)
        
        return resultados
    
    def buscar_avancada(self, **filtros):
        """Busca avançada com múltiplos filtros"""
        resultados = self.estoque
        
        if 'nome' in filtros and filtros['nome']:
            termo = filtros['nome'].lower()
            resultados = [j for j in resultados if termo in j.nome.lower()]
        
        if 'genero' in filtros and filtros['genero']:
            termo = filtros['genero'].strip().lower()
            resultados = [j for j in resultados if j.genero.strip().lower() == termo]
        
        if 'empresa' in filtros and filtros['empresa']:
            termo = filtros['empresa'].lower()
            resultados = [j for j in resultados if termo in j.empresa.lower()]
        
        if 'avaliacao_exata' in filtros:
            resultados = [j for j in resultados if j.avaliacao == filtros['avaliacao_exata']]
        
        if 'max_preco' in filtros:
            resultados = [j for j in resultados if j.preco <= filtros['max_preco']]
        
        if 'lancamento_exato' in filtros:
            resultados = [j for j in resultados if j.lancamento == filtros['lancamento_exato']]
        
        return resultados
    
    def recomendar_para_usuario(self, usuario_nome, max_resultados=5):
        """Recomenda jogos baseado nas preferências do usuário (por NOME DE USUÁRIO)"""
        usuario_encontrado = None
        
        for usuario in self.usuarios:
            if usuario['Usuario'].lower() == usuario_nome.lower():
                usuario_encontrado = usuario
                break
        
        if not usuario_encontrado:
            print(f"\nUsuário '{usuario_nome}' não encontrado!")
            return []
        
        recomendacoes = []
        generos_preferidos = [
            usuario_encontrado['jogo_genero']['Genero1'],
            usuario_encontrado['jogo_genero']['Genero2'],
            usuario_encontrado['jogo_genero']['Genero3']
        ]
        
        for genero in generos_preferidos:
            if genero:
                jogos_genero = self.buscar_por_genero_exato(genero)
                recomendacoes.extend(jogos_genero)
        
        # Não precisa remover duplicatas - cada jogo tem apenas um gênero
        # Ordenar por avaliação (melhores primeiro)
        recomendacoes.sort(key=lambda x: x.avaliacao, reverse=True)
        
        return recomendacoes[:max_resultados]
    
    # ========== MÉTODOS DE EXIBIÇÃO ==========
    
    def exibir_jogo_simples(self, jogo):
        """Exibe um jogo em formato simplificado"""
        estrelas = "★" * jogo.avaliacao + "☆" * (5 - jogo.avaliacao)
        
        print("+" + "=" * 68 + "+")
        print(f"| {jogo.nome.upper():^66} |")
        print("+" + "=" * 68 + "+")
        print(f"| ID:            {jogo.identificacao:<52} |")
        print(f"| Empresa:       {jogo.empresa:<52} |")
        print(f"| Gênero:        {jogo.genero:<52} |")
        print(f"| Lançamento:    {jogo.lancamento:<52} |")
        print(f"| Preço:         R$ {jogo.preco:<49.2f} |")
        print(f"| Avaliação:     {estrelas} ({jogo.avaliacao}/5){' ' * 36} |")
        print(f"| Estoque:       {jogo.quantidade} cópias{' ' * 44} |")
        print("+" + "=" * 68 + "+")
    
    def exibir_resultados(self, resultados, titulo="RESULTADOS DA BUSCA"):
        """Exibe uma lista de resultados"""
        if not resultados:
            print(f"\n{titulo}: Nenhum jogo encontrado!")
            return
        
        print(f"\n{'='*70}")
        print(f"{titulo} ({len(resultados)} jogos encontrados)")
        print('='*70)
        
        for i, jogo in enumerate(resultados, 1):
            estrelas = "★" * jogo.avaliacao + "☆" * (5 - jogo.avaliacao)
            print(f"{i:2d}. {jogo.nome:<35} | {jogo.genero:<15} | R$ {jogo.preco:7.2f} | {estrelas}")
    
    def exibir_detalhes_jogo(self, index, resultados):
        """Exibe detalhes completos de um jogo específico"""
        if 0 <= index < len(resultados):
            jogo = resultados[index]
            jogo.exibir_formatado()
        else:
            print("Índice inválido!")
    
    # ========== MENU PRINCIPAL ==========
    
    def menu_principal(self):
        """Menu interativo do sistema de busca"""
        while True:
            print("\n" + "="*70)
            print("SISTEMA DE BUSCA E RECOMENDAÇÃO DE JOGOS")
            print("="*70)
            print(f"Jogos no estoque: {len(self.estoque)}")
            print(f"Usuários cadastrados: {len(self.usuarios)}")
            print("="*70)
            print("\nMENU DE BUSCA:")
            print("1. Buscar por nome do jogo")
            print("2. Buscar por gênero")
            print("3. Buscar por empresa desenvolvedora")
            print("4. Buscar por avaliação exata")
            print("5. Buscar por preço máximo")
            print("6. Buscar por ano de lançamento exato")
            print("7. Busca avançada (múltiplos filtros)")
            print("8. Recomendações personalizadas")
            print("9. Ver todos os jogos disponíveis")
            print("10. Ver todos os usuários cadastrados")
            print("0. Sair do sistema")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            match opcao:
                case "1":
                    print("\nBUSCA POR NOME")
                    nome = input("Digite o nome (ou parte) do jogo: ").strip()
                    resultados = self.buscar_por_nome(nome)
                    self.exibir_resultados(resultados, f"BUSCA POR: '{nome}'")
                    self.menu_detalhes(resultados)
                
                case "2":
                    print("\nBUSCA POR GÊNERO")
                    print("Gêneros disponíveis: RPG, FPS, Survival, MOBA, Gacha, Terror, Puzzle, Esportes, Chill, Coop")
                    genero = input("Digite o gênero: ").strip()
                    resultados = self.buscar_por_genero_exato(genero)
                    self.exibir_resultados(resultados, f"JOGOS DE {genero.upper()}")
                    self.menu_detalhes(resultados)
                
                case "3":
                    print("\nBUSCA POR EMPRESA")
                    empresa = input("Digite o nome da empresa: ").strip()
                    resultados = self.buscar_por_empresa(empresa)
                    self.exibir_resultados(resultados, f"JOGOS DA {empresa.upper()}")
                    self.menu_detalhes(resultados)
                
                case "4":
                    print("\nBUSCA POR AVALIAÇÃO EXATA")
                    try:
                        avaliacao = int(input("Avaliação exata (1 a 5): "))
                        if 1 <= avaliacao <= 5:
                            resultados = self.buscar_por_avaliacao_exata(avaliacao)
                            self.exibir_resultados(resultados, f"JOGOS COM {avaliacao} ESTRELAS")
                            self.menu_detalhes(resultados)
                        else:
                            print("Avaliação deve ser entre 1 e 5!")
                    except ValueError:
                        print("Digite um número válido!")
                
                case "5":
                    print("\nBUSCA POR PREÇO MÁXIMO")
                    try:
                        max_preco = float(input("Preço máximo (R$): "))
                        if max_preco >= 0:
                            resultados = self.buscar_por_preco(max_preco)
                            self.exibir_resultados(resultados, f"JOGOS ATÉ R$ {max_preco:.2f}")
                            self.menu_detalhes(resultados)
                        else:
                            print("Preço deve ser positivo!")
                    except ValueError:
                        print("Digite um preço válido!")
                
                case "6":
                    print("\nBUSCA POR ANO DE LANÇAMENTO EXATO")
                    try:
                        ano = int(input("Ano exato de lançamento (ex: 2018): "))
                        if 1980 <= ano <= 2025:
                            resultados = self.buscar_por_lancamento_exato(ano)
                            self.exibir_resultados(resultados, f"JOGOS LANÇADOS EM {ano}")
                            self.menu_detalhes(resultados)
                        else:
                            print("Ano deve estar entre 1980 e 2025!")
                    except ValueError:
                        print("Digite um ano válido!")
                
                case "7":
                    print("\nBUSCA AVANÇADA")
                    print("Preencha os filtros (deixe em branco para ignorar):")
                    
                    nome = input("Nome: ").strip()
                    genero = input("Gênero: ").strip()
                    empresa = input("Empresa: ").strip()
                    
                    avaliacao_input = input("Avaliação exata (1-5): ").strip()
                    avaliacao_exata = int(avaliacao_input) if avaliacao_input else None
                    
                    max_preco_input = input("Preço máximo R$: ").strip()
                    max_preco = float(max_preco_input) if max_preco_input else None
                    
                    lancamento_input = input("Ano exato de lançamento: ").strip()
                    lancamento_exato = int(lancamento_input) if lancamento_input else None
                    
                    filtros = {}
                    if nome: filtros['nome'] = nome
                    if genero: filtros['genero'] = genero
                    if empresa: filtros['empresa'] = empresa
                    if avaliacao_exata is not None: filtros['avaliacao_exata'] = avaliacao_exata
                    if max_preco is not None: filtros['max_preco'] = max_preco
                    if lancamento_exato is not None: filtros['lancamento_exato'] = lancamento_exato
                    
                    resultados = self.buscar_avancada(**filtros)
                    
                    desc_filtros = []
                    for chave, valor in filtros.items():
                        if chave == 'avaliacao_exata':
                            desc_filtros.append(f"Avaliação: {valor}★")
                        elif chave == 'max_preco':
                            desc_filtros.append(f"Preço: R$ {valor:.2f}")
                        elif chave == 'lancamento_exato':
                            desc_filtros.append(f"Ano: {valor}")
                        else:
                            desc_filtros.append(f"{chave}: {valor}")
                    
                    titulo = "BUSCA AVANÇADA: " + " | ".join(desc_filtros)
                    self.exibir_resultados(resultados, titulo)
                    self.menu_detalhes(resultados)
                
                case "8":
                    print("\nRECOMENDAÇÕES PERSONALIZADAS")
                    
                    if self.usuarios:
                        print("Usuários cadastrados (nome de usuário):")
                        for i, usuario in enumerate(self.usuarios[:10], 1):
                            generos = f"{usuario['jogo_genero']['Genero1']}, {usuario['jogo_genero']['Genero2']}, {usuario['jogo_genero']['Genero3']}"
                            print(f"  {i}. {usuario['Usuario']} - {usuario['Idade']} anos - Prefere: {generos}")
                    
                    usuario_nome = input("\nDigite o NOME DE USUÁRIO: ").strip()
                    
                    try:
                        max_resultados = int(input("Quantas recomendações deseja? (padrão: 5): ") or "5")
                    except ValueError:
                        max_resultados = 5
                    
                    resultados = self.recomendar_para_usuario(usuario_nome, max_resultados)
                    
                    if resultados:
                        usuario = None
                        for u in self.usuarios:
                            if u['Usuario'].lower() == usuario_nome.lower():
                                usuario = u
                                break
                        
                        if usuario:
                            print(f"\nRECOMENDAÇÕES PARA {usuario['Usuario'].upper()}")
                            generos = f"{usuario['jogo_genero']['Genero1']}, {usuario['jogo_genero']['Genero2']}, {usuario['jogo_genero']['Genero3']}"
                            print(f"   Gêneros preferidos: {generos}")
                        
                        self.exibir_resultados(resultados, "RECOMENDAÇÕES PERSONALIZADAS")
                        self.menu_detalhes(resultados)
                
                case "9":
                    print("\nTODOS OS JOGOS DISPONÍVEIS")
                    resultados = self.estoque
                    resultados.sort(key=lambda x: x.nome)
                    self.exibir_resultados(resultados, "CATÁLOGO COMPLETO")
                    self.menu_detalhes(resultados)
                
                case "10":
                    print("\nUSUÁRIOS CADASTRADOS")
                    print("="*60)
                    for i, usuario in enumerate(self.usuarios, 1):
                        print(f"\n{i}. {usuario['Usuario']}")
                        print(f"   Nome: {usuario['Nome']}")
                        print(f"   Email: {usuario['Email']}")
                        print(f"   Telefone: {usuario['Numero']}")
                        print(f"   Idade: {usuario['Idade']} anos")
                        generos = f"{usuario['jogo_genero']['Genero1']}, {usuario['jogo_genero']['Genero2']}, {usuario['jogo_genero']['Genero3']}"
                        print(f"   Gêneros preferidos: {generos}")
                        print("-" * 50)
                
                case "0":
                    print("\n" + "="*70)
                    print("Obrigado por usar o Sistema de Busca de Jogos!")
                    print("Até logo!")
                    print("="*70)
                    break
                
                case _:
                    print("Opção inválida! Tente novamente.")
            
            if opcao != "0":
                input("\nPressione Enter para voltar ao menu principal...")
    
    def menu_detalhes(self, resultados):
        """Menu para ver detalhes de jogos específicos"""
        if not resultados:
            return
        
        while True:
            print(f"\nDETALHES DOS JOGOS ENCONTRADOS")
            print("-" * 50)
            print("Digite o número do jogo para ver detalhes completos")
            print("Digite 'V' para voltar ao menu principal")
            print("Digite 'S' para fazer nova busca")
            
            opcao = input("\nSua escolha: ").strip().upper()
            
            match opcao:
                case 'V':
                    break
                case 'S':
                    return True
                case _:
                    try:
                        index = int(opcao) - 1
                        if 0 <= index < len(resultados):
                            print("\n" + "="*70)
                            print("DETALHES COMPLETOS DO JOGO")
                            print("="*70)
                            self.exibir_detalhes_jogo(index, resultados)
                            
                            print("\nDeseja ver detalhes de outro jogo?")
                            print("1. Sim, escolher outro número")
                            print("2. Não, voltar ao menu")
                            escolha = input("Escolha: ").strip()
                            if escolha == "2":
                                break
                        else:
                            print(f"Número inválido! Digite um número entre 1 e {len(resultados)}")
                    except ValueError:
                        print("Opção inválida! Digite um número, 'V' ou 'S'")

def mostrar_bem_vindo():
    """Exibe tela de boas-vindas"""
    print("\n" + "="*70)
    print("BEM-VINDO AO SISTEMA DE BUSCA DE JOGOS")
    print("="*70)
    print("\nEste sistema integra:")
    print("- Estoque de jogos (cadastro_de_produto.py)")
    print("- Cadastro de usuários (cadastro_de_usuario.py)")
    print("- Sistema de busca e recomendações")
    print("\n" + "="*70)

def main():
    mostrar_bem_vindo()
    
    sistema = SistemaBusca()
    
    print("\nCARREGANDO DADOS...")
    print(f"   Jogos carregados: {len(sistema.estoque)}")
    print(f"   Usuários carregados: {len(sistema.usuarios)}")
    
    if not sistema.estoque:
        print("\nAVISO: Nenhum jogo encontrado no estoque!")
        print("   Execute primeiro o cadastro_de_produto.py")
        resposta = input("   Deseja continuar mesmo assim? (s/n): ").lower()
        if resposta != 's':
            print("Programa encerrado.")
            return
    
    if not sistema.usuarios:
        print("\nAVISO: Nenhum usuário encontrado!")
        print("   Execute o cadastro_de_usuario.py para recomendações personalizadas")
        input("\nPressione Enter para continuar...")
    
    sistema.menu_principal()

if __name__ == "__main__":
    main()