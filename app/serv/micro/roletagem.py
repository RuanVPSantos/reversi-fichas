import pandas as pd
from random import randint

def roletagem(data, max=65):
    roletaveis = pd.read_excel("./static/data.xlsx", data)
    dado = randint(1, max)
    roletado = roletaveis[roletaveis.chave >= dado].iloc[0].valor
    return roletado