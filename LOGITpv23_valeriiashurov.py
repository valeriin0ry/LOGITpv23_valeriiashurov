#3
from math import *
from random import *
from sunau import AUDIO_FILE_ENCODING_ADPCM_G721, AUDIO_FILE_ENCODING_ADPCM_G722
from xml.etree.ElementTree import PI
#kokku=randint(1,666)
#print("Laual peal on",kokku,"kommid. Mitu tahad süüa?")
#kommid=int(input())
#kokku-=kommid 
#print("Nüüd kokku on",kokku)


#2

#arv1=float(input("Arv1: "))
#t=input("Tehe: ")
#arv2=float(input("Arv2: "))
#vastus=eval(str(arv1)+t+str(arv2))
#print(str(arv1)+t+str(arv2)+"="+str(vastus))
#print(arv1,t,arv2,"=",vastus,sep="") #separator - razdelitel'
#print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))







#1

#print("Tere maailm!".center(75,"-"))
#nimi=input("Mis on sinu nimi?").capitalize() #python->Python
#print("Tere "+nimi+"!")
#print("Tere",nimi+"!")
#print("Tere {0}!".format(nimi))
#vanus=int(input("Kui vana sa oled?"))               #"21" !=21
#print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja nimi=",nimi,type(nimi))
#print("Muutuja vanus=",vanus,type(vanus))




#vanus=18
#eesnimi="Jaak"
#pikkus=16.5
#kas_käib_koolis=True

#print("Muutuja vanus=",vanus,"on",type(vanus))
#print("Muutuja eesnimi=",eesnimi,"on",type(eesnimi))
#print("Muutuja pikkus=",pikkus,"on",type(pikkus))




#4

#u=float(input("Ümbermõõt: ")) #L=pi*2*r=pi*d
#d=round(u/pi,2) 
#print("Läbimõõt =",d)

#5

from math import *
#a=float(input("pikkus: "))
#b=float(input("laius: "))
#d=sqrt(a**2+b**2)
#print("Diagonaal=",d,"m")



#6
try:
    aeg = float(input("Mitu tundi kulus sõiduks: "))
    try:
        teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
        kiirus = teepikkus/aeg 
        print("Sinu kiirus oli "+str(kiirus) + "km/h")
    except:
        print("Viga andmetaga")
except:
    print("On vaja ainult ")


#7

#num1 = int(input("Введите первое целое число"))
#num2 = int(input("Введите второе целое число"))
#num3 = int(input("Введите третье целое число"))
#num4 = int(input("Введите четвертое целое число"))
#num5 = int(input("Введите пятое целое число"))

#average = (num1 + num2 + num3 + num4 + num5) / 5
#print("Среднее арифметическое число: ", average)

#7 (2 variant)

try: 
    min_=int(input("Min: "))
except:
    print("On vaja täisarv kasutada!")
try:
    max_=int(input("Max: "))
except:
    print("Viga max_ muutujaga!")

a1=randint(min_,max_)
a2=randint(min_,max_)
a3=randint(min_,max_)
a4=randint(min_,max_)
a5=randint(min_,max_)
print("Arvud: {0},{1},{2},{3},{4}. Aritmetiline keskmine on: {5}".format(a1,a2,a3,a4,a5,keskmine))

#8

print("@..@".center(10," "))
print("(----)".center(10," "))
print(" \__/ ").center(10," ")
print('^^ \"\" ^^').center(10," ")

#9

a = int(input("Sisesta esimese külje pikkus: "))
b = int(input("Sisesta teise külje pikkus: "))
c = int(input("Sisesta kolmanda külje pikkus: "))
umbermoot = a + b + c
print(a+b+c)

#10
pizza_cost: 12.90
tip_percentage = 10

num_people = int(input("Kui palju inimesi tellib pitsat: "))

tip_amount = pizza_cost * (tip_percentage / 100)
total_cost = pizza_cost + tip_amount
cost_per_person = total_cost / num_people

print("\nPitsa hind: "), pizza_cost, "euro"
print("tip",tip_percentage, "%): ", "{:.2f}".format(tip_amount),"euro")
print("kogumaksumus: ", "{:.2f}".format(total_cost), "euro")
print("\nKõik peavad maksma:", "{:.2f}".format(cost_per_person), "euro")
