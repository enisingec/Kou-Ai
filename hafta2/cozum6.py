def temizle(x):
    new =""
    for i in x:
        if i.isalpha():
            new +=i
    return new

with open("odev.txt","r") as readFile:
    readRows = readFile.readlines()

with open("sonuc6.txt","w") as writeFile:
    for i in readRows:
        writeFile.writelines(temizle(i) + "\n")