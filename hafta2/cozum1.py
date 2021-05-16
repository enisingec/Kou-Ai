liste = []
dosya = open("odev.txt", "r")
dosya1 = open("sonuc1.txt","w")
for i in dosya.readlines():
    temiz=""
    for a in i:
        if a.isalpha():
            temiz += a
    liste.append(temiz)
for i in liste:
    dosya1.writelines(i+"\n")
dosya1.close()
dosya.close()