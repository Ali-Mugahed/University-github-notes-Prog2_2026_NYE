szamok = [7, -13, -31, -90, 94, 21, -38.15, 104, 13, 21.4, 36, 15, -31, -2.66, 7, -6, 23.45, 147, 0, 33, 149, 150, -70, -95, -60, 78]

poz_db =0
for i in szamok:
    if i > 0:
        poz_db += 1
print(poz_db)

print(len(szamok))

print(sum(szamok))

nem_int = 0
for i in szamok:
    if int(i) != i:
        nem_int += 1
print(nem_int)

print(szamok[1])
print(szamok[::2])

print(szamok.count(7))

szamok.append(20.5)
print(szamok)

print(szamok.index(0))

paros_db = 0
paratlan_db = 0
for i in szamok:
    if i % 2 == 0:
        paros_db += 1
    if i % 2 == 1:
        paratlan_db += 1
print(paros_db, paratlan_db)

print(min(szamok))
print(max(szamok))
