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