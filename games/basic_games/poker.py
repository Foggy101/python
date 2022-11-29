# GRA W POKERA

# ISSUES AND POTENTIAL FEATURES
# przypisz wynik do rezultatow, zeby mozna bylo porownywac (2 liczby, jedna za np. fulla,
#       druga za konkretne karty(zeby porownac 2 fule)
# rozstrzyganie remisu, para vs para np. najlierw wyzsze figury, potem wyzsze kolory(sprawdz zasady gry)
# ogarnij caly kod, zeby dzial i dla gracza i dla komputera
# wiecej graczy
# poprawne zasady gry (obstawianie, po kolei flop etc)

import random
import operator
talia = [(2, "kier"), (3, "kier"), (4, "kier"), (5, "kier"), (6, "kier"), (7, "kier"), (8, "kier"), (9, "kier"),
         (10, "kier"), (11, "kier"), (12, "kier"), (13, "kier"), (14, "kier"),
         (2, "karo"), (3, "karo"), (4, "karo"), (5, "karo"), (6, "karo"), (7, "karo"), (8, "karo"), (9, "karo"),
         (10, "karo"), (11, "karo"), (12, "karo"), (13, "karo"), (14, "karo"),
         (2, "pik"), (3, "pik"), (4, "pik"), (5, "pik"), (6, "pik"), (7, "pik"), (8, "pik"), (9, "pik"), (10, "pik"),
         (11, "pik"), (12, "pik"), (13, "pik"), (14, "pik"),
         (2, "trefl"), (3, "trefl"), (4, "trefl"), (5, "trefl"), (6, "trefl"), (7, "trefl"), (8, "trefl"), (9, "trefl"),
         (10, "trefl"), (11, "trefl"), (12, "trefl"), (13, "trefl"), (14, "trefl")]
# ----------------------------------------------------------------------------------------------
# LOSOWANIE KART
karty_wgrze = []
karty = []


def losuj_karty(n):
    global karty_wgrze
    global karty
    karty = []
    for i in range(1, n+1):
        karta = random.choice(talia)
        while karta in karty_wgrze:
            karta = random.choice(talia)
        karty_wgrze.append(karta)
        karty.append(karta)
    karty.sort()
    karty_wgrze.sort()
    return karty


reka_gracz = losuj_karty(2)
reka_gracz.sort()
# reka_pc = losuj_karty(2)
river = losuj_karty(5)
karty_gracz = reka_gracz + river
karty_gracz.sort()
# karty_pc = reka_pc+river
# karty_pc.sort()
# ----------------------------------------------------------------------------------------------
# EDYTOWANIE KART DO TESTOW
# karty_gracz = [(5, "kier"), (6, "kier"), (7, "kier"), (8, "kier"), (9, "kier"), (2, "kier"), (2,"trefl")]
# karty_gracz.sort()
# print("karty gracz edit",karty_gracz)
# ----------------------------------------------------------------------------------------------
# LISTY I DICT
figury = [i for i in range(2, 15)]
kolory = ["kier", "karo", "pik", "trefl"]
figury_dict = {}
for j in figury:
    if sum(i.count(j) for i in karty_gracz) != 0:
        figury_dict.update({j: sum(i.count(j) for i in karty_gracz)})
kolory_dict = {}
for j in kolory:
    kolory_dict.update({j: sum(i.count(j) for i in karty_gracz)})
# ----------------------------------------------------------------------------------------------
# STRIT CHECK
figury_dict_keyslist = list(figury_dict)
ilosc_strit = 0
check_strit = 0
poczatek_strit_list = []
poczatek_strit_list_values = []
try:
    for i in range(0, len(karty_gracz)):
        if int(figury_dict_keyslist[i]) == int(figury_dict_keyslist[i+1])-1 == int(figury_dict_keyslist[i+2])-2\
                == int(figury_dict_keyslist[i+3])-3 == int(figury_dict_keyslist[i+4])-4:
            check_strit = 1
            poczatek_strit = i
            poczatek_strit_list.append(i)
            ilosc_strit += 1
            poczatek_strit_list_values.append(figury_dict_keyslist[i])
except IndexError:
    pass
# ----------------------------------------------------------------------------------------------
# POKER CHECK
poker_check_list = []
kolor_lista = []
check_poker = 0
for i in poczatek_strit_list_values:
    for j in range(0, 5):
        poker_check_list.append(i+j)
    for k in range(0, len(karty_gracz)):
        if poker_check_list.__contains__((karty_gracz[k][0])):
            kolor_lista.append((karty_gracz[k][1]))
    for j in kolory:
        if kolor_lista.count(j) >= 5:
            check_poker = 1
    poker_check_list.clear()
    kolor_lista.clear()
# ----------------------------------------------------------------------------------------------
# SPRAWDZANIE WYNIKU
wynik_gracza = ""
punkty_gracza = 0
trzy_pary = False
XXX = []
if check_poker == 1:
    wynik_gracza = "poker"
    punkty_gracza = 8
elif operator.countOf(figury_dict.values(), 4) == 1:
    wynik_gracza = "kareta"
    punkty_gracza = 7
elif operator.countOf(figury_dict.values(), 2) >= 1 and operator.countOf(figury_dict.values(), 3) == 1\
        or operator.countOf(figury_dict.values(), 3) == 2:
    wynik_gracza = "full house"
    punkty_gracza = 6
elif operator.countOf(kolory_dict.values(), 5) == 1 or operator.countOf(kolory_dict.values(), 6) == 1 or\
        operator.countOf(kolory_dict.values(), 7) == 1:
    wynik_gracza = "kolor"
    punkty_gracza = 5
elif check_strit == 1:
    wynik_gracza = "strit"
    punkty_gracza = 4
elif operator.countOf(figury_dict.values(), 2) == 0 and operator.countOf(figury_dict.values(), 3) == 1:
    wynik_gracza = "trojka"
    punkty_gracza = 3
elif operator.countOf(figury_dict.values(), 2) == 3:
    wynik_gracza = "2 pary"
    punkty_gracza = 2
    trzy_pary = True
elif operator.countOf(figury_dict.values(), 2) == 2:
    wynik_gracza = "2 pary"
    punkty_gracza = 2
elif operator.countOf(figury_dict.values(), 2) == 1 and operator.countOf(figury_dict.values(), 3) == 0\
        and operator.countOf(figury_dict.values(), 4) == 0:
    wynik_gracza = "para"
    punkty_gracza = 1
else:
    wynik_gracza = "nic"
    punkty_gracza = 0
# ----------------------------------------------------------------------------------------------
# WYSWIETLANIE


def wyswietl(karty):
    karty_edit = []
    Y = list(karty)
    print("(", end=" ")
    for i in range(0, len(karty)):
        Y = list(karty[i])
        if Y[0] == 11:
            Y[0] = 'J'
        elif Y[0] == 12:
            Y[0] = "Q"
        elif Y[0] == 13:
            Y[0] = "K"
        elif Y[0] == 14:
            Y[0] = "As"
        karty_edit.append(tuple(Y))

    for i in range(0, len(karty_edit)):
        if i != len(karty_edit) - 1:
            print(f'{karty_edit[i][0]} {karty_edit[i][1]}', end=', ')
        else:
            print(f'{karty_edit[i][0]} {karty_edit[i][1]}', end='')
    print(" )")


print(f'Reka gracza: ', end='')
wyswietl(reka_gracz)
print(f'River: ', end='')
wyswietl(river)
if punkty_gracza != 0 and punkty_gracza != 5 and punkty_gracza != 9:
    print(f'Wynik gracza: {wynik_gracza} ->', end=' ')
else:
    print(f'Wynik gracza: {wynik_gracza}', end=' ')

wynik_gracza_karty_0 = []
wynik_gracza_karty_1 = []
wynik_gracza_karty_end = []

# wyswietlanie wynikowych kart (wszystko poza strit,kolor,poker)
if punkty_gracza == 1 or punkty_gracza == 2 or punkty_gracza == 3 or punkty_gracza == 6 or punkty_gracza == 7:
    for figura, kolor in karty_gracz:
        if operator.countOf(wynik_gracza_karty_0, figura) == 0:
            wynik_gracza_karty_0.append(figura)
        elif operator.countOf(wynik_gracza_karty_0, figura) == 1:
            wynik_gracza_karty_1.append(figura)
    for i in range(0, len(karty_gracz)):
        try:
            if karty_gracz[i][0] == wynik_gracza_karty_1[0] or karty_gracz[i][0] == wynik_gracza_karty_1[1]\
                    or karty_gracz[i][0] == wynik_gracza_karty_1[2] or karty_gracz[i][0] == wynik_gracza_karty_1[3]:
                wynik_gracza_karty_end.append(karty_gracz[i])
        except IndexError:
            None

    if punkty_gracza == 6 and len(wynik_gracza_karty_end) != 5:  # wyswietlanie fulla przy 2 parach lub 2 trojkach
        if operator.countOf(figury_dict.values(), 3) == 2:
            wyswietl(wynik_gracza_karty_end[1:])
        elif operator.countOf(figury_dict.values(), 2) == 2:
            if wynik_gracza_karty_end[0][0] == wynik_gracza_karty_end[1][0] == wynik_gracza_karty_end[2][0]:
                wyswietl(wynik_gracza_karty_end[:-2])
            else:
                wyswietl(wynik_gracza_karty_end[2:])

    elif punkty_gracza == 7 and len(wynik_gracza_karty_end) != 4:  # ogarnia wyswietlanie przy karecie+parze/trojce
        if operator.countOf(figury_dict.values(), 2) == 1:
            wyswietl(wynik_gracza_karty_end[2:])
        elif operator.countOf(figury_dict.values(), 3) == 1:
            wyswietl(wynik_gracza_karty_end[3:])

    elif trzy_pary:                                   # ogarnia najwyzsze dwie pary z trzech
        wyswietl(wynik_gracza_karty_end[2:])

    else:
        wyswietl(wynik_gracza_karty_end)                    # normalne wyswietlanie

# wyswietlanie wynikowych kart (kolor)
if punkty_gracza == 5:
    for i in kolory:
        if kolory_dict[i] >= 5:
            print(f'{i}', end=' ')
    for i in kolory:
        if kolory_dict[i] >= 5:
            for figura, kolor in karty_gracz:
                if kolor == i:
                    wynik_gracza_karty_end.append((figura, kolor))
                    if len(wynik_gracza_karty_end) > 5:
                        wynik_gracza_karty_end.pop(0)
    wyswietl(wynik_gracza_karty_end)

# wyswietlanie wynikowych kart (strit)
if punkty_gracza == 4:
    bleh = []
    for i in range(0, len(karty_gracz)):
        bleh.append(karty_gracz[i][0])
    try:
        for i in range(int(bleh.index(poczatek_strit_list_values[-1])), len(karty_gracz)):
            wynik_gracza_karty_end.append(karty_gracz[i])
        for i in range(int(bleh.index(poczatek_strit_list_values[-1])), len(wynik_gracza_karty_end)):
            if wynik_gracza_karty_end[i][0] == wynik_gracza_karty_end[i+1][0]:
                wynik_gracza_karty_end.pop(i+1)
            if wynik_gracza_karty_end[i][0] == wynik_gracza_karty_end[i+1][0]:  # zeby przy trojce usunelo
                wynik_gracza_karty_end.pop(i+1)
    except IndexError:
        None
    while len(wynik_gracza_karty_end) > 5:
        wynik_gracza_karty_end.pop(-1)
    wyswietl(wynik_gracza_karty_end)

# wyswietlanie wynikowych kart (poker)
if punkty_gracza == 8:
    for i in kolory:
        if kolory_dict[i] >= 5:
            for figura, kolor in karty_gracz:
                if kolor == i:
                    wynik_gracza_karty_end.append((figura, kolor))
                    if len(wynik_gracza_karty_end) > 5:
                        wynik_gracza_karty_end.pop(0)
    wyswietl(wynik_gracza_karty_end)
