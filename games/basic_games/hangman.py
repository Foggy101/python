import time


def ustawienia():
    global liczba_zyc
    global haslo
    global wisielec
    haslo = input("Podaj haslo do zgadniecia").lower()
    haslo = haslo.lower()
    while not haslo.isalpha():
        haslo = input("Podaj haslo do zgadniecia").lower()
    else:
        print("Haslo zaakceptowane")

    wisielec = "_" * len(haslo)

    liczba_zyc = input("Ustaw liczbe prob")
    while not liczba_zyc.isdigit() or int(liczba_zyc) <= 0:
        liczba_zyc = input("Ustaw liczbe prob")
    else:
        print("Liczba zyc ustalona")
        time.sleep(1)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Haslo:", wisielec)
    liczba_zyc = int(liczba_zyc)


def guess():
    global litera
    print("Liczba pozostalych prob:", liczba_zyc, end="  ")
    litera = input("Wpisz nowa litere: ").lower()
    while not litera.isalpha() or len(litera) != 1:
        litera = input("Wpisz pojedyncza litere!").lower()
    else:
        pass

    while litera in zgadniete_litery or litera in pudlo_litery:
        litera = input("Juz to probowales! Zgadnij inna litere").lower()
    else:
        pass


def check():
    global litera
    global zgadniete_litery
    global index
    global wisielec
    global wisielec_new
    global zgadniete_litery
    global liczba_zyc

    if haslo.__contains__(litera):
        zgadniete_litery.append(litera)
        index = -1
        for i in haslo:
            index += 1
            if litera == i:
                wisielec_lista = list(wisielec)
                wisielec_lista[index] = litera
                wisielec_new = "".join(wisielec_lista)
                wisielec = wisielec_new
            else:
                pass
        if len(zgadniete_litery) != len(set(haslo)):
            print("Dobrze! Haslo:", wisielec)
        else:
            pass
    else:
        pudlo_litery.append(litera)
        liczba_zyc -= 1
        if liczba_zyc != 0:
            print("Pudlo!  Haslo:", wisielec)
        else:
            pass


gra = "tak"
while gra == "tak":
    haslo = "haslo"
    zgadniete_litery = []
    pudlo_litery = []
    ustawienia()
    while len(zgadniete_litery) != len(set(haslo)) and liczba_zyc != 0:
        wisielec_new = ""
        guess()
        check()
    if liczba_zyc == 0:
        print("Niestety, straciles wszystkie zycia i przegrales! Poprawne haslo to:", haslo)
        gra = input("Czy chcesz zagrac jeszcze raz? tak/nie").lower()
    else:
        print("Gratulacje, wygrales! Odgadniete haslo: '", haslo, "'")
        gra = input("Czy chcesz zagrac jeszcze raz? tak/nie").lower()
        while gra != "tak" and gra != "nie":
            gra = input("Czy chcesz zagrac jeszcze raz? tak/nie").lower()
        else:
            pass
else:
    print("Do zobaczenia!")
