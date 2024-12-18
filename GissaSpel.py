
import random
y = random.randint(2,99)
x = input("Gissa på ett heltal mellan 1 och 100: ")
x = int(x)
i = int(1)
while x != y:
    if x>=y:
        print("Du gissade för högt!")
        x = input("Gissa igen: ")
        x = int(x)
        i=i+1
    elif x<y:
        print("Du gissade för lågt!")
        x = input("Gissa igen: ")
        x = int(x)
        i=i+1
else:
    if i == 1:
        print("Du gissade rätt på första försöket!")

    else:            
        print(f'Du gissade rätt! Du behövde {i} försök!')

        
