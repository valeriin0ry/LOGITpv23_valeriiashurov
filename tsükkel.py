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

#print("***arvumäng***")  # Pealkiri

#print()
#while True:
#    try:
#        a = abs(int(input("Sisestage täisarv: ")))  # Päring täisarvu sisestamiseks
#        break  # Tsükli katkestamine
#    except ValueError:
#         print("See ei ole täisarv")  # Teade vea kohta, kui sisestatakse mitte-täisarv

#if a == 0:
#    print("Nulliga pole mõtet midagi ette võtta")  # Kui sisestatakse null
#else:
#    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")  # Ülesanne
#    print()

#    b = a
#    paaris = 0
#    paaritu = 0
#    while b > 0:
#        if b % 2 == 0:
#            paaris += 1  # Paarisarvud arvus
#        else:
#            paaritu += 1  # Paaritud arvud arvus
#        b = b // 10

#    print("Paarisarvud:", paaris)  # Paarisarvude väljund
#    print("Paaritud arvud:", paaritu)  # Paaritud arvude väljund
#    print()
#    print("*Pöörame* sisestatud arvu ümber")  # Pööramise algus
#    print()
#    b = 0
#    while a > 0:
#        number = a % 10
#        a = a // 10
#        b = b * 10
#        b += number  # Arvu pööramine
#    print("*Pööratud* arv", b)  # Pööratud arvu väljund
#    print()
#    print("Kontrollime Collatzi hüpoteesi") 
#    print()
#    c = a 
#    if c % 2 == 0:
#        print("c on paarisarv. Jagame kahega.")  
#    else:
#        print("c on paaritu arv. Korrutame kolmega, liidame ühe ja jagame kahega.") 
#        if c % 2 == 0:
#            c = c / 2
#        else:
#            c = (3 * c + 1) / 2
#        print(c, end=" ")  # Järjestuse väljund
#    print()
#    print("Hüpotees on tõene")  # Teade hüpoteesi tõesuse kohta



#1

#n = int(input("Sisestage arv vahemikus 1 kuni 9: ")) #numbri sisestamine

#if 1 <= n <= 9:  #numbri kontroll
#    for i in range(n):
#        print("")
#        print("   /V\    ")
#        print("  / V \   ")
#        print(" / V V \  ")
#        print("/VV V VV\  ")
#        print("")
#else:
#    print("Arv peab olema vahemikus 1 kuni 9") #veateade, kui number on vale

##2

#R = int(input("Sisestage arv: "))
#arv = 1 #muutuja määramine
#for i in range(1, R + 1,2):  #paarituid numbreid 1 kuni R sammuga
#    arv *= i #arvude korrutis
#print("Paaritud от 1 до", R,arv) #tulemus

##3 #не знаю как реализовать через цикл


##4
#n = input("Sisestage arv: ")
#paaris = ("") 
#paaritud = ("")   #muutujate lisamine

#for arv in n:
#    if int(arv) % 2 == 0:   #täisarvu test, tagastab jagamise jäägi
#        paaris += arv + " "
#    else:
#        paaritud += arv + " "  #kui number on paaritu

#print(f"Paaris: {paaris}")
#print(f"Paaritud: {paaritud}")



##5

#A = int(input("Введите A: "))
#B = int(input("Введите B: "))

#summa = 0 #muutuja lisamine lahendamiseks tsükli kaudu
#for i in range(A, B + 1): #lahendus muutuva loendusega tsükli kaudu
#    summa += i
#print("Arvude summa on:", summa)


#исправление 18 задача
from random import *
N = randint(1, 10)
M = randint(1, 10)
stepen = [2, 3]
for i in stepen:
    ck_N = N ** i
    ck_M = M ** i
    print(f"N = {N}, M = {M}, N^{i} = {ck_N}, M^{i} = {ck_M}")

