import csv

from functions import (
    limpar_categoria,
    tratar_categoria_vazia,
    calcular_media,
    tratar_dimensao,
    calcular_volume
)

CAMINHO_PRODUTOS = "data/raw/olist_products_dataset.csv"


def carregar_produtos(CAMINHO_PRODUTOS):

    produtos = []

    with open(CAMINHO_PRODUTOS, mode="r", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            produtos.append(produto)

    return produtos

def salvar_produtos(produtos, caminho_saida):
    
    colunas = produtos[0].keys()
    
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
        escritor.writerows(produtos)
        
def processar_produtos(caminho_entrada):
    produtos = carregar_produtos(caminho_entrada)
    
    pesos = []
    comprimentos = []
    alturas = []
    larguras = []
    
    # coleta valores válidos para cálculo das médias
    for produto in produtos:
        if produto["product_weight_g"] != "":

            pesos.append(
                float(produto["product_weight_g"])
            )
        if produto["product_length_cm"] != "":

            comprimentos.append(
                float(produto["product_length_cm"])
            )

        if produto["product_height_cm"] != "":

            alturas.append(
                float(produto["product_height_cm"])
            )
        if produto["product_width_cm"] != "":

            larguras.append(
                float(produto["product_width_cm"])
            )
    # calcular médias
    media_peso = calcular_media(pesos)
    media_comprimento = calcular_media(comprimentos)
    media_altura = calcular_media(alturas)
    media_largura = calcular_media(larguras)
    
    categorias_corrigidas = 0
    dimensoes_corrigidas = 0
    
    # Tratar os dados
    for produto in produtos:
        
        # categoria original 
        categoria_original = produto["product_category_name"]
        
        # tratar categoria vazia
        categoria = tratar_categoria_vazia(categoria_original)
        
        # limpar categoria
        categoria = limpar_categoria(categoria)
                                     
        produto["product_category_name"] = categoria
        
        # contador de categorias corrigidas
        if categoria_original.strip() == "":
            
            categorias_corrigidas += 1
        
        # tratar peso
        if produto["product_weight_g"] == "":
            dimensoes_corrigidas += 1
        produto["product_weight_g"] = tratar_dimensao(
            produto["product_weight_g"],
            media_peso
        )
        
        # tratart comprimento
        if produto["product_length_cm"] == "":
            dimensoes_corrigidas += 1
            
        produto["product_length_cm"] = tratar_dimensao(
            produto["product_length_cm"],
            media_comprimento
        )
        
        # tratar altura
        if produto["product_height_cm"] == "":
            dimensoes_corrigidas += 1
        produto["product_height_cm"] = tratar_dimensao(
            produto["product_height_cm"],
            media_altura
        )
        
        # tratar largura
        if produto["product_width_cm"] == "":
            dimensoes_corrigidas += 1
            
        produto["product_width_cm"] = tratar_dimensao(
            produto["product_width_cm"],
            media_largura
        )
        
        # criar nova coluna de volume
        produto["volume_cm3"] = calcular_volume(
            produto["product_length_cm"],
            produto["product_height_cm"],
            produto["product_width_cm"]
        )
    relatorio = {
        "total_produtos" : len(produtos),
        "categorias_corrigidas" : categorias_corrigidas,
        "dimensoes_corrigidas" : dimensoes_corrigidas
    }
    
    return produtos, relatorio