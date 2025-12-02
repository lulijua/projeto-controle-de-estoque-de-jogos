# 🕹️ Sistema de Controle de Estoque e Carrinho de Jogos

Este é um sistema modular em Python para gerenciar o Estoque de Jogos, Cadastros de Usuários e simular um Carrinho de Compras. Desenvolvido como projeto final para a disciplina de Introdução à Programação (INF - UFG 2025.2).

---

## 🚀 Funcionalidades

### 🧩 Cadastro de Produtos

- Adicionar jogos ao estoque
- Cada jogo possui:
    - Código ID
    - Nome
    - Empresa
    - Gênero
    - Lançamento
    - Classificação Indicativa
    - Preço
    - Avaliação
    - Quantidade
    - Descrição
    - Platformas
    - Requisitos
- Atualizar dados dos jogos
- Remover jogos
- Validações para evitar duplicatas

### 🔍 Busca de Produtos

- Busca por nome, gênero, empresa, avaliação, preço máximo e ano de lançamento.
- Busca avançada combinando múltiplos filtros.
- Recomendação de jogos baseada em preferências do usuário.
- Exibição simples de jogos e detalhes.
- Menus interativos (principal e de detalhes).

### 👤 Cadastro de Usúario

- Valida e cadastra usuários via input interativo até digitar SAIR.
- Impede duplicar usuário, email e telefone.
- Regras:
    - Nome: só letras (permite espaços).
    - Email: deve conter "@gmail" e não iniciar com "@".
    - Telefone: formato 99 999999999.
    - Idade: número entre 1 e 119.
    - Gêneros: escolhe 3 dentre lista permitida (rpg, fps, survival, puzzle, - chill, gacha, esportes, moba, terror, coop).
Armazena perfis em lista global clientes_cadastrados.
Exibe relatório formatado de todos os clientes ao final.

### 🛒 Inserção ao Carrinho

- Registra a saída de estoque
- Calcula o total faturado no dia
- Permite adicionar produtos ao carrinho
- Gera um desconto de 10%, com base numa probabilidade de 30%
- Finaliza a adição ao carrinho, listando os produtos adicionados e calculando seus preços

---

## 📁 Estrutura do Projeto

projeto-controle-de-estoque-de-jogos/
│
├── cadastro_de_produto.py
├── busca-de-produto.py
├── carrinho.py
├── cadastro_usuario.py
└── README.md

---

## 🛠️ Instalação e Dependências

- Este projeto requer Python 3.9+.
- Clone o repositório: git clone <https://github.com/lulijua/projeto-controle-de-estoque-de-jogos>
- Navegue até o diretório do projeto: cd projeto-controle-de-estoque-de-jogos

---

## ▶️ Como executar
- Cadastro de produtos:
```bash
python cadastro_de_produto.py
```
- Busca de produtos:
```bash
python busca-de-produto.py
```
- Cadastro de usuário:
```bash
python cadastro_usuario.py
```
- Carrinho (exemplo rápido de uso em Python):
```python
from carrinho import adicionar_ao_carrinho, finalizar_compra
adicionar_ao_carrinho("Zelda")
finalizar_compra()
```

---

## 🗺️ Roadmap (Futuras Melhorias)
- Persistir dados (arquivo/JSON/DB).
- Interface de linha de comando unificada (menu principal).
- Tratamento de erros e logs.
- Mais testes (busca avançada, erros de entrada, limites de estoque).

---

## 🤝 Contribuição
- Branches: `main` (estável), `desenvolvimento` (integração), `testes` (cobertura).
```bash
git switch -c minha-feature
git add -A && git commit -m "feat: descrição curta"
git push -u origin minha-feature
```
Abra um PR (Pull & Request) para `desenvolvimento`.

## 📄 Licença
MIT — sinta-se livre para usar e contribuir.

## 👥 Autores
Equipe do projeto:
 — Caio Cesar De Oliveira Pereira 
 — Luiza Ferreira Júa
 — Mariana Almeida Barros
 — Nicholas Martins
 


