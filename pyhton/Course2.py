szamok = {7, -13, -21, -90, 94, 21, -38.15, 104, 13, 21.4, 36, 15, -31, -2.66, 8}
#számok összege
print(f"Számok összege: {sum(szamok)}")
#számok összege egészre kerekítve
print(f"Számok összege: {round(sum(szamok), 0)}") #matematikai kerekítés
print(f"Számok összege: {int(sum(szamok))}") #csak egész rész
#számok átlaga (=összeg/darabszám)
print(f"Számok átlaga: {sum(szamok)/len(szamok)}")
#hány pozitív (>0) szám és hány negatív (<0) szám
poz_db = 0
neg_db = 0
for i in szamok:
    if i > 0:
        poz_db += 1 #poz_db = poz_db + 1
    elif i < 0:
        neg_db += 1
print(f"{poz_db} pozitív szám, {neg_db} negatív szám van.")
#új halmazba minden elem abszolút értékét
Abs = set()
for i in szamok:
    Abs.add(abs(i))
print(f"Abs halmaz: {Abs}")
#2 új halmazba: csak páros/páratlan számokat (!!! csak egész szám jó)
paros = set()
paratlan = set()
##for i in szamok:
##    if i == int(i) and i % 2 == 0:
##        paros.add(i)
##    elif i == int(i) and i % 2 != 0:
##        paratlan.add(i)
for i in szamok:
    if i == int(i):
        if i % 2 == 0:
            paros.add(i)
        else:
            paratlan.add(i)
print(f"Páros számok halmaza: {paros}")
print(f"Páratlan számok halmaza: {paratlan}")
#új listába minden szám négyzetét, 2 tizedesre kerekítve
negyzet = []
for i in szamok:
    negyzet.append(round(i ** 2, 2))
print(f"A négyzet lista: {negyzet}")












    



        
