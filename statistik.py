from statistics import *

def medel(siffror):
    print(mean(siffror))

def medianen(siffror):
    print(median_grouped(siffror))

siffror = []

b = True

while b:

    print(siffror)
    print("Välj vilket räknesätt du vill använda")
    
    print("1. Medelvärde")
    print("2. Median")
    print("3. Lägg till fler siffror")
    print("4. Ta bort siffror")
    print("5. Avsluta programmet")
    

    val = (input("Skriv 1, 2, 3 eller 4\n"))

    if val == "1":
        medel(siffror)

    elif val == "2":
        medianen(siffror)
        
    elif val == "3":
        siffra = int(input("Hur måga siffror vill du lägga till\n"))
        for i in range(siffra):
            siffra2 = int(input("Skriv siffran du vill lägga till\n"))
            siffror.append(siffra2)

    elif val == "4":
        siffra1 = int(input("Skriv vilken av siffrorna du vill ta bort\n"))
        for i in range(siffra1):
            siffra3 = int(input("Skriv siffran du vill ta bort\n"))
            siffror.remove(siffra1)
                
    elif val == "5":
        print("Hej då")
        b = False
    
