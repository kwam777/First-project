# Aufbau eines Simplen Quiz mit Python
print("Willkommen zum Quiz!")

spielen = input("Willst du mitspielen? ")
# kommt als Antwort ja, wird das Spiel gestartet, sonst wird es beendet.
if spielen.lower() != "ja":
    quit()
# Fragen und Antworten
print("Okay! Lass uns spielen :)")
punkte = 0
antwort = input("Was ist eine CMD in Windows ? ")
if antwort.lower() == "kommandozeileneingabe":
    print('Richtg!')
    punkte +=1
else:
    print("Falsch!")

antwort = input("Was ist eine GPU ? ")
if antwort.lower() == "graphic-processing unit":
    print('Richtg!')
    punkte += 1
else:
    print("Falsch!")

antwort = input("Welches Sprache spricht man in der Schweiz ? ")
if antwort.lower() == "schweizerdeutsch":
    print('Richtg!')
    punkte += 1
else:
    print("Falsch!")

antwort = input("Wieviele Bundesländer hat Deutschland ? ")
if antwort.lower() == "16":
    print('Richtg!')
    punkte += 1
else:
    print("Falsch!")


antwort = input(" Was ist eine RAM? ")
if antwort.lower() == "psu":
    print('Richtg!')
    punkte += 1
else:
    print("Falsch!")

# Ausgabe der Punktzahl der richtig beantworteten Fragen in % und in Dezimalzahlen
print("Du hast " + str(punkte) + "Fragen richtig !")
print("Du hast " + str((punkte/5) *100) + "%.")