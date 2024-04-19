#Daniele Pietropaoo
#19/04/24

#ESERCIZIO 1


#funzione di sottrazione
def subtrack(a : int,b : int) -> int:


    return a - b

print(subtrack(67,4))
print("-----------------------------")



"""------------------------------------------------"""


#ESERCIZIO 2

def cv(n : int) -> int:

    if n == 5:
        print("il numero è uguale a 5")
    elif n < 5:
        print("il numero è minore di cinque")

    else: 
        print("il numero è maggiore di 5")

cv(2)

print("-----------------------------")



"""------------------------------------------------"""

#ESERCIZIO 3

def cs(s : str) -> str:

    if  len(s)== 10:
        print(f"il testo {s} è uguale a 10")
    elif len(s) < 10:
        print(f"il testo {s} è minore a 10")
        

    else: 
        print(f"il testo {s}  è maggiore di 10")

cs(s = "DAJEROMADAJE")



print("-----------------------------")



"""------------------------------------------------"""

#ESERCIZIO 4

def pn(l : list) -> int:

    for i in l:
    
     print("\n",i)

pn(l = [1,2,3,4,5])

print("-----------------------------")



"""------------------------------------------------"""

#ESERCIZIO 5

def ce(l : list) -> str:

    for i in l:
        if i == 5:
            print(f"il numero è uguale a 5")
        elif i < 5:
            print(f"{i} è minore di cinque")

        else: 
            print(f"{i} è maggiore di 5")


ce(l = [1,2,3,4,5])

print("-----------------------------")



"""------------------------------------------------"""
    
     


