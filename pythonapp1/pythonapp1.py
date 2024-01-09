
#6

#pikkus = float(input("Sisesta oma pikkus sentimeetrites: "))

#luhike_piir = 160
#pikk_piir = 180

#if pikkus < luhike_piir:
#    print("Sa oled lühike. ")
#elif lühuke_piir <= pikkus < pikk_piir:
#    print("Sa oled keskmise pikkusega. ")
#else:
#    print("Sa oled pikk.")
    


#try:
#    pikkus=int(input("Sisesta oma pikkus: "))
#    if pikkus>29 and pikkus<155:
#        vastus="lühike"
#    elif pikkus>=155 and pikkus<170:
#        vastus="keskmine"
#    elif pikkus>=170 and pikkus<=256:
#        vastus="pikk"
#    else:
#         vastus="tundmatu"
#    print("Sinu pikkus on {0}".format(vastus))
#except:
#    print("Vale andmete formaat!")


##7

#sugu=input("Kas sa oled mees või naine?").lower()
#if sugu=="naine" or sugu=="n":
#    l1=155
#    l2=170
#    l3=256
#elif sugu=="mees" or sugu=="m":
#    l1=160
#    l2=180
#    l3=256
#else: 
#    l1=0
#    print("Viga")



#try:
#    pikkus=int(input("Sisesta oma pikkus: "))
#    if pikkus>29 and pikkus<155:
#        vastus="lühike"
#    elif pikkus>=155 and pikkus<170:
#        vastus="keskmine"
#    elif pikkus>=170 and pikkus<=256:
#        vastus="pikk"
#    else:
#         vastus="tundmatu"
#    print("Sinu pikkus on {0}".format(vastus))
#except:
#    print("Vale andmete formaat!")

from random import *
from datetime import *
#8 Poes
#tsekk="Arve :"+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0

#toodel="Piim"
#hind=randint(50,150)/100
#v=input("Toode:"+toodel+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("Mitu?"))
#    tsekk+=toodel+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#    summa+mitu*hind
#toode="Leib"
#hind=randint(90,300)/100
#v=input("Toode:")
#print(tsekk)


#13
try:
    gender = input("Kas sa oled mees või naine? ")  
    if gender.lower() == "naine":  
        raise("Kahjuks, otsime ainult mehi")
        age = int(input("Palun märkige oma vanus: "))
        if 16 <= age <= 18:
            print("Sa oled sobid meeskonda")
        else:
            print("Kahjuks sa ei sobi meeskonda")
    else:
        print("Otsime ainult mehi.")
except:
    print("Kahjuks sa ei sobi meeskonda")


#12
#hind=float(input("Sisesta toote hind: "))
#if hind <= 10:
#    soodustus=hind*0.1
#else:
#    soodustus=hind*0.2
#okonnelik_hind=hind-sodustus
#print("Lõplik hind on", okonnelik_hind,"€")


#next
#try:
#    s1=float(input("Введите длину первой стороны квадрата: "))
#    s2=float(input("Введите длину второй стороны квадрата: "))

#    if s1==s2:
#        print("Это квадрат!")
#    else:
#        print("Это не квадрат.")
#except:
#    print("Где-то ошибка, посмотрите тип как вы указали данные!")

from random import *
from datetime import *
a=10 #int
b=2.3 #float
c="programma" #str
d="1.1" #str
print(b.is_integer()) #false
print(c.isalpha()) #true
print(d.isalpha()) #false
print(d.isnumeric()) #false
print(d.isdigit())
print(d.isdecimal())


try:
    print("Tere! Olen sinu uus sõber - Python!")
    nimi = input("Sisesta oma nimi: ")
    print(nimi + ", oi kui ilus nimi!")
    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if vastus == 1:
        pikkus = int(input("Sisesta oma pikkus (cm): "))
        mass = float(input("Sisesta oma kaal (kg): "))
        indeks = mass / (0.01 * pikkus) ** 2
        print(nimi + "! Sinu keha indeks on: {:.1f}".format(indeks))
        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("Alakaal")
        elif 19 <= indeks < 25:
            print("Normaalkaal")
        elif 25 <= indeks < 30:
            print("Ülekaal")
        elif 30 <= indeks < 35:
            print("Rasvumine")
        elif 35 <= indeks < 40:
            print("Tugev rasvumine")
        else:
            print("Tervisele ohtlik rasvumine")
    else:
        print("Kahju! See on väga kasulik info!")
    print()
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

except ValueError:
    print("Vigane sisend. Palun sisesta korrektne arv.")
