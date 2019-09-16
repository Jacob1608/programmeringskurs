Fråga_1 = input("Vad är Finlands huvudstad?")

points1 = ("+1")
points2 = ("-1")

if Fråga_1.lower() == ("Helsingfors"):
    print("Rätt!" + str(points1) + " poäng")
else:
    print("Fel!" + str(points2) + " poäng!")
    
Fråga_2 = input("Vad är Sveriges huvudstad?")
    
if Fråga_2.lower() == ("Stockholm"):
    print("Rätt!" + str(points1) + " poäng")
else:
    print("Fel!" + str(points2) + " poäng!")
    
Fråga_3 = input("Vad är Rysslands huvudstad?")
if Fråga_3.lower() == ("Moskva"):
    print("Rätt!" + str(points1) + " poäng")
else:
    print("Fel!" + str(points2) + " poäng!")