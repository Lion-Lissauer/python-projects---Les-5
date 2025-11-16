import time
from operator import itemgetter

studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana", 9.1)]

for naam, cijfer in studenten:
    print(f"{naam} - {cijfer}")

cijfers = []
for student in studenten:
    naam = student[0]
    cijfer = student[1]
    cijfers.append(cijfer)

# Gemiddelde cijfers berekenen

gemiddelde = sum(cijfers) / len(cijfers)
student_nr1 = studenten[0]
for student in studenten:
    if student[1] > student_nr1[1]:
       student_nr1 = student

print(f"\nHet gemiddelde cijfer is {gemiddelde}"
      f" en de beste student is {student_nr1[0]} met een eindcijfer van {student_nr1[1]}")

# Studenten toevoegen

while True:
    student_toevoegen = input("\nStudenten toevoegen? (ja/nee) ").lower()
    if student_toevoegen == "ja":
        naam = input("Voeg een nieuwe student toe: ")
        cijfer = float(input(f"{naam} heeft het volgende resultaat bereikt: "))
        print()
        studenten.append((naam, cijfer))
        for naam, cijfer in studenten:
            print(f"{naam} - {cijfer}")
        break
    elif student_toevoegen == "nee":
        break
    else:
        print("Ongeldige invoer")

# Studenten en bijbehorende resultaten opzoeken

time.sleep(1)
naam_zoeken = input("\nZoek een student: ")
naam_gevonden = False

for naam, cijfer in studenten:
    if naam.lower() == naam_zoeken.lower():
        print(f"{naam} heeft een {cijfer} behaald.")
        naam_gevonden = True
        break
if not naam_gevonden:
    print("Naam niet gevonden")

# Sorteren op hoogste cijfers

while True:
    time.sleep(1)
    lijst_sorteren = input("\nResultaten sorteren? (ja/nee) ").lower()
    print()
    if lijst_sorteren == "ja":
        lijst_gesorteerd = sorted(studenten, key=itemgetter(1), reverse=True)
        for naam, cijfer in lijst_gesorteerd:
            print(f"{naam} - {cijfer}")
        break
    elif lijst_sorteren == "nee":
        break
    else:
        print("Ongeldige invoer")
