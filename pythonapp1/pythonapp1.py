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
#8 Poes
tsekk="Arve: 12345\nToode Hind Kogus Summa\n"
summa=0

toodel="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toodel+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toodel+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
print(tsekk)
