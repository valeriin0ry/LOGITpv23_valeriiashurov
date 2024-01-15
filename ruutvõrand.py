#мой код
#from math import *

#answer = input("Kas soovite lahendada ruutvõrrandi? (Mitte päris): ").lower()

#if answer == "jah":
#    try:
#        a = float(input("Sisestage väärtust a: "))
#        b = float(input("Sisestage väärtust b: "))
#        c = float(input("Sisestage väärtust c: "))
#        D = b**2 - 4*a*c
        
#        if D > 0:
#            root1 = (-b + sqrt(D)) / (2*a)
#            root2 = (-b - sqrt(D)) / (2*a)
#            print("Võrrandi lahendused:", round(root1, 2), round(root2, 2))
#        elif D == 0:
#            root = -b / (2*a)
#            print("Võrrandi lahendused:", round(root, 2))
#        else:
#            print("Võrrandil pole reaalarvulisi lahendeid.")
    
#    except ValueError:
#        print("Viga")
        
#elif answer == "ei":
#    print("Head päeva!")
#else:
#    print("Viga")


#код учителя
#from math import *
#vastus=input("Kas lahendame ruutvõrrand?").lower()
#if vastus=="jah"
#    print("Ruutvõrrandi lahendamine:")
#    try:
#        #a,b,c=map(float,input("a,b,c:")).splite(",")
#        a=float(input("a: "))
#        b=float(input("b: "))
#        c=float(input("c: "))
#        D=b**2-4*a*c
#        if D>0:
#            x1=(-b+sqrt(D))/2*a
#            x2=(-b-sqrt(D))/2*a
#            print("2 lahendust 1:{0:.2f},2:{1:.2f}".format(x1,x2))
#        elif D==0
#            x1=(-b)/2*a 
#            print("1 lahendus: {0:.2f}".format(x1))
#        else:
#            print("Lahendused puuduvad")
#    except:
#        print("Viga andmetüübiga")

    #1 задача (легкая до ужаса)
#number = float(input("Sisestage number: "))
#if number > 0:
#    print("Arv on positiivne")
#    if number % 2 == 0:
#        print("Paarisarv")
#    else:
#        print("Paaritu number")
#elif number < 0:
#    print("Negatiivne arv")
#else:
#    print("Neutraalne")


#    #2

#from math import *
#a,b,c=map(float,input("a,b,c:").split())
#if a>0 and b>0 and c>0:
#    if a+b+c==180:
#        print("Kolmnurk")
#        if a==b==c:
#            print("võrdkülgne")
#        elif a==b or b==c or a==c:
#            print("võrdhaarne")
#        else:
#            print("erikülgne")
#    else:
#        print("Nurgad")
#else:
#    print("<0")


    #3
from math import *
v=input("Kas tahad 1-7 numbrist saada päeva nimetus?")
if v.lower()=="jah":
    try:
        nr=int(input("Päeva number: "))
        if nr==1:
            p="esmaspäev"
        elif nr==2:
            p="teisipäev"
        elif v==3:
            p="kolmapäev"
        elif nr==4:
            p="neljapäev"
        elif nr==5:
            p="reede"
        elif nr==6:
            p="laupäev"
        elif nr==7:
            p="pühapäev"
        else:
            p="on vaja 1-7"
        print(p)
    except:
        print("Viga")