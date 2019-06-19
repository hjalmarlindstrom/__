val = int(input("Välj om du kryptera ett meddelande eller avkrypera ett \n 1. Kryptera \n 2. Avkryptera \n Skriv 1 för kryptering och 2 för avkryptering \n"))
if val == 1:
    meddelande = input("Vad för meddelande du vill kryptera?")
    for bokstav in meddelande:
        print(ord(bokstav), end = " ")
if val == 2:
    kryperat_meddelande = input("\n Vad för meddelande vill du avkryptera?")
    kryperat_meddelande = kryperat_meddelande.split()
    for siffra in kryperat_meddelande:
        print(chr(int(siffra)), end = " ")
