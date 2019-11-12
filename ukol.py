from math import sin, tan, log, atan, radians, e
L = str  # Lambert
A = str  # Marin
B = str  # Braun
M = str  # Mercator
R = float(637111000)  # v cm poloměr Země
v = int  # zem.délka
u = int  # zem.šířka
Poledniky1 = float
Rovnobezky1 = float
Poledniky = float
Rovnobezky = float
result = []  # výsledný seznam poledníků
result1 = []  # výsledný seznam rovnoběžek
def vypocet_poledniku():
    for v in range(-180, 190, 10):
        Poledniky1 = R * radians(v)  # poledniky po vypoctu
        Poledniky2 = Poledniky1 / x  # vydeleno meritkem
        Poledniky3 = round(Poledniky2, 1)  # zaokrouhleni na milimetry
        result.append(float(Poledniky3))  # vysledek vydeleny meritkem add to seznam
def vypocet_rovnobezek():
    Rovnobezky2 = Rovnobezky1 / x
    Rovnobezky3 = round(Rovnobezky2, 1)
    result1.append(float(Rovnobezky3))
zobrazeni = str(input("Zadej typ zobrazení"))
x = float(input("Zadej měřítko"))

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
    for u in range(0, 90, 10):
        Rovnobezky1 = R*log(atan(u/2), e)
        vypocet_rovnobezek()
else:
    print("Zadej správné zobrazení")
print("Poledniky:", result)
print("Rovnobezky:", result1)
