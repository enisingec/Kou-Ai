dosya = open("odev.txt", "r+")
dosya1 = open("sonuc3.txt","w")
for i in dosya.readlines():
    for a in i:
        if not a.isalpha():
            i =i.replace(a,"")
    dosya1.writelines(i+"\n")