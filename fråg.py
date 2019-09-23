    def 
Fråga_1 = input("Vad är Finlands huvudstad?")

    points1 = ("+1")
    points2 = ("-1")
    points = 0

if Fråga_1 == ("Helsingfors"):
    print("Rätt!" + str(points1) + " poäng")
    points = points +1
else:
    print("Fel!" + str(points2) + " poäng!")
    points = points -1
    
Fråga_2 = input("Vad är Sveriges huvudstad?")
    
if Fråga_2 == ("Stockholm"):
    print("Rätt!" + str(points1) + " poäng")
    points = points +1
else:
    print("Fel!" + str(points2) + " poäng!")
    points = points -1
    
Fråga_3 = input("Vad är Rysslands huvudstad?")
if Fråga_3 == ("Moskva"):
    print("Rätt!" + str(points1) + " poäng")
    points = points +1
else:
    print("Fel!" + str(points2) + " poäng!")
    points = points -1

print ("Grattis! Du fick " +str(points) + " poäng!")

