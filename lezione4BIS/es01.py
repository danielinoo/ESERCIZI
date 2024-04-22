#Daniele Pietrpaolo
#22/04/2024

#ESERCIZIO 1 dato un intero x, restituisce true se x è palindromo, e false altrimenti

def is_palindrome(x):

    #cambio il numero in una stringa e lo rigiro
    s : int = str(x)
    rev ="".join(reversed(s))

    #conronto stringa S con la stringa rigitata(REV) 
    if s == rev:
        return True
    else:
        return False
    
print(is_palindrome(10))

    
