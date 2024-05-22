#Daniele Pietropaolo

def transform(x: int) -> int:
    
    if x % 2 == 0:
        x  / 2

    else:
        x* 3 -1

print("\n---------------------------\n")
########################################################
import copy
def ruota(l : list,k : int):

    if k > len(l):
        m = k% len(l)
        k = m



    l2 = copy.deepcopy(l)
    l2.sort(reverse= True)

    l1 : list = []

    #inserisco i numeri fino a K
    for i in range(k):
        l1.append(l2[i])
        

    #aggiungo i numeri rimanenti a alla fine della lista
    for j in l:
        if j not in l1:
            l1.append(j)

    print(l1)


#ruota([1,2,3,4,5],27)
print("\n---------------------------\n")
##################################




def calcola_stipendio(ore_lavorate: int) -> float:
    
    stipendio = 0
    os = 0
    
    if ore_lavorate > 40:
        os = ore_lavorate - 40
        stipendio = os * 15 + 40 * 10
    else:
        stipendio = ore_lavorate * 10

    return stipendio

print("\n---------------------------\n")

###############################################

def print_seq(): 
    
    print("Sequenza a):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(1,8):
        print(i)
    print("\n")

    print("Sequenza b):")
    # SCRIVI QUI IL TUO CICLO
    l = [3, 8, 13, 18, 23]
    for i in l:
        print(i)
    print("\n")

    print("Sequenza c):")
    # SCRIVI QUI IL TUO CICLO
    l = [20, 14, 8, 2, -4, -10]
    for i in l:
        print(i)
    print("\n")

    print("Sequenza d):")
    l = [19, 27, 35, 43, 51]
    for i in l:
        print(i)
    print("\n")
    
    return
print_seq()
print("\n---------------------------\n")

##################################################################



import math

def list_statistics(numbers: list[int]) -> ... :
    
    mas = max(numbers)
    m= min(numbers)

    s = 0

    for i in numbers:
        s += i


    media : float = s / len(numbers)

    return mas,min,media




print("\n---------------------------\n")

##################################################################


def seconds_since_noon(ore : int,minuti: int,secondi : int):
    
    a = ore - 12

    o = a * 3600 #numero di secondi in un ora
    m = minuti * 60 #numero secondi in un minuto
    s = secondi + m + o #secondi totali

    return s



def time_difference(ore2 : int,minuti2: int,secondi2 : int,ore1 : int,minuti1: int,secondi1 : int):


    diff : int = 0

    s1 = seconds_since_noon(ore2,minuti2,secondi2)
    s2 = seconds_since_noon(ore1,minuti1,secondi1)

    diff =s1 - s2

    return diff



print("\n---------------------------\n")

##################################################################



def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocità: float = 100.0
    rimbalzi: int = 0

    print(f"Tempo: {tempo} Altezza: {altezza}")

    while rimbalzi < 5:
        altezza = altezza + velocità
        velocità = velocità - 96
        tempo += 1

        if altezza < 0:
            altezza= altezza*-0,5 
            velocità=velocità*-0,5

        if altezza <= 0:
        
            print(f"Tempo: {tempo} Rimbalzo!")
            rimbalzi+=1

        else:
            print(f"Tempo: {tempo} Altezza: {altezza}")







    













