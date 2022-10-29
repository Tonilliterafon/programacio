import random

x = random.randint(1, 100)
y = int(input("Adivina el numero escrivint-hi un: "))

torn = int(1)

if y==x :
    print("Enorabona! Ho has aconseguit!")


while (y!=x) :        
    if x > y:
        print("Es petit, torna a provar")
    else:
        print("Es gran, torna a provar")
    y = int(input("Adivina el numero escrivint-hi un una altra vegada: "))
    torn += 1

print("Enorabona! Aconseguit en " , torn , " vegades.")


