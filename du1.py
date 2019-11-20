from math import sin, tan, log, radians, e
result = []  # výsledný seznam poledníků
result1 = []  # výsledný seznam rovnoběžek

def vypocet_poledniku():
    for v in range(-180, 190, 10):
        polednik1 = R * radians(v) * 100000 # poledniky po vypoctu
        polednik2 = polednik1 / x  # vydeleno meritkem
        if polednik2 > 100 or polednik2 < -100:  # ošetření vzdáleností nad 1 m
            result.append("-")
        else:
            polednik3 = round(polednik2, 1)  # zaokrouhleni na milimetry
            result.append(float(polednik3))  # vysledek vydeleny meritkem přidán do seznamu

def vypocet_rovnobezek():
    rovnobezka2 = rovnobezka1 / x  # stejný postup jako u poledníků, akorát chybí první krok, vždy jiný vzorec,
    # pokracuje na řádcích 43 až 58
    if rovnobezka2 > 100 or rovnobezka2 < -100:
        result1.append("-")
    else:
        rovnobezka3 = round(rovnobezka2, 1)
        result1.append(float(rovnobezka3))

zobrazeni = str(input("Zadej typ zobrazení"))
if zobrazeni != 'L' and zobrazeni != 'M' and zobrazeni != 'B' and zobrazeni != 'A':  # ošetřená špatná zobrazení
    print("Zadej správné zobrazení")
    quit()

x = float(input("Zadej měřítko"))
if x <= 0:  # ošetřené záporné či nulové měřítko
    print("Zadej měřítko větší než 0")
    quit()

R= float(input("Zadej poloměr Země"))  # libovolný poloměr Země
if R == 0:
    R = 6371.11
elif R < 0:
    print("Zadej kladný poloměr Země v cm")
    quit()

vypocet_poledniku()

if zobrazeni == 'L':
    for u in range(-90, 100, 10):
        rovnobezka1 = R*sin(radians(u)) * 100000
        vypocet_rovnobezek()
elif zobrazeni == 'A':
    for u in range(-90, 100, 10):
        rovnobezka1 = R*radians(u) * 100000
        vypocet_rovnobezek()
elif zobrazeni == 'B':
    for u in range(-90, 100, 10):
        rovnobezka1 = 2*R*tan(radians(u/2)) * 100000
        vypocet_rovnobezek()
elif zobrazeni == 'M':
    for u in range(-80, 90, 10):
        rovnobezka1 = R*log(1/tan(radians(90-u)/2), e) * 100000
        vypocet_rovnobezek()

print("Poledniky:", result)
print("Rovnobezky:", result1)

# vypocet souradnic za 2 b

zs = float
zd = float
while zs != 0 and zd != 0:  # podmínka, kdy ukončit program (ptaní se na další vstup)
    zs = float(input("Zadej zem. šířku ve formátu stupňů (př. 48,325°)"))
    if zs > 90 or zs < -90:
        print("Zeměpisná šířka musí být v rozsahu +- 90°")  # ošetřené nekoretní zem. šířky
        quit()
    zd = float(input("Zadej zem. délku ve formátu stupňů (př. 52,212°)"))
    if zd > 180 or zd < -180:
        print("Zeměpisná délka musí být v rozsahu +-180°")  # ošetřené nekoretní zem. délky
        quit()

    polednik2b = R * radians(zd) * 100000  # vypočet stejný jako ve funkci vypocet_poledniku,
    # pouze změněný vstupní úhel změněný taky výstup -> pouze jedna hodnota, ne seznam
    polednik2b_1 = polednik2b / x
    polednik2b_2 = round(polednik2b_1, 1)
    if zobrazeni == 'L':  # opět ošetření rovnoběžek více podmínkami kvůli rozdílným vzorcům
        rovnobezka2b = R*sin(radians(zs)) * 100000
    if zobrazeni == 'A':
        rovnobezka2b = R * radians(zs) * 100000
    if zobrazeni == 'B':
        rovnobezka2b = 2 * R * tan(radians(zs / 2)) * 100000
    if zobrazeni == 'M':
        rovnobezka2b = R * log(1/tan(radians(90-zs) / 2), e) * 100000
    rovnobezka2b_1 = rovnobezka2b / x
    rovnobezka2b_2 = round(rovnobezka2b_1, 1)

    print(rovnobezka2b_2)  # výsledná hodnota souřadnice
    print(polednik2b_2)