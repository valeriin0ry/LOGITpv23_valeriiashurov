#1 замена слова
while True:
    S = input("Sisestage string: ")
    new_S = S.replace("sõbralik", "lahke")
    print("Tulemus:", new_S)
    vastus = input("Kas jätkata?: ").lower()
    if vastus == "jah":
        break


#2 умножение строки
S1 = "Mulle meeldib programmeerimine"
while True:
    try:
        r = int(input("Sisestage rea korduste arv: "))
        if r <= 0:
            print("Sisestage positiivne arv!")
        result = S1 * r
        print("Tulemus:", result)
        break
    except ValueError:
        print("Sisestage täisarv!")
#3 вывод и оценка длины 
for i in range(3):
    S = input("Sisestage string: ")
    l = len(S)
    print(f"Stringi {S} pikkus on {l}")
    
    if length > 10:
        print("See string on üsna pikk!")
    elif length < 5:
        print("See string on üsna lühike!")
    else:
        print("See string on mõõduka pikkusega.")

#4 результат двух строк
while True:
    S1 = input("Sisestage esimene string: ")
    S2 = input("Sisestage teine string: ")
    result = S1 + S2
    print("Tulemus:", result)
    
    vastus = input("Kas jätkata?: ").lower()
    if vastus =="jah":
        break
#5 символы строки с их индексами
S = "Programmeerimine"
for i in range(len(S)):
    char = S[i]
    print(f"Indeksiga {i} sümbol: {char}")
#6 поиск индекса строки марина
S = "Programmeerimine, Marina"
for i in range(len(S)):
    index = S.find("Marina")
    print("Esimese rea indeks:", index)
#7 поиск индекса с о
S = "Programmerimine, Marina"
for i in range(3):  
    index = S.rfind("o")
    print("Viimase 'o' sümboli indeks:", index)
#8 вывод с 1 по 4 позицию
while True:
    S = "Programmeerimine"
    substr = S[1:4]
    print("Väljavõetud string:", substr)
    break
#9 содержит ли строка символы в нижнем регистре
while True:
    S = "Programmeerimine"
    väiketähtede = S.islower()
    print("Kas S on väiketähtedes?:", väiketähtede)
    break
#10 содержит ли строка символы в верхнем регистре
while True:
    S = "Programmeerimine"
    suurtähtede = S.isupper()
    print("Kas S on suurtähtedes?:", suurtähtede)
    break
#11 замена регистра всех символов в строке
while True:
    S = input("Sisestage string: ")
    if S.lower() == 'välju':
        break
    result = S.swapcase()
    print(result)
#12 перевод первой буквы строки в верхний регистр
while True:
    S = input("Sisestage string (väljumiseks sisestage 'välju'): ")
    if S.lower() == 'välju':
        break
    result = S.capitalize()
    print(result)
     
#13 начинается ли строка на заданный шаблок
S = "Programmeerimine, Marina"
lõpp = "Programmeerimine"

if S.startswith(lõpp):
    print("String algab eesliitega", lõpp)
else:
    print("String ei alga eesliitega", lõpp)

#14 заканчивается ли строка на заданный шаблон
S = "Programmeerimine, Marina"
lõpp = "Marina"

if S.endswith(lõpp):
    print("String lõpeb", lõpp)
else:
    print("String ei lõpe", lõpp)