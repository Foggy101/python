import random
import time


def number(x):
    x = input("Podaj kolejna liczbe: ")
    while not x.isdigit() or int(x) >= 50 or int(x) < 1 or int(x) in player:
        print("Niepoprawna liczba.")
        x = input("Podaj niepowtarzajaca sie liczbe calkowita w przedziale od 1 do 49: ")
    else:
        x = int(x)
        return x


def number1(z):
    z = input("Podaj pierwsza liczbe calkowita w przedziale od 1 do 49. Kolejne liczby nie moga sie powtarzac: ")
    while not z.isdigit() or int(z) >= 50 or int(z) < 1 or int(z) in player:
        print("Niepoprawna liczba.")
        z = input("Podaj liczbe calkowita w przedziale od 1 do 49: ")
    else:
        z = int(z)
        return z


def guess(y):
    y = number(y)
    return y
    player1 = [n1, n2, n3, n4, n5, n6]
    print(player1)


def update():
    player = [n1, n2, n3, n4, n5, n6]
    print(player)
    return player


n1 = n2 = n3 = n4 = n5 = n6 = ""
player = [n1, n2, n3, n4, n5, n6]

n1 = number1(n1)
player = [n1, n2, n3, n4, n5, n6]
print("Twoje liczby:", player)

n2 = number(n2)
player = [n1, n2, n3, n4, n5, n6]
print("Twoje liczby:", player)

n3 = number(n3)
player = [n1, n2, n3, n4, n5, n6]
print("Twoje liczby:", player)

n4 = number(n4)
player = [n1, n2, n3, n4, n5, n6]
print("Twoje liczby:", player)

n5 = number(n5)
player = [n1, n2, n3, n4, n5, n6]
print("Twoje liczby:", player)

n6 = number(n6)
player = [n1, n2, n3, n4, n5, n6]
print("Twoje liczby:", player)

time.sleep(2)
print("Komora maszyny losujacej jest pusta. Nastepuje zwolnienie blokady.")
time.sleep(2)
print("Rozpoczynamy losowanie!")
time.sleep(2)

r1 = r2 = r3 = r4 = r5 = r6 = ""
game = [r1, r2, r3, r4, r5, r6]

r1 = random.randrange(1, 50)
game = [r1, r2, r3, r4, r5, r6]
print(game)
time.sleep(1)

r2 = random.randrange(1, 50)
while r1 == r2 or r3 == r2 or r4 == r2 or r5 == r2 or r6 == r2:
    r2 = random.randrange(1, 50)
else:
    pass
game = [r1, r2, r3, r4, r5, r6]
print(game)
time.sleep(1)

r3 = random.randrange(1, 50)
while r1 == r3 or r2 == r3 or r4 == r3 or r5 == r3 or r6 == r3:
    r3 = random.randrange(1, 50)
else:
    pass
game = [r1, r2, r3, r4, r5, r6]
print(game)
time.sleep(1)

r4 = random.randrange(1, 50)
while r1 == r4 or r2 == r4 or r3 == r4 or r5 == r4 or r6 == r4:
    r4 = random.randrange(1, 50)
else:
    pass
game = [r1, r2, r3, r4, r5, r6]
print(game)
time.sleep(1)

r5 = random.randrange(1, 50)
while r1 == r5 or r2 == r5 or r3 == r5 or r4 == r5 or r6 == r5:
    r5 = random.randrange(1, 50)
else:
    pass
game = [r1, r2, r3, r4, r5, r6]
print(game)
time.sleep(1)

r6 = random.randrange(1, 50)
while r1 == r6 or r2 == r6 or r3 == r6 or r4 == r6 or r5 == r6:
    r6 = random.randrange(1, 50)
else:
    pass
game = [r1, r2, r3, r4, r5, r6]
print(game)
time.sleep(4)

print("")
print("Twoje liczby:", player)
print("Wylosowane liczby", game)
result = set(player).intersection(game)
time.sleep(1)
if len(result) == 0:
    print("Wynik:", len(result), " Nie odgadles ani jednej liczby!")
else:
    print("Wynik:", len(result), " Odgadniete liczby:", result)

