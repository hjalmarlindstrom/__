def velocity(s, t):
    if t == 0:
        print("Man kan inte dividera med noll")
    else:
        print(s/t)


def time(s, v):
    if v == 0:
        print("Man kan inte dividera med noll")
    else:
        print(s/v)

def segment(v, t):
    print(v*t)
while True:
    print("Välj vad du vill räkna ut av valen nedan")
    print("1. Hasighet")
    print("2. Tid")
    print("3. Sträckan")
    val = int(input("Skriv 1, 2, eller 3 för att välja"))
    if val == 1:
        s = int(input("Skriv stäckan"))
        t = int(input("Skriv tiden"))
        if t == 0:
            print("Man kan inte dividera med noll")
        else:
            velocity(s/t)

    if val == 2:
        s = int(input("Skriv stäckan"))
        v = int(input("Skriv hastigheten"))
        if v == 0:
            print("Man kan inte dividera med noll")
        else:
            time(s/v)

    if val == 3:
        v = int(input("Skriv hastigheten"))
        t = int(input("Skriv tiden"))
        segment(v*t) 

    print("-------------------------")

            
