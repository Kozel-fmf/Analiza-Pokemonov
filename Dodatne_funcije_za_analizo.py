import ast

#V tej datoteki so zapisane funkcije, ki služijo za pomoč pri analizi

#Določi generacijo pokemona glede na njegovo stevilko
def doloci_generacijo(stevilka):
    if 1 <= stevilka <= 151:
        return 1  #Generacija 1
    elif 152 <= stevilka <= 251:
        return 2  #Generacija 2
    elif 252 <= stevilka <= 386:
        return 3  #Generacija 3
    elif 387 <= stevilka <= 493:
        return 4  #Generacija 4
    elif 494 <= stevilka <= 649:
        return 5  #Generacija 5
    elif 650 <= stevilka <= 721:
        return 6  #Generacija 6
    elif 722 <= stevilka <= 809:
        return 7  #Generacija 7
    elif 810 <= stevilka <= 898:
        return 8  #Generacija 8
    elif 899 <= stevilka <= 1025:
        return 9  #Generacija 9
    else:
        return None

#Spremeni niz v seznam   
def niz_v_seznam(vrednost):
    if isinstance(vrednost, str):
        return ast.literal_eval(vrednost)
    return vrednost
