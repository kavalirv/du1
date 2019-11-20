# Zadání

- vypočítat souřadnice rovnoběžek a poledníků pro konkrétní zobrazení
- ošetřit nekoretní vstupy
- zeptat se uživatele na typ zobrazení a měřítko

## Postup

- definovali jsme si novou funkci *'vypocet_poledniku'*
	- kde pomocí `for in range` cyklu nadefinujeme, že chceme od -180° do 180°
	 (musíme napsat 190 či 181, protože cyklu bere poslední hodnotu kromě) a že chceme po 10°
	- následně jsme zadali vzorec podle kterého má postupovat (pro všechny zobrazení stejný)
	- vydělili měřítkem, ošetřili vzdálenosti nad 1 m, zaokrouhlili a přidali do seznamu výslednou hodnotu

- definovali jsme funkci *'vypocet_rovnobezek'* 
	- postup stejný jako u poledníku až na to, že mají zobrazení rozdílný vzorec
- to ošetřeno `if` podmínkami 
	- řádky 43 až 58
	-> vždy po zadání zobrazení proveden vzorec pro zobrazení a poté funkce *'vypocet_rovnobezek'*
- Mercator ošetřen u rovnoběžek pro hodnoty od -80° do 80° 
	- na 90° není definován
- měřítko ošetřeno pro vstupy menší nebo rovno nule -> konec programu (řádky 29 až 32)
- nakonec pomocí funkce print vyvolány výsledné seznamy - `print("Poledniky:", result)`

#### Libovolný poloměr

- na řádku 34 až 39
- R - poloměr Země ošetřen pro vstup od uživatele menší než nula -> konec programu a pro hodnotu '0', kdy bere v úvahu základní hodnotu R = 6371,11 km

#### Výpočet souřadnic za 2 b

- řádky 65 až 93
- pro vypocet souradnic zvolené délky a šířky užit `while` cyklus, který běží dokud není ZD i ZS = 0
- Uživatel zadá ZS a ZD, opět ošetřeny nekorentí vstupy typu: ZD= 220° apod.
- poté výpočet poledníků a rovnoběžek shodný podle vzorců z původního programu, rozdíl v tom, že výsledek je pouze jedna hodnota, nikoliv seznam
- také vstupem je zadaná jedna hodnota pro ZS a ZD a ne hodnoty od -180 do 180, respektive -90 do 90
- mezi hodnoty ukládány do proměnných s koncovkou 2b_x (2b, že se vztahují k této části úkolu, indexy x značí to samé co indexy 1,2,3 u původního programu)

#### Funkčnost programu

- Program se uživatele zeptá na zobrazení a měřítko, případně libovolný poloměr Země
	- při nekorektní vstupech - chybová hláška a konec programu
	- při korektní vstupech provede část **'Postup'**

- Následně se zeptá na zem. délku a šířku pro výpočet souřadnic podle části *'Výpočet souřadnic za 2b'*
	- při nekorektní vstupu - chybová hláška a konec programu
	- při zadání zem. délky i šířky hodnotou '0' se program ukončí
	- při zadání korektních hodnot vyvolá přepočtené hodnoty souřadnic a ptá se znovu na zem. délku a šířku
