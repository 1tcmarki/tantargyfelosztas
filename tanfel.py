"""
1. feladat
Olvassa be és tárolja el a beosztas.txt állományban talált adatokat, és annak
felhasználásával oldja meg a következő feladatokat! 
""" 
beosztas={}
beosztasok=[]
segedlista=[]

with open("beosztas.txt","r",encoding="utf-8") as fin:
    for sor in fin:
        segedlista.append(sor.strip())
        if len(segedlista)==4:


            beosztas["tanar"]=segedlista[0]
            beosztas["tantargy"]=segedlista[1]
            beosztas["osztaly"]=segedlista[2]
            beosztas["oraszam"]=int(segedlista[3])
            beosztasok.append(beosztas)
            segedlista=[]
            beosztas={}

"""
2. feladat
Hány bejegyzés található az állományban? Az eredményt írassa ki a képernyőre! 
"""
print("2. feladat")
print(f"A fájlban {len(beosztasok)} bejegyzés van.")

"""
3. feladat
Mennyi a heti osszoraszam az iskolaban? Az eredmenyt irassa ki a kepernyore!
"""
print("3. feladat")


def osszegezes(bok):
    osszeg=0
    for elem in bok:
        osszeg+=elem["oraszam"]
    return osszeg

print(f"Az iskolában a heti összóraszám: {osszegezes(beosztasok)}")

"""
4. feladat
Kérje be a felhasználótól egy tanár nevét, és írassa ki a képernyőre, hogy hetente hány
órában tanít!
"""
be_tanarnev=input("Egy tanar neve= ") or "Albatrosz Aladin"
def tanar_oraszamanak_osszegzese(bok,be_nev):
    osszeg=0
    for elem in bok:
        if be_nev==elem["tanar"]:
            osszeg+=elem["oraszam"]
    return osszeg
print(f"A tanar heti oraszama: {tanar_oraszamanak_osszegzese(beosztasok,be_tanarnev)}")

"""
5. feladat
Készítse el az of.txt fájlt, amely az osztályfőnökök nevét tartalmazza osztályonként
az alábbi formában (az osztályok megjelenítésének sorrendje a mintától eltérhet):

9.a - Albatrosz Aladin
9.b - Hangya Hanna
9.c - Zerge Zenina
KIVALOGATAS
…
"""
with open("of.txt","w",encoding="utf-8") as fout:
    for elem in beosztasok:
        if elem["tantargy"]=="osztalyfonoki":
            print(f"{elem['osztaly']} - {elem['tanar']}", file=fout)

"""
6. feladat
Egyes osztályokban bizonyos tantárgyakat a tanulók csoportbontásban tanulnak: ekkor az
adott tantárgyra és osztályra két bejegyzést is tartalmaz a tantárgyfelosztás. Kérje be egy
osztály azonosítóját, valamint egy tantárgy nevét, és írassa ki a képernyőre, hogy az adott
osztály a megadott tantárgyat csoportbontásban vagy osztályszinten tanulja-e!
(Feltételezheti, hogy a megadott osztály tanulja a megadott tantárgyat.) 
"""

print("6. feladat")
be_osztaly=input("Osztaly= ") or "10.b"
be_tantargy=input("Tantargy= ") or "kemia"

def csoportban_tanuljak(beo,be_o,be_t):
    i=0
    while i<len(beo) and not(beo[i]["osztaly"]==be_o):
        i+=1
    return not(i<len(beo))

if csoportban_tanuljak(beosztasok,be_osztaly, be_tantargy):
    print("Csoportban tanuljak.")
else:
    print("Osztalyszinten tanuljak.")

# index=0
# while index<len(beosztasok) and not(beosztasok[index]["osztaly"]==be_osztaly and beosztasok[index]["tantargy"]==be_tantargy):
#     index+=1

# 7. feladat
# A fenntartó számára az is fontos információ, hogy hány tanár dolgozik az iskolában. Írassa
# ki ezt az adatot a képernyőre!

print("7.feladat")
