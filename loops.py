# Tafels

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# Probeer het eerst zonder loop,

waarde = int(input("Voer een getal in: "))

print(waarde, "x 1 =", waarde * 1)
print(waarde, "x 2 =", waarde * 2)
print(waarde, "x 3 =", waarde * 3)
print(waarde, "x 4 =", waarde * 4)
print(waarde, "x 5 =", waarde * 5)
print(waarde, "x 6 =", waarde * 6)
print(waarde, "x 7 =", waarde * 7)
print(waarde, "x 8 =", waarde * 8)
print(waarde, "x 9 =", waarde * 9)
print(waarde, "x 10 =", waarde * 10)

# Probeer het nu met een loop.

getal = int(input("\nVoer een getal in: "))

for i in range(1, 11):
    print(getal, "x", i, "=", getal * i)

# --------------------------------------------------------------------------------------------

# Optellen
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.

# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)

limit = int(input("\nVoer een getal in: "))
sum = 0
divide = []

for i in range(1, limit + 1):
    sum += i
    divide.append(str(i))

output = " + ".join(divide) + f" = {sum}"

print(f"De som van alle getallen tot {limit} is {sum} ({output})")
print()

# --------------------------------------------------------------------------------------------

# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# --------------------------------------------------------------------------------------------


# Fibonacci-reeks

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34

# i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
a = 0
b = 1

# Eerst drukken we de eerste twee getallen af

print(f"{a} en {b}")

# Vervolgens berekenen we de volgende getallen en drukken ze af

i = int(input("\nHoeveel Fibonacci-getallen wil je zien? "))
fibonacci = [a,b]

for _ in range(i - 2):
    c = a + b
    fibonacci.append(c)
    a,b = b,c

print(" ".join(map(str, fibonacci)))
