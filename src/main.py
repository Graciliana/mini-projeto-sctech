from products_processing import (processar_produtos, salvar_produtos)
from orders_processing import (processar_orders, salvar_orders)
import os 

CAMINHO_PRODUTOS_ENTRADA = '../data/raw/olist_products_dataset.csv'
CAMINHO_PRODUTOS_SAIDA = '../data/processed/produtos_tratados.csv'

CAMINHO_ORDERS_ENTRADA = '../data/raw/olist_orders_dataset.csv'
CAMINHO_ORDERS_SAIDA = '../data/processed/orders_tratados.csv'


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
        f"Total de produtos: "
        f"{relatorio['total_produtos']}"
    )
    
    print(
        f"Categorias Corrigidas: "
        f"{relatorio['categorias_corrigidas']}"
    )
    
    print(
        f"Dimensões corrigidas: "
        f"{relatorio['dimensoes_corrigidas']}"
    )
    print("\n")
    
    
    print("=" * 50)
    print("RELATÓRIO DE PEDIDOS")
    print("=" * 50)
    
    orders, relatorio_orders = (
        processar_orders(CAMINHO_ORDERS_ENTRADA)
    )
    
    salvar_orders(
        orders,
        CAMINHO_ORDERS_SAIDA
    )
    
    print(
        f"Total de pedidos: "
        f"{relatorio_orders['total_pedidos']}"
    )
    print(
        f"Pedidos cancelados: "
        f"{relatorio_orders['pedidos_cancelado']}"
    )
    print(
        f"Inconsistências: "
        f"{relatorio_orders['inconsistencias']}"
    )
    print(
        f"Datas convertidas: "
        f"{relatorio_orders['datas_convertidas']}"
    )
    print(
        f"Pedidos entregues sem data: "
        f"{relatorio_orders['pedidos_entregues_sem_data']}"
    )
    
    print("\n")
    
    print("=" * 50)

if __name__ == "__main__":
    main()


