import re

#blok vseh podatkov o enem pokemonu
vzorec_bloka = re.compile(
    r'#\d{4}\s*</td>[\s\S]*?<td align="center" class="fooinfo">\d+</td>\s*<td align="center" class="fooinfo">'
    r'\d+</td>\s*<td align="center" class="fooinfo">\d+</td>\s*<td align="center" class="fooinfo">\d+</td>\s*'
    r'<td align="center" class="fooinfo">\d+</td>\s*<td align="center" class="fooinfo">\d+</td>',
    flags=re.DOTALL)


#Spodnji vzorci so namenjeni iskanju željenih podatkov v dani html kodi
vzorec_stevilke = re.compile(
    r'#(?P<Stevilka>\d+)')

vzorec_imena = re.compile(
    r'<\s*a\s+href="[^"]+">(?P<Ime>[^<]+)<\/a>\n')

vzorec_type = re.compile(
    r'/pokemon(?P<Type>/type/([a-zA-Z]+))')

vzorec_signature_move = re.compile(
    r'<\s*a\s+href="/abilitydex/[^"]+">(?P<Signature_move>[^<]+)<\/a>\s*')

vzorec_stats = re.compile(
    r'<td align="center" class="fooinfo">(?P<Hp>\d+)</td>\s*'
    r'<td align="center" class="fooinfo">(?P<Attack>\d+)</td>\s*'
    r'<td align="center" class="fooinfo">(?P<Defense>\d+)</td>\s*'
    r'<td align="center" class="fooinfo">(?P<Sp_Att>\d+)</td>\s*'
    r'<td align="center" class="fooinfo">(?P<Sp_Def>\d+)</td>\s*'
    r'<td align="center" class="fooinfo">(?P<Speed>\d+)</td>')


#Naslednje fukcije bodo za vsak blok podatkov izločile željene podatke in jih spravile v slovar
def izloci_stevilko(blok):
    stevilka = vzorec_stevilke.search(blok).groupdict()
    stevilka['Stevilka'] = int(stevilka['Stevilka'])
    return stevilka

def izloci_ime(blok):
    ime = vzorec_imena.search(blok).groupdict()
    ime['Ime'] = ime['Ime']   
    return ime

def izloci_type(blok):
    seznam_tipov = []
    slovar_tipov = {}
    for i in vzorec_type.finditer(blok.group(0)):
        tip = i.group('Type')[6:] 
        seznam_tipov.append(tip)
    slovar_tipov['Type'] = seznam_tipov   
    return slovar_tipov

def izloci_signature_move(blok):
    seznam_signature_moves = []
    slovar_signature_moves = {}
    for i in vzorec_signature_move.finditer(blok.group(0)):
        signature_move = i.group('Signature_move')
        seznam_signature_moves.append(signature_move)
        slovar_signature_moves['Signature_move'] = seznam_signature_moves
    return slovar_signature_moves

def izloci_hp(blok):
    slovar_hp = {}
    for vrstica in vzorec_stats.finditer(blok.group(0)):
        slovar_hp['Hp'] = int(vrstica.group('Hp'))
    return slovar_hp

def izloci_att(blok):
    slovar_att = {}
    for vrstica in vzorec_stats.finditer(blok.group(0)):
        slovar_att['Attack'] = int(vrstica.group('Attack'))
    return slovar_att

def izloci_def(blok):
    slovar_def = {}
    for vrstica in vzorec_stats.finditer(blok.group(0)):
        slovar_def['Defense'] = int(vrstica.group('Defense'))
    return slovar_def

def izloci_sp_att(blok):
    slovar_sp_att = {}
    for vrstica in vzorec_stats.finditer(blok.group(0)):
        slovar_sp_att['Sp_Att'] = int(vrstica.group('Sp_Att'))
    return slovar_sp_att

def izloci_sp_def(blok):
    slovar_sp_def = {}
    for vrstica in vzorec_stats.finditer(blok.group(0)):
        slovar_sp_def['Sp_Def'] = int(vrstica.group('Sp_Def'))
    return slovar_sp_def

def izloci_spd(blok):
    slovar_spd = {}
    for vrstica in vzorec_stats.finditer(blok.group(0)):
        slovar_spd['Speed'] = int(vrstica.group('Speed'))
    return slovar_spd  