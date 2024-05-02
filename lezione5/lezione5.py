#Pietropaolo Daniele
#2/5/24
import copy
#scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.



def convert_temperature(temperature : float,to_fahrenheit = True) -> float:

    if to_fahrenheit == True:
        temperature : float = (temperature * 9/5) + 32
        return temperature

    else:
        temperature = (temperature - 32) /1.8
        return temperature




print(convert_temperature(4))
print("|||||||||||||||")
print(convert_temperature(56,to_fahrenheit=False))


print("\n----------------------------------\n")

#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(threshold : int,numbers : list [int]) -> list:

    r : int = 0

    for i in range(len(numbers)):
        if numbers[i] > threshold:
            r = r + numbers[i]

    return r


print(sum_above_threshold(10,numbers = [1,2,3,4,5,20,30,10]))

print("\n----------------------------------\n")
#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli eleme

def remove_duplicates(l : list) -> list:

    l1 : list = []
    for i in l:

        if i not in l1:
            l1.append(i)

    return l1


print(remove_duplicates(l = [1,1,1,2,3,1,5,6,7,8,9,9]))


print("\n----------------------------------\n")
#Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

def rounded_average(numbers: list[int]) -> int:

    media : int = 0
    s : int = 0


    s = sum(numbers)
    media = s / len(numbers)
    media = round(media)
    return media

print(rounded_average(numbers = [1,1,2,2]))

print("\n----------------------------------\n")
#La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
#Un errore nell'implementazione porta a risultati inaspettati.

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return sum(numbers) * len(numbers)
    else:
        return sum(numbers) / len(numbers)
    
    
print(calculate_average(numbers= [1,2,3,4,5]))


print("\n----------------------------------\n")
#Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.


def countdown(n: int) -> int:

    for i in range(n,-1,-1):
        print(i)

    
countdown(5)


print("\n----------------------------------\n")
#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:

    l1 : list = []
    l2 : list = []

    for i in expression:
        if len(l1) > len(l2):
            return False
        
        if i == "(":
            l2.append(i)

        elif i == ")":
            l1.append(i)

        else: 
            continue
    return True

print(check_parentheses(expression="ciao 8())"))


print("\n----------------------------------\n")
#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(l : list = [int]) -> int:

    c : int = 0

    for i in range(len(l)):
        if l[i] != l[i + 1]  or l[i] != l[i - 1]:
            c += 1
    
    return c

print(count_isolated(l = [1, 1, 4, 5]))

#da rivedere

print("\n----------------------------------\n")
#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.


