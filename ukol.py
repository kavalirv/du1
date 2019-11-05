from math import sin, tan, cos, log
L = str  # Lambert
A = str  # Marin
B = str  # Braun
M = str  # Mercator
R = float(6371.11)
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
    for v in range(-180, 180, 10):
        Poledniky1 = R*v
        result.append(float(Poledniky1))
    for u in range(-90, 90, 10):
        Rovnobezky1 = R*sin(u)
        result1.append(float(Rovnobezky1))
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
        Rovnobezky1 = R*log(w, e)
else:
    print("Zadej správné zobrazení")
x = float(input("Zadej měřítko"))
Rovnobezky = Rovnobezky1 / x
Poledniky = Poledniky1 / x
print(result)
print(result1)
