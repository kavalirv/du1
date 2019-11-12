from math import sin, tan, cos, log, atan, radians
L = str  # Lambert
A = str  # Marin
B = str  # Braun
M = str  # Mercator
R = float(637111000)  # v cm poloměr Země
v = int  # zem.délka
u = int  # zem.šířka
e = float(2.71828)
Poledniky1 = float
Rovnobezky1 = float
Poledniky = float
Rovnobezky = float
result = []
result1 = []
zobrazeni = str(input("Zadej typ zobrazení"))
if zobrazeni == 'L':
    x = float(input("Zadej měřítko"))
    for v in range(-180, 180, 10):
        Poledniky1 = R*radians(v)  # poledniky po vypoctu
        Poledniky2 = Poledniky1 / x  # vydeleno meritkem
        Poledniky3 = round(Poledniky2)  # zaokrouhleni na milimetry
        result.append(float(Poledniky3))  # vysledek vydeleny meritkem add to seznam
    for u in range(-90, 90, 10):
        Rovnobezky1 = R*sin(radians(u))
        Rovnobezky2 = Rovnobezky1 / x
        Rovnobezky3 = round(Rovnobezky2)
        result1.append(float(Rovnobezky3))
elif zobrazeni == 'A':
    for v in range(-180, 180, 10):
        Poledniky1 = R*v
    for u in range(-90, 90, 10):
        Rovnobezky1 = R*u
elif zobrazeni == 'B':
    for v in range(-180, 180, 10):
        Poledniky1 = R*v
    for u in range(-90, 90, 10):
        Rovnobezky1 = 2*R*tan(u/2)
elif zobrazeni == 'M':
    for v in range(-180, 180, 10):
        Poledniky1 = R*v
    for u in range(-90, 90, 10):
        Rovnobezky1 = R*log(atan(u/2), e)
else:
    print("Zadej správné zobrazení")
print(result)
print(result1)
