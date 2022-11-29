import random
import time

# ISSUE: you can break the 'play again?' by input other than 1/0

gra = 1
punkty_gracz = 0
punkty_komputer = 0
a = 0


def punkt_gra():
    global punkty_gracz
    global punkty_komputer
    punkty_gracz += 1
    print("Aktualny wynik Ty:", punkty_gracz, "Komputer:", punkty_komputer)
    return punkty_gracz


def punkt_komp():
    global punkty_gracz
    global punkty_komputer
    punkty_komputer += 1
    print("Aktualny wynik Ty:", punkty_gracz, "Komputer:", punkty_komputer)
    return punkty_komputer


while int(gra) == 1:
    opcje = ["kamien", "papier", "nozyce"]
    x = random.choice(opcje)

    gracz = ""
    while gracz not in opcje:
        gracz = input("Kamien, papier, nozyce?").lower()
    else:
        print("Zagrales:", gracz)

    time.sleep(1)
    print("Komputer zagral:", x)

    if gracz == x:
        print("remis")
        print("Aktualny wynik Ty:", punkty_gracz, "Komputer:", punkty_komputer)
        gra = input("grac dalej? 0/1")
    elif gracz == opcje[0] and x == opcje[1]:
        print("przegrales")
        punkt_komp()
        gra = input("grac dalej? 0/1")
    elif gracz == opcje[0] and x == opcje[2]:
        print("wygrales")
        punkt_gra()
        gra = input("grac dalej? 0/1")
    elif gracz == opcje[1] and x == opcje[2]:
        print("przegrales")
        punkt_komp()
        gra = input("grac dalej? 0/1")
    elif gracz == opcje[1] and x == opcje[0]:
        print("wygrales")
        punkt_gra()
        gra = input("grac dalej? 0/1")
    elif gracz == opcje[2] and x == opcje[0]:
        print("przegrales")
        punkt_komp()
        gra = input("grac dalej? 0/1")
    elif gracz == opcje[2] and x == opcje[1]:
        print("wygrales")
        punkt_gra()
        gra = input("grac dalej? 0/1")
    else:
        pass
