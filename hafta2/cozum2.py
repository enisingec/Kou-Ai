dosya = open("odev.txt", "r")
dosya1 = open("sonuc2.txt", "w")
for i in dosya.readlines():
    temiz=""
    for a in i:
        if a.isalpha():
            temiz += a
    dosya1.writelines(temiz+"\n")
dosya1.close()
dosya.close()