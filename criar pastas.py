import os

def criar_pastas():
    # Obtém o diretório atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    print(f"diretorio_atual: {diretorio_atual}")

    # Lista todos os itens no diretório atual
    itens = os.listdir(diretorio_atual)

    print(f"itens: {itens}")

    for item in itens:
        # Verifica se o item é um diretório
        if os.path.isdir(os.path.join(diretorio_atual, item)):
            # Cria as pastas 'src' e 'test cases' dentro do diretório
            pasta_src = os.path.join(diretorio_atual, item, 'src')
            pasta_testes = os.path.join(diretorio_atual, item, 'test cases')

            # Cria as pastas se elas não existirem
            if not os.path.exists(pasta_src):
                os.makedirs(pasta_src)
                print(f"Pasta 'src' criada em {os.path.join(item, 'src')}")
            if not os.path.exists(pasta_testes):
                os.makedirs(pasta_testes)
                print(f"Pasta 'test cases' criada em {os.path.join(item, 'test cases')}")

if __name__ == "__main__":
    criar_pastas()
