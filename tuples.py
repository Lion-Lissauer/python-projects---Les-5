
steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
# Loop door de tuple en print elk element afzonderlijk

for stad in steden:
    print(stad)

# --------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple

print()
print(tuple1 + tuple2)

# --------------------------------------------------------------------------------------------


# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)

# Print enkele elementen van de tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element

tuple3 = ("iets",69,None,False,"plop!")

print()
print(tuple3[0])
print(*tuple3[1:4])
print(tuple3[4])

# --------------------------------------------------------------------------------------------


# Maak een tuple met een naam en een leeftijd

# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)

# Print de uitgepakte variabelen

tuple4 = ("Lion", 40)
naam, leeftijd = tuple4 # Bij een verkeerde volgorde krijgen de variabelen de verkeerde waarden.

print()
print("Naam:", naam)
print("Leeftijd:", leeftijd)
