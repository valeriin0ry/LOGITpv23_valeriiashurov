from random import *
name1 = "valera"
name2 = "eldar"
vastuses = ["камень", "ножницы", "бумага"]
name1_score = 0
name2_score = 0
round_ = 1

while True:
    print("Раунд", round_)
    name1_vastus = input("Камень, ножницы, бумага, раз два три!: ").lower()
    if name1_vastus in vastuses:
        name2_vastus = vastuses[randint(0, 2)]
        print(f"У {name2} {name2_vastus}")
        if name1_vastus == "камень" and name2_vastus == "ножницы" or \
           name1_vastus == "ножницы" and name2_vastus == "бумага" or \
           name1_vastus == "бумага" and name2_vastus == "камень":
            print(f"{name1} победил!")
            name1_score += 1
        elif name1_vastus=="камень" and name2_vastus=="камень" or \
             name1_vastus=="ножницы" and name2_vastus=="ножницы" or \
             name1_vastus=="бумага" and name2_vastus=="бумага":
            print("Ничья, еще разок")
        elif name1_vastus != name2_vastus:
            print(f"{name2} победил!")
            name2_score += 1    
        print(f"Счет: {name1} - {name1_score}, {name2} - {name2_score}")
        again = input("Сыграть еще?: ").lower()
        if again != "да":
            print("Новая игра")
            break
        round_ += 1
    else:
        print("Мы играем в другую игру")