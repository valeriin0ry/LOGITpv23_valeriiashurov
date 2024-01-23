from datetime import *
from random import *
##Komm
#while True:
#    v=input("Tahan komme!").lower()
#    if v=="komm": break

#print("2. variandt -while tingimusega-")
#v=""
#while v!="komm":
#    v=input("Tahan komme!").lower()








#Nädala päev
#paevad=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]
#tunnid=["8 tundi","9 tundi","5 tundi","8 tundi","8 tundi", "tunde pole", "tunde pole"]
#for i in range(7):
#    print(paevad[i]+"-"+tunnid[i])

#prak
#nimi=(input("Sisesta nimi: "))
#korda=int(input("Mitu kordas: "))
#for i in range (korda):
#    print("Tere,"+nimi)





#nimi=input("Mis on sinu nimi?")
#mitu=int(input("Mitu korda tervitada?"))
#for i in range(1,mitu+1):
#print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")

##2 summa 10 arvud
#summa = 0
#for i in range(10):
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#print(summa)

#summa=0
#i=0
#while True:
#    i+=1
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#    if i==10: break
#print(summa)


#3
#k=0
#while True:
#    k+=1
#    a=randint(1,50)
#    b=randint(1,50)
#    p=0
#    v=-1000
#    while p!=3:
#        p+=1
#        v=int(input("Millega võrdub {0}+{1}= ".format(a,b)))
#        if v==a+b:
#            print("Tubli!")
#            break
#        else:
#            print("Mõtle veel!")
#    print("{0}+{1}={2}".format(a,b,a+b))

#    if k==5:break

    #Таблица умножения на 5 (9)
    #from random import *
    #from datetime import *
    
    #korrutamine=["5"]
    #arv:["1","2","3","4","5","6","7","8","9","10"]
    #for i in range(10):
    #    tulemus = int(arv[i]) * 5
    #    print(f"{arv[i]} * 5 = {tulemus}")


    #15
#katsed = 0
#while True:
#    vastus = input("Osta elevant ära! Kirjuta 'elevant': ")
#    katsed += 1

#    if vastus.lower() == 'elevant':
#        print(f"Õige! Ostsid elevanti ära {katsed} katsega.")
#        break
#    else:
#        print("Vale vastus. Proovi uuesti.")

#    #7
#    from random import *
#    for i in range(5):
#        number=randint(0,9)
#        print(number, end="")
#    print()

#8
#paaris=0
#paaritu=0
#for i in range(1,101):
#    if i%2==0:
#        print(f"{i}-paaris")
#        paaris+=1
#    else:
#        print(f"{i}-paaritu")
#        paaritu+=1

#print(f"Paarisarvude arv: {paaris}")
#print(f"Paaritute arvude arv: {paaritu}")

#kakaya to zada4a
#from random import *
#number=randint(1,100)
#katsed=3
#while katsed>0:
#    külaline=int(input("Угадайте число от 1 до 100: "))
#    if külaline == number:
#        print("Поздравляю, вы угадали число!")
#        break
#    else:
#        katsed -= 1
#        print(f"Неверно. У вас осталось {katsed} попыток.")
#        if katsed == 0:
#            print(f"Извините, вы использовали все попытки. Загаданное число было {number}")
#            veelkord = input("Хотите ли вы угадать?: ").lower()
#            if veelkord.lower()=="нет":
#                break
#            else:
#                katsed=3



    #13
print("Arv Ruut Kuup")
print()
print("-------------")
print()

for i in range(1, 11):
    ruut = i ** 2
    kuup = i ** 3
    print(f"{i:2}  {ruut:2}  {kuup:3}")














#arve_nr=datetime.now() #date.today()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0
#tooded=["Piim","Leib","Komm"] #index 0-1-2
#for i in range(3): #(0,3,1) = 1 число 0, 2 - 3, 3 - 1 #i=0, i=1, i=2
#    toode=tooded[i]
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
#    if v=="jah":
#        mitu=int(input("Mitu?"))
#        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#        summa+=mitu*hind

#tsekk+="Kokku maskta: "+str(summa)
#print(tsekk)
