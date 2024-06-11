def criar_carro(marca, modelo, ano, cor):
    carro = {"Marca": marca, "Modelo": modelo, "Ano": ano, "Cor":cor }
    return carro

def adicionar_carro(lista_carros, dicionario_carro):
    lista_carros.append(dicionario_carro)
    return lista_carros

def remover_carro_por_modelo(lista_carros, modelo):
    for elemento in lista_carros:
        if (elemento["Modelo"] == modelo):
            lista_carros.remove(elemento)
    return lista_carros

def ordenar_carros_por_ano(lista):
    lista_ordenada = sorted(lista, key=lambda x:x["Ano"], reverse=True)
    return lista_ordenada

def atualizar_cor_carro(carros, modelo, nova_cor):
    for elemento in carros:
       if elemento["Modelo"] == modelo:
           elemento["Cor"] = nova_cor
    return carros
           