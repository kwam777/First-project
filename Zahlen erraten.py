import random

top_of_range = input("Gib eine Zahl ein: ")
# Ist die Top_of_Range angabe eine Zahl,wird die if Schleife ausgeführt
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Bitte gebe beim nächsten Mal eine Zahl an die größer als 0 ist. ')
        quit()

else:
    print("Bitte gebe beim nächsten Mal eine Zahl an. ")
    quit()


zufallnummer = random.randint(0, top_of_range)

versuche = 0
while True:
    versuche += 1
    benutzer_ratet = input('Rate einfach: ')
    if benutzer_ratet.isdigit():
        benutzer_ratet = int(benutzer_ratet)
    else:
       print('Bitte gib eine Nummer ein. ')
       continue

    if benutzer_ratet == zufallnummer:
        print("Du hast es geschafft!")
        break
    else:
        if benutzer_ratet > zufallnummer:
            print("Zu hoch angesetzt!")
        else:
            print("Zu tief angesetzt")


print(" Du hast nur", versuche, "Versuche gebraucht! :)" )
