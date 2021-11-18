'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

# 1. Vyžádá si od uživatele přihlašovací jméno a heslo.

oddelovac = "-" * 45
print(oddelovac)
username = input("Přihlašovací jméno: ")
password = input("Heslo: ")
print(oddelovac)

# 2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

registrovani = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# 3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty...

if registrovani.get(username) == password:
    print("Zdravím", username,". Povoleno analyzovat texty ...")
else:
    print("Přístup odepřen !")
    quit()
print(oddelovac)

# 4. Program nechá uživatel vybrat mezi třemi texty...

vyber_textu = int(input("Vyber text 1, 2 nebo 3: "))
if vyber_textu == 1 or vyber_textu == 2 or vyber_textu == 3:
    print("Vybrán text číslo ", vyber_textu, "...")
else:
    print("Neplatný výběr !")
    quit()
print(oddelovac)

# 5. Pro vybraný text spočítá následující statistiky...

cista_slova = []
for slovo in TEXTS[vyber_textu - 1].split():
    cista_slova.append(slovo.strip(".,"))
print("Počet slov je:", len(cista_slova))

s_velkym = 0
jen_mala = 0
jen_velka = 0
jen_cisla = 0
cisla = 0
for slovo in cista_slova:
    if slovo.istitle() == 1:
        s_velkym = s_velkym + 1
    elif slovo.islower() == 1:
        jen_mala = jen_mala + 1
    elif slovo.isupper() == 1:
        jen_velka = jen_velka + 1
    elif slovo.isnumeric() == 1:
        jen_cisla = jen_cisla + 1
        cisla = cisla + int(slovo)
print("Počet slov začínajících velkým písmenem:", s_velkym)
print("Počet slov psaných malými písmeny:", jen_mala)
print("Počet slov psaných velkými písmeny:", jen_velka)
print("Počet čísel (ne cifer):", jen_cisla)
print("Suma všech čísel (ne cifer) v textu:", cisla)
print(oddelovac)

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.

delka_slov = []
for slovo in cista_slova:
    delka_slov.append(len(slovo))
delka_slov.sort()

pismena = []
for cislo in delka_slov:
    if cislo not in pismena:
        pismena.append(cislo)

cetnosti = []
for cislo in pismena:
    cetnosti.append(delka_slov.count(cislo))

oddelovac_kratsi = "-" * 34
print(oddelovac_kratsi)
print("LEN".center(7),"|","ČETNOST".center(23))
print(oddelovac_kratsi)
for cislo in pismena:
    print(str(pismena[pismena.index(cislo)]).rjust(5),"  |", str("*"*cetnosti[pismena.index(cislo)]).ljust(19),
          str(cetnosti[pismena.index(cislo)]) + "x".ljust(4))
print(oddelovac_kratsi)

# Vyhnul jsem se slovníku... :-)
