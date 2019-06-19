siffror = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range (len(siffror)):
    print(siffror[i])

val = int(input("Vilken är din favoritsiffra? \n"))

siffror.append(val)

for i in range (len(siffror)):
    print(siffror[i])

if 32 in siffror:
    print("32 är också min favoritsiffra")
