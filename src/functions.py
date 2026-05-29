# limpeza
# regex
# # datas 
# médias
# vaidaçãooes
import re
from datetime import datetime

# remover espaço colocar tudo com letras minusculas e remover caraters
def limpar_categoria(categoria):
    #transformar em minúsculo
    categoria = categoria.lower()
    # remover espaço extra
    categoria = categoria.strip()
    # substituir underline por espaço
    categoria =  categoria.replace("_", " ")
    
    # remover caracteres espaciais
    categoria = re.sub(
        r"[^a-zA-Zà-ÿ0-9\s]",
        "",
        categoria
    )
    # remover espaços duplicados
    categoria = re.sub(r"\s+", " ", categoria)
    
    # primeira letra maiúscula em cada palavra
    categoria = categoria.title()

    return categoria
# tratar as categoria vazias substituindo  por sem categoria
def tratar_categoria_vazia(categoria):
    
    if categoria.strip() == "":
        
        return "Sem Categoria"
    
    return categoria

# converter datas
def converter_data(data):
    
    if data.strip() == "":
        return ""
    data_convertida = datetime.strptime(
        data,
        "%Y-%m-%d %H:%M:%S"
    )
    
    return data_convertida.strftime("%d/%m/%Y")

## cALCULAR MÉDIA
def calcular_media(lista_valores):
    soma = sum(lista_valores)
    quantidade = len(lista_valores)
    media = soma / quantidade
    
    return round(media, 2)

# tratar dimensoes vazias 
def tratar_dimensao(valor, media):

    if valor.strip() == "":

        return media

    return float(valor)

# calcular volume do produto

def calcular_volume(
    comprimento,
    altura,
    largura
):
    if (
        comprimento == ""
        or altura == ""
        or largura == ""
    ):
        return 0

    volume = (
        float(comprimento)
        * float(altura)
        * float(largura)
    )

    return round(volume, 2)

if __name__ == "__main__":

    print(limpar_categoria(" Informática### "))
    print(limpar_categoria("cama_Mesa_Banho!!!"))
    print(limpar_categoria("telefonia   "))
    
    print(tratar_categoria_vazia(""))
    

    data = "2017-05-16 15:05:35"

    print(converter_data(data))
    
    valores = [10,20,30]
    print(calcular_media(valores))
    
    print(tratar_dimensao("", 250.0))
    
    print(calcular_volume(20, 10, 0))