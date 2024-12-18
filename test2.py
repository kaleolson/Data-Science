"""
sup
"""


#y = "skola är "
#x = "kul"
#z = "inte kul"
#print (f'''Jag tycker att {y}{x} 
#oftast iallafall''')

#sträng = "Tjo"
#inta = 7
#flytning = 8.0
#lögn = False

#print(type(sträng),type(inta),type(flytning),type(lögn))

#x = "123"
#y = 2
#z = int(x)*y
#print(z)

""" a ="Hello, World!"
b = a.split(",") # returns ['Hello', ' World!']
print(b)

a = 5+3
b = 5//2
c = 5%2
d = 5**2
print(a,b,c,d) """

""" x = 10
y = 3

print(x+y,x-y,x/y,x*y,x%y,x//y,x**y)
x = 3.14
print(int(x))
x = 5
print(float(x))
 """
""" age = 10
txt = "jag är " + str(age) + " år"
print(txt)
txt = f"Jag är {age} år"
print(txt) """

""" resultat = round(0.1 + 0.2, 1)
print(resultat)

tal1 = 0.1
tal2 = 0.2
tal1 = int(tal1 * 10)
tal2 = int(tal2 * 10) 
print(tal1 + tal2)
korrektSvar = (tal1 + tal2)/10
print(korrektSvar) """

""" x = input("Skriv ett tal: ")
x = int(x)
print (x + 5) """

""" x = input("Skriv första talet: ")
y = input("Skriv andra talet: ")
x = float(x)
y = float(y)
summa = int(x)+int(y)
print (f"Summan är : {summa}") """

""" txt = "We are the \n so-called \"Vikings\"\t from the north."
print(txt) """

""" x = 10
y = 5
z = 3
print(x>5 and y < 10)
print(x>5 and y < 10 or z == 3) """

""" try:
    x = int("123")
    print(x)
except:
    print("ett fel uppstod 1")
print("Fånga specifika fel")

try:
    x = int("ett,två,tre")
    print(x)
except ValueError:
    print("ett värdefel uppstod 2")
print(x)
print("Programmet forsätter här")

try:
    x = int("123")
    y = 0
    print(x/y)
    print(x)
except ValueError:
    print("ett värdefel uppstod 2")
except ZeroDivisionError:
    print("Ett zerodivision fel")
finally:
    print("programmet fortsätter") """
""" 
try:
    x = int("123")
    y = int(input("Skriv in en siffra: "))
    print(x/y)
    print(x)
except ValueError:
    print("ett värdefel uppstod 2")
except ZeroDivisionError:
    print("Ett zerodivision fel")
except Exception as e:
    print(f"Det blev fel: {e}")
finally: #Tex kan vara att du vill köra om programmet för att användaren ska ge en giltlig siffra att dela med.
    print("Programmet frågra igen om en ny input")
print("Programmet fortstätter") """

""" empty_list= []
print(type(empty_list))
print((empty_list == []))
print(bool(empty_list))
mixed_list= [1, "Text", True]
print(mixed_list[-1:0])
for mix in mixed_list:
    if mix == 1:
        print("Det är sant ja"+mix)
    print(mix) """

""" reallyLongList = [1,2,3,4,5,2,3,4,5,2,3,4,5,2,3,4,5,2,3,4,5]
for index, number in enumerate(reallyLongList):
    if number % 2 == 0:
        print(index, number)
 """

""" reallyLongListFruit = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]
x = 1
for index, Fruits in enumerate(reallyLongListFruit):
    if  x % 3 == 0:
        print(index, Fruits)
        x = x + 1 
    else:
        x = x + 1

index = 0
reallyLongListNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for number in reallyLongListNumbers:
    if number % 3 == 0:
        index = index +1
        print(index, number)
        
print(reallyLongListNumbers[2::3])

reallyLongListNumbers.reverse()
print(reallyLongListNumbers)

print(len(reallyLongListFruit)) #Antal entiteter i en lista
reallyLongListFruit.append("sten")
print(reallyLongListFruit)
reallyLongListFruit[0] = "blåbär"
print(reallyLongListFruit) 
reallyLongListFruit.remove("blåbär")
reallyLongListFruit.pop()"""


""" def prepend(prependList, value):
    prependList.insert(0,value)

prepend(stadsLista, "Örebro") """
""" 
stadsLista = ["karlshamn", "karlskrona","karlstad","ronneby","ängelholm"]
stadsLista.append("stockholm")

stadsLista.pop(1) #del stadsLista[1]

for stad in stadsLista:
    print(stad)

siffrorLista = [1,2,3,4,5]
sum = 0
for sif in siffrorLista:
    sum = sum + sif
    print(sum)
# summa = sum(siffrorLista)
 
namnLista = ["Karl", "Malin", "Max", "Linda", "Jonas", "Sofia"]
for n in namnLista:
    if n == "Sofia":
        print(n)
i = 0 """
""" for stad1 in stadsLista:
   stadsLista[i].capitalize
   stadsLista.pop(i)
   stadsLista.append(i)
   print(stadsLista[1])
   i += 1
print(stadsLista)
 """
stadsLista = ["karlshamn", "karlskrona","karlstad","ronneby","ängelholm"]
""" i = 0
for city in stadsLista:
    stadsLista.pop(i)
    x = city.capitalize()
    stadsLista.append(i)
    print(city)
    print(i)
    i += 1
print(stadsLista)
 """
for i, city in enumerate(stadsLista):
    #city.capitalize()
    stadsLista[i] = city.capitalize()
print(stadsLista)