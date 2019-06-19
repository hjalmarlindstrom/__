siffror = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

for i in range(len(siffror)):
    print(siffror[i])
    
siffror.remove(9)
siffror.append(9)

print("----------------------")
for i in range(len(siffror)):
    print(siffror[i])

x = 0
while x < len(siffror):
    print(siffror)
    x=x+2
