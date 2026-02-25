szamok = [7, 17, 27, 41, -5, -98, 11.5, 10, 7, 7, 4.25, -5.5, 16, -55, 44, 13, 23, 31, 0, 155]
#elemek darabszأ،ma
print(len(szamok))
#legkisebb szأ،m
print(min(szamok))
#legnagyobb szأ،m
print(max(szamok))
#elsإ‘ elem
print(szamok[0])
#utolsأ³ elem
print(szamok[-1])
#utolsأ³ elإ‘tti elem
print(szamok[-2])
#elemek (szأ،mok) أ¶sszege
print(sum(szamok))

#hأ،ny pozitأ­v szأ،m van
poz_db = 0
for i in szamok: #bejأ،rjuk a listأ،t = vأ©gig megyأ¼nk a listأ،n = megnأ©zأ¼nk minden elemet
    if i > 0:
        poz_db += 1 #poz_db = poz_db + 1 (nإ‘ 1-el)
print(poz_db)

#hأ،ny egأ©sz szأ،m van
int_db = 0
for i in szamok:
    if int(i ) == i:
        int_db += 1
print(int_db)

#hأ،ny pأ،ros أ©s hأ،ny pأ،ratlan szأ،m van
paros_db = 0
paratl_db = 0
for i in szamok:
    if i % 2 == 0:
        paros_db += 1
    elif i % 2 == 1:
        paratl_db += 1
        
print(paros_db)
#vagy B megoldأ،s: paratl_db = int_db - paros_db
print(paratl_db)






















