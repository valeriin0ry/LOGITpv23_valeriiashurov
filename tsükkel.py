from datetime import *
from random import *
#13 tsükkel
#algsumma=float(input("Mis summa paneme panka?"))
#alg=lõppsumma=algsumma
#intress=randint(1,10)
#print(f"Paned panka summa, mis võrdub {algsumma}. Intress on {intress}")
#aastad=int(input("Mitmeks aastaks"))
#print("Aasta Algsumma Intress Aasta_lõpuks")
#for i in range(1,aastad+1):
#    intsumma=(algsumma*intress)/100
#    lõppsumma=algsumma+intsumma
#    print(f"{i} {algsumma} {intsumma} {lõppsumma}")
#    aglsumma=lõppsumma
#print(f"Summa kokku: {lõppsumma} Eur")
#print(f"Kasum: {lõppsumma-alg} Eur")


#14
#for j in range(1,11):
#    for i in range(1,11):
#        print(f"{j*i:4}",end=" ")
#    print()

print("***arvumäng***")
print()
while True:
    try:
        a = abs(int(input("Sisestage täisarv: ")))
        break
    except ValueError:
         print("See ei ole täisarv")

if a == 0:
    print("Nulliga pole mõtet midagi ette võtta")
else:
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()

    b = a
    paaris = 0
    paaritu = 0
    while b > 0:
        if b % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        b = b // 10

    print("Paarisarvud:", paaris)
    print("Paaritud arvud:", paaritu)
    print()
    print("*Pöörame* sisestatud arvu ümber")
    print()
    b = 0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Pööratud* arv", b)
    print()
    print("Kontrollime Collatzi hüpoteesi")
    print()
    c = a 
    if c % 2 == 0:
        print("c on paarisarv. Jagame kahega.")
    else:
        print("c on paaritu arv. Korrutame kolmega, liidame ühe ja jagame kahega.")
    while c != 1:
        if c % 2 == 0:
            c = c / 2
        else:
            c = (3 * c + 1) / 2
        print(c, end=" ")
    print()
    print("Hüpotees on tõene")





    