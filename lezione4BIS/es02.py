#Daniele Pietrpaolo
#22/04/2024

#ESERCIZIO 2 data una stringa  S  che continene parole e spazzi,
#restituire la lunghezza dell' ultima parola in S.

def length_of_last_word(s : str) -> int:


    #rovescio la frase
    rev ="".join(reversed(s))

    n = 0

    for i in range(len(rev)):

        if rev[i] == " ":
            break
        else:

            n += 1
    print(f"nella frase \"{s} \" l' ultima parla è lunga ")
    return n
    
   
print(length_of_last_word(" HELLO WORLD"))