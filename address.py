min_lista = ['Person1', 'Person2', 'Person3']
min_dictionary = {'Anna': 'person1@gmail.com', 'Peter': 'person2@gmail.com'}

open = True

while open:
    print ("Sidu morjens!")
    svar = input("Vad vill du göra? Lägg till (l), hämta (h) eller stäng (s)")
    if svar == 'l':
        namn = input ("Ange namn").lower()
        epost = input ("Ange epost").lower()
        min_dictionary[namn] = epost
    elif svar == 'h':
        epost_namn = input("Vems epost letar du efter?").lower()
        if epost_namn in min_dictionary:
            print(min_dictionary[epost_namn])
        else:
            print("Tyvärr finns ej denna person i din lista!")
    elif svar == 's':
        print("På återseende!")
        break
    else:
        print ("Välj l, h eller s")
        




