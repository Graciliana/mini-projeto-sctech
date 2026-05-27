import csv

CAMINHO_PRODUTOS = "data/raw/olist_products_dataset.csv"


def carregar_produtos(CAMINHO_PRODUTOS):

    produtos = []

    with open(CAMINHO_PRODUTOS, mode="r", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            produtos.append(produto)

    return produtos


dados_produtos = carregar_produtos(CAMINHO_PRODUTOS)

print(f"Total de produtos carregados: {len(dados_produtos)}")

print("\nPrimeiro registro:\n")

print(dados_produtos[0])

print(" Verificar as colunas ")
print(dados_produtos[0].keys())
print(type(dados_produtos[0]))

for produto in dados_produtos[:5]:
    print(produto)