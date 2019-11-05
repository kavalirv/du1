from math import sin, tan, cos, log
L=str #Lambert
A=str #Marin
B=str #Braun
M=str #Mercator
R=float(6371.11)
v=float # zem.délka
u=float # zem.šířka
e=float(2.71828)
w = float(cos(u/2)/sin(u/2))  # cotanges pro Mercatora
Poledniky1=float
Rovnobezky1=float
zobrazeni=input("Zadej typ zobrazení")
if zobrazeni=='L':
    for v in range(-180,180,10):
        Poledniky1=R*v
    for u in range(-90,90,10):
        Rovnobezky1=R*sin(u)
elif zobrazeni=='A':
    for v in range(-180, 180, 10):
        Poledniky1=R*v
    for u in range(-90,90,10):
        Rovnobezky1=R*u
elif zobrazeni=='B':
    for v in range(-180,180,10):
        Poledniky1=R*v
    for u in range(-90,90,10):
        Rovnobezky1=2*R*tan(u/2)
elif zobrazeni=='M':
    for v in range(-180, 180, 10):
        Poledniky1=R*v
    for u in range(-90, 90, 10):
        Rovnobezky1=R*math.log(w,e)
else:
    print("Zadej správné zobrazení")
x=input("Zadej měřítko")
Rovnobezky=Rovnobezky1/x
Poledniky=Poledniky1/x
print(Rovnobezky)
print(Poledniky)


