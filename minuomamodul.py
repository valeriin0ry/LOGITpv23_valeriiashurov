from pickle import TRUE
from string import *
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsiooni tagastab täidetud kasutaja list ja salasõna list:
    Kirjeldus
    :param list kasutajad:kasutajate list
    :param list paroolid:paroolide list
    :rtype: list,list
    """
    while True:
        nimi = input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool = input("Mis on sinu parool? ")
                flag_p = False
                flag_l = False
                flag_u = False
                flag_d = False
                if len(parool) >= 8:
                    parool_list = list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p = True
                        elif p in ascii_lowercase:
                            flag_l = True
                        elif p in ascii_uppercase:
                            flag_u = True
                        elif p in digits:
                            flag_d = True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                        print("Kasutaja registreeritud!")
                        break
                    else:
                        print("Nõrk salasõna! Salasõna peab sisaldama vähemalt üht suurt tähte, üht väikest tähte, ühte numbrit ja ühte erimärki.")
                else:
                    print("Nõrk salasõna! Salasõna peab olema vähemalt 8 tähemärki pikk.")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid
    return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas
        Nimi on järjendis kasutajad
        Salasõna on paroolide järjendis
        Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad: ...
    :param list paroolid: ...
    """
    p = 0
    while True: 
        nimi = input("Sisesta kasutajanimi: ") 
        if nimi in kasutajad:
            while True:
                parool = input("Sisesta salasõna: ")
                p += 1
                try:
                    if kasutajad.index(nimi) == paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        return
                except ValueError:
                    print("Vale nimi või salasõna!")
                    if p == 5:
                        print("Proovi uuesti 10 sekundi pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sekundit")
        else:
            print("Kasutajat pole")
def nimi_või_parooli_muurmine(list_:list, tüüp:str):
    """
    """
    if tüüp=="nimi":
        muutuja=input("Vana kasutajanimi: ")
        uus_muutuja=input("Uus kasutajanimi: ")
    elif tüüp=="parool":
        muutuja=input("Vana parool: ")
        uus_muutuja=input("Uus parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uue nimi või parool: ")
        list_[indeks]=uus_muutuja
        print("Muudetud!")
    else:
        print("Sisestati vale kasutajanimi või parool")
    return list_
def parooli_taastamine(kasutajad:list, paroolid:list):
    """

    """
    nimi = input("Sisesta oma kasutajanimi: ")
    if nimi in kasutajad:
        print("Kasutaja on olemas! Allpool on teie parool")
        indeks = kasutajad.index(nimi)
        parool = paroolid[indeks]
        print(f"Sinu parool on: {parool}")
        vastus=input("Kas te tahate parooli muuta? ")
        if vastus.lower()=="jah":
            uus_parool=input("Sisesta uus parool: ")
            paroolid[indeks]=uus_parool
            print("Muudetud!")
        else:
            print(f"Okei, siis siin on sinu parool! -> {parool}")
    else:
        print("Kasutaja pole")
