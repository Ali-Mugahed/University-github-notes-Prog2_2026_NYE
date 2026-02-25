"""
Halmaz = set = összetett adattípus
- nincs ismétlődő elem
- elemnek nincs indexe (helye)
- elemek nem sorbarendezhetők (növekvő vagy csökkenő)
megadási módok:
- A = set() (üres halmaz) 
- B = {..., elemek, ...} , így nem adunk meg üres halmazt (B = {} nem jó)"""

#halmaz függvényei:
gyumolcs = {"alma", "körte", "barack", "dinnye", "cseresznye", "meggy", "banán"}
print(len(gyumolcs)) #elemek száma
szamok = {1, 4, 5, 66, -2.5}
print(type(szamok)) #adat típusa
print(min(szamok)) #legkisebb elem
print(max(szamok)) #legnagyobb elem
print(sum(szamok)) #elemek összege
print(sorted(szamok)) #sorbarendezett listát ad
print(sorted(gyumolcs))

#halmaz metódusai (tagfüggvények):
gyumolcs.add("dió") #új elem hozzáadása
print(gyumolcs)
gyumolcs.add("meggy")
print(gyumolcs)
gyumolcs.remove("barack") #elem eltávolítása (csak létező elem)
print(gyumolcs)
#gyumolcs.remove("málna")
gyumolcs.discard("málna") #elem eltávolítása (nem csak létező elem)
print(gyumolcs)
#halmazműveletek:
gyumolcs2 = {"banán", "narancs", "ananász", "kókusz"}
print(gyumolcs.union(gyumolcs2)) #halmazok egyesítése = uniója
print(gyumolcs | gyumolcs2) #halmazok egyesítése jele
print(gyumolcs - gyumolcs2) #halmazok különbsége jele (.difference() )
print(gyumolcs.intersection(gyumolcs2)) #halmazok metszete
print(gyumolcs & gyumolcs2) #halmazok metszete jele
print(gyumolcs.symmetric_difference(gyumolcs2)) #halmazok szimmetrikus különbsége
print(gyumolcs ^ gyumolcs2) #halmazok szimmetrikus különbsége jele

"""
Adott egy halmaz, mely tartalmazza a számokat 1-től 20-ig.
Írjon kódot, mely eltávolítja a páros számokat.
"""
A = set()
for i in range(1, 21):
    A.add(i)
print(A)
A_list = list(A)
for i in A_list: #0-tól 19-ig
    if i % 2 == 0:
        A_list.remove(i)
print(A_list)















