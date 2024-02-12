while True:
    a = input("Выберите действие \n1 - Замена слова \n2 - Умножение строки \n3 - Вывод и оценка длины строки \n4 - Результат двух строк \n5 - Символы строки с их индексами \n6 - Поиск индекса строки \n7 - Поиск индекса символа o \n8 - Вывод символов с 1 по 4 позицию: ")
    if a == "1":
        while True:
            S = input("Sisestage string: ")
            new_S = S.replace("sõbralik", "lahke")
            print("Tulemus", new_S)
            vastus = input("Kas jatkata? ").lower()
            if vastus == "jah":
                break
    elif a == "2":
        S1 = "Mulle meeldib programmeerimine"
        while True:
            try:
                r = int(input("Sisestage rea korduste arv: "))
                if r <= 0:
                    print("Sisesta positiivne arv")
                else:
                    result = S1 * r
                    print("Tulemus:", result)
                    break
            except ValueError:
                print("Sisestage täisarv")
    elif a == "3":
        for i in range(3):
            S = input("Sisestage string: ")
            length = len(S)
            print(f"Nööri pikkus {S} on {length}")

            if length > 10:
                print("Rida on pikk")
            elif length < 5:
                print("Rida on lühike")
            else:
                print("Keskmise pikkusega nöör")
    elif a == "4":
        while True:
            S1 = input("Sisestage esimene string: ")
            S2 = input("Sisestage teine string: ")
            result = S1 + S2
            print("Tulemus", result)

            vastus = input("Kas jatkata? ").lower()
            if vastus == "jah":
                break
    elif a == "5":
        S = "Programmeerimine"
        for i in range(len(S)):
            char = S[i]
            print(f"Index {i} sümbol: {char}")
    elif a == "6":
        S="Programmerimine, Marina"
        print(S)
        K = input("Что вы хотите найти?")
        index = S.find(K)
        print(f"Esimese rea indeks {K}", index)
    elif a == "7":
        S = "Programmeerimine, Marina"
        for i in range(3):
            index = S.rfind("o")
            print("Viimase märgi indeks 'o':", index)
    elif a == "8":
        while True:
            S = "See on Programmeerimine"
            substr = S[7:23]
            print("Ekstraheeritud string:", substr)
            break



    elif a =="9":
        c=input("Введите слово или набор букв с маленькой и большой буквы \n")
        ll=a.title(9)
        print(ll)
    



#try:
#    while True:
#        print("Kirjutage Tekst ja me kontrollime, kas teite tekst sisaldab numbreid")
#        a = input("Kirjutage tekst: ")
#        a1=[]
#        if any(char.isdigit() for char in a):
#            a1.append("Number")
#        if any(char.isalpha() for char in a):
#            a1.append("Täht")
#        if any(char.isalnum() for char in a):
#            a1.append("Numbrid ja kirjad")
#        if any(char.isspace() for char in a):
#            a1.append("Tühik")
#        if any(char.istitle() for char in a):
#            a1.append("Algustähega")
#        if not a1:
#            print("Midagi pole")
#        else:
#            print("Siin on:", (a1))

##9 содержит ли строка символы в нижнем регистре
#while True:
#    S = "Programmeerimine"
#    väiketähtede = S.islower()
#    print("Kas S on väiketähtedes?:", väiketähtede)
#    break
##10 содержит ли строка символы в верхнем регистре
#while True:
#    S = "Programmeerimine"
#    suurtähtede = S.isupper()
#    print("Kas S on suurtähtedes?:", suurtähtede)
#    break
##11 замена регистра всех символов в строке
#while True:
#    S = input("Sisestage string: ")
#    if S.lower() == 'välju':
#        break
#    result = S.swapcase()
#    print(result)
##12 перевод первой буквы строки в верхний регистр
#while True:
#    S = input("Sisestage string (väljumiseks sisestage 'välju'): ")
#    if S.lower() == 'välju':
#        break
#    result = S.capitalize()
#    print(result)
     
##13 начинается ли строка на заданный шаблок
#S = "Programmeerimine, Marina"
#lõpp = "Programmeerimine"

#if S.startswith(lõpp):
#    print("String algab eesliitega", lõpp)
#else:
#    print("String ei alga eesliitega", lõpp)

##14 заканчивается ли строка на заданный шаблон
#S = "Programmeerimine, Marina"
#lõpp = "Marina"

#if S.endswith(lõpp):
#    print("String lõpeb", lõpp)
#else:
#    print("String ei lõpe", lõpp)