from math import sin, tan, log, radians, e
result = []  # výsledný seznam poledníků
result1 = []  # výsledný seznam rovnoběžek
def vypocet_poledniku():
    for v in range(-180, 190, 10):
        Poledniky1 = R * radians(v)  # poledniky po vypoctu
        Poledniky2 = Poledniky1 / x  # vydeleno meritkem
        if Poledniky2 >100 or Poledniky2 < -100:
            result.append("-")
        else:
            Poledniky3 = round(Poledniky2, 1)  # zaokrouhleni na milimetry
            result.append(float(Poledniky3))  # vysledek vydeleny meritkem add to seznam
def vypocet_rovnobezek():
    Rovnobezky2 = Rovnobezky1 / x
    if Rovnobezky2 > 100 or Rovnobezky2 < -100:
        result1.append("-")
    else:
        Rovnobezky3 = round(Rovnobezky2, 1)
        result1.append(float(Rovnobezky3))
zobrazeni = str(input("Zadej typ zobrazení"))
if zobrazeni != 'L' and zobrazeni != 'M' and zobrazeni != 'B' and zobrazeni != 'A':
    print("Zadej správné zobrazení")
    quit()
x = float(input("Zadej měřítko"))
if x <=0:
    print("Zadej měřítko větší než 0")
    quit()
R= float(input("Zadej poloměr Země v cm"))  # libovolný poloměr Země v cm
if R == 0:
    R=637111000
elif R <0:
    print ("Zadej kladný poloměr Země v cm")
    quit()

if zobrazeni == 'L':
    vypocet_poledniku()
    for u in range(-90, 100, 10):
        Rovnobezky1 = R*sin(radians(u))
        vypocet_rovnobezek()
elif zobrazeni == 'A':
    vypocet_poledniku()
    for u in range(-90, 100, 10):
        Rovnobezky1 = R*radians(u)
        vypocet_rovnobezek()
elif zobrazeni == 'B':
    vypocet_poledniku()
    for u in range(-90, 100, 10):
        Rovnobezky1 = 2*R*tan(radians(u/2))
        vypocet_rovnobezek()
elif zobrazeni == 'M':
    vypocet_poledniku()
    for u in range(-80, 90, 10):
        Rovnobezky1 = R*log(1/tan(radians(90-u)/2), e)
        vypocet_rovnobezek()
else:
    print("Zadej správné zobrazení")
print("Poledniky:", result)
print("Rovnobezky:", result1)
# vypocet souradnic za 2 b
zs = float
zd = float
while zs != 0 and zd != 0:
    zs = float(input("Zadej zem. šířku ve formátu stupňů (př. 48,325°)"))
    if zs > 90 or zs < -90:
        print("Zeměpisná šířka musí být v rozsahu +- 90°")
        quit()
    zd = float(input("Zadej zem. délku ve formátu stupňů (př. 52,212°)"))
    if zd > 180 or zd < -180:
        print("Zeměpisná délka musí být v rozsahu +-180°")
        quit()
    Poledniky2b = R * radians(zd)  # poledniky po vypoctu
    Poledniky2b_1 = Poledniky2b / x  # vydeleno meritkem
    Poledniky2b_2 = round(Poledniky2b_1, 1)  # zaokrouhleni na milimetry
    if zobrazeni == 'L':
        Rovnobezky2b = R*sin(radians(zs))
    if zobrazeni == 'A':
        Rovnobezky2b = R * radians(zs)
    if zobrazeni == 'B':
        Rovnobezky2b = 2 * R * tan(radians(zs / 2))
    if zobrazeni == 'M':
        Rovnobezky2b = R * log(1/tan(radians(90-zs) / 2), e)
    Rovnobezky2b_1 = Rovnobezky2b / x
    Rovnobezky2b_2 = round(Rovnobezky2b_1, 1)
    print(Rovnobezky2b_2)
    print(Poledniky2b_2)
