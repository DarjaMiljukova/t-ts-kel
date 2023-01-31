from math import *
from random import *

##0

#snäkid = ["Kartulikrõpsud", "Šokolaadikommid", "Närimiskumm", "Küpsised"]
#hind = [1.50, 0.75, 0.50, 1.00]

#kokku = 0

#while True:
#    print("Tere tulemast see snäk masin")
#    print("Palun valige snack:")
#    for i, snäk in enumerate(snäkid):
#        print(f"{i + 1}: {snäk} - €{hind[i]}")
#    valik = int(input("Sisesta oma valik (1-4): "))
#    if valik == 0:
#        break
#    if valik > 0 and valik <= len(snäkid):
#        snäk = snäkid[valik - 1]
#        kulud = hind[valik - 1]
#        kokku += kulud
#        print(f"Naudi oma {snäk}! Teie kogusumma on €{kokku}")
#    else:
#        print("Vigane valik. Proovi uuesti.")
#    break





##20
#print()
#print()
#print()


#numbers = []

#for i in range(4):
#    num = int(input("Sisesta number {}: ".format(i + 1)))
#    numbers.append(num)

#print()
#print("Kõige rohkem on: ", max(numbers))
#print()
#print("Väikseim arv on: ", min(numbers))

#print()
#print()
#print()



##20 2

#i=0
#while i<1:
#  numbers = []
#  print("Sisesta number:")
#  for i in range(4):
#    number = int(input())
#    numbers.append(number)

#  rohkem = max(numbers)
#  väiksem = min(numbers)
#  print("Kõige rohkem on: ", rohkem)
#  print("Väikseim arv on: ", väiksem)
#  i+=1



#print()
#print()
#print()



##20 3

#while True:
#  numbers = []
#  print("Sisesta number:")
#  for i in range(4):
#    number = int(input())
#    numbers.append(number)

#  rohkem = max(numbers)
#  väiksem = min(numbers)
#  print("Kõige rohkem on: ", rohkem)
#  print("Väikseim arv on: ", väiksem)
#  break

#print()
#print()
#print()

#запросить 5 имен и определить самое большое и самое маленькое среди них

s = str(input(""))
l = s.split() #подсчитывает количество символов до пробела
 
lon = max(l, key=len) #подсчитывает строку
short = min(l, key=len)
 
print(f'Longest: {lon}, shortest: {short}')
print()
print()


