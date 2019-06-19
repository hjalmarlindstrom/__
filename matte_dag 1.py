import math
x = 23.5
y = math.sqrt(x)
z = (math.pow(x,3))

answer = math.sqrt(81)
print(answer)
print(math.pow(12,12))

namn = "chad chowdury"
ålder = "21 år"
yrke = "frizbeespelare"
nationalitet = "wakanda"

print("jag heter" ,namn,"och är", ålder, "jag kommer från" ,nationalitet ,"och jobbar som", yrke)




namn =input("Vad heter du? ")

if namn == "Hjalmar":
     print("Hej Hjalmar")
else:
    print("Hej", namn)

ålder = int(input("Hur gammal är du? "))



if ålder == 13:
    print("Du är lika gammal som Hjalmar")
elif ålder > 12:
    print("Du är tillräckligt gammal")

else:
    print("Du är inte tillräckligt gammal!")
