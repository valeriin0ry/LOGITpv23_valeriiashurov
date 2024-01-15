from math import *

answer = input("Kas soovite lahendada ruutvõrrandi? (Mitte päris): ").lower()

if answer == "jah":
    try:
        a = float(input("Sisestage väärtust a: "))
        b = float(input("Sisestage väärtust b: "))
        c = float(input("Sisestage väärtust c: "))
        D = b**2 - 4*a*c
        
        if D > 0:
            root1 = (-b + sqrt(D)) / (2*a)
            root2 = (-b - sqrt(D)) / (2*a)
            print("Võrrandi lahendused:", round(root1, 2), round(root2, 2))
        elif D == 0:
            root = -b / (2*a)
            print("Võrrandi lahendused:", round(root, 2))
        else:
            print("Võrrandil pole reaalarvulisi lahendeid.")
    
    except ValueError:
        print("Viga")
        
elif answer == "ei":
    print("Head päeva!")
else:
    print("Viga")