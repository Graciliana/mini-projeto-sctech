import csv
from functions import converter_data

CAMINHO_ORDER = "../data/raw/olist_orders_dataset.csv"

def carregar_orders(CAMINHO_ORDER):

    orders = []

    with open(CAMINHO_ORDER, mode="r", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for order in leitor:
            orders.append(order)

    return orders
def salvar_orders(orders, caminho_saida):
    
    colunas = orders[0].keys()
    
    with open(
        caminho_saida,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=colunas
        )
        
        escritor.writeheader()
        
        escritor.writerows(orders)

def processar_orders(caminho_entrada):
    orders = carregar_orders(caminho_entrada)
    # contadores do Relatorio
    
    orders_cancelados = 0
    
    inconsistencias = 0
    
    datas_covertidas = 0
    
    orders_entregues_sem_data = 0
    
    # processamento dos pedidos
    for order in orders:
        # conversoa da data de aprovação
        data_aprovacao = order["order_approved_at"]
        
        if data_aprovacao != "":
            order["order_approved_at"] = converter_data(
                data_aprovacao
            )
            datas_covertidas += 1
        # verificar entrega vazias
        data_entrega = (
            order["order_delivered_customer_date"]
        )
        
        status =  order["order_status"]
        
        if data_entrega == "":
            
            # pedido cancelado
            if status == "canceled":
                orders_cancelados += 1
                
            #pedidos entregue sem data
            elif status == "delivered":
                orders_entregues_sem_data += 1
                
                inconsistencias += 1
                
            # outros casos inconsist
            else:
                inconsistencias += 1
    
    # realtorio final
    
    relatorio = {
        "total_pedidos": len(orders),
        "pedidos_cancelado" : orders_cancelados,
        "inconsistencias" : inconsistencias,
        "datas_convertidas" : datas_covertidas,
        "pedidos_entregues_sem_data" :orders_entregues_sem_data
    }
    return orders, relatorio