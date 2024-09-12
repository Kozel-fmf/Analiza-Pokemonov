import requests
import json
import csv
from Preberi_podatke import *


#S spletne strani pobere html kodo in jo shrani v datoteko
url = "https://www.serebii.net/pokemon/nationalpokedex.shtml"
odziv = requests.get(url)
if odziv.status_code == 200:
    print(url)
    with open("stran.html", "w") as f:
        f.write(odziv.text)
else:
   print("Prišlo je napake")


#Prebere datoteko, ki smo jo zgoraj ustvarili
with open("stran.html") as f:
    vsebina = f.read()


#V seznam pokemoni vstavi slovarje vseh pokemonov s podatki
pokemoni = []
for blok in vzorec_bloka.finditer(vsebina):
    vsi_podatki = izloci_stevilko(blok.group(0)) | izloci_ime(blok.group(0)) | izloci_type(blok) | izloci_signature_move(blok) | izloci_hp(blok) | izloci_att(blok) |izloci_def(blok) |izloci_sp_att(blok) | izloci_sp_def(blok) | izloci_spd(blok)
    pokemoni.append(vsi_podatki)


#Iz pridobljenih podatkov naredi .json datoteko
with open("pokemoni.json", "w") as f:
    json.dump(pokemoni, f, ensure_ascii = False, indent = 4)


#Iz pridobljenih podatkov naredi .csv datoteko
with open("pokemoni.csv", "w") as f:
    pisatelj = csv.DictWriter(f, fieldnames=["Stevilka", "Ime", "Type", "Signature_move", "Hp", "Attack", "Defense", "Sp_Att", "Sp_Def", "Speed"])
    pisatelj.writeheader()
    for pokemon in pokemoni:
        pisatelj.writerow(pokemon)