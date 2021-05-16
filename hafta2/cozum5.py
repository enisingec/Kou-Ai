s = {63: None, 45: None, 61: None, 40: None, 41: None, 43: None, 49: None, 50: None, 51: None, 52: None,53: None, 54: None, 55: None, 56: None, 57: None}
with open("sonuc5.txt","w") as w:
    with open("odev.txt", "r") as r:
        for i in r.readlines():
            w.writelines(i.translate(s))