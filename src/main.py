from products_processing import (processar_produtos, salvar_produtos)
import os 

CAMINHO_PRODUTOS_ENTRADA = '../data/raw/olist_products_dataset.csv'
CAMINHO_PRODUTOS_SAIDA = '../data/processed/produtos_tratados.csv'


def main():
    produtos, relatorio = processar_produtos(
        CAMINHO_PRODUTOS_ENTRADA
    )
    salvar_produtos(
        produtos,
        CAMINHO_PRODUTOS_SAIDA
    )
    
    print("=" * 50)
    print("RELATÓRIO DE PROCESSAMENTO")
    print("=" * 50)
    
    print(
        f"Categorias Corrigidas: "
        f"{relatorio['categorias_corrigidas']}"
    )
    
    print(
        f"Dimensões corrigidas: "
        f"{relatorio['dimensoes_corrigidas']}"
    )
    
if __name__ == "__main__":
    main()


