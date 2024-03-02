from app.serv.micro.roletagem import roletagem

def etnia(raca):
    nova_etnia = ""
    if raca == "Humano":
        nova_etnia = ""
    if raca == "Monstros":
        nova_etnia = f'{roletagem("monstros", 44)}'
        if nova_etnia == 'Djinn':
            nova_etnia = f'Djinn do {roletagem("elementos", 9)}'
        if nova_etnia == 'Elemental':
            nova_etnia = f'Elemental do {roletagem("elementos", 9)}'

    if raca == "Demônio":
        nova_etnia = f'{roletagem("demonios", 44)}'
        if nova_etnia == "Os Pecados":
            nova_etnia = f"Pecado da {roletagem('pecado', 7)}"
        if nova_etnia == "Os do Apocalipse":
            nova_etnia = f"Apocalipse Da {roletagem('apocalipse', 4)}"

    if raca == "Mortos-Vivos Verdadeiros":
        nova_etnia = f'{roletagem("mvvs", 76)}'

    if raca == "Vampiros":
        nova_etnia = f"{roletagem('vampiros', 35)}"
        if nova_etnia == "Vampiro Ferai":
            nova_etnia= f"Vampiro Ferai {roletagem('ferai', 17)}"
        if nova_etnia == "Vampiro Perpétuo":
            nova_etnia = roletagem('perpetuos', 7)
            femininos = ['Morte', 'Destruição']
            artigo = 'o'
            if nova_etnia in femininos:
                artigo = 'a'
            nova_etnia = f"Vampiro Perpétuo d{artigo} {nova_etnia}"
    if raca == "Goblinoides":
        nova_etnia = roletagem('goblinoides', 131)

    if raca == "Elfos":
        nova_etnia = roletagem("elfos", 87)

    if raca == 'Îngerii':
        nova_etnia = roletagem("ingerii", 86)
    
    return nova_etnia