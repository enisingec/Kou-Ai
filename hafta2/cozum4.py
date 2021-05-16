with open("sonuc4.txt","w") as w:
    with open("odev.txt", "r") as f:
        for i in f.readlines():
            for a in i :
                if not (a.isalpha()):i = i.replace(a,"")
            w.writelines(i+"\n")

