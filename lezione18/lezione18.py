#Daniele Pietropaolo


#Esercizio 1 - Crea un decorator  che stampa n volte l'output della funzione decorata chiamandola due volte.

def ri_decorator(n):

    def decorator(func):

        def wrapper():
        
            for i in range(n):
                func()

        return wrapper
    
    return decorator


@ri_decorator(2)
def funzione():

    print("\nstampa funzione\n")


funzione()

print("\n---------------------\n")

#Esercizio 2 - Crea un decorator che calcola il tempo di esecuzione della funzione che viene decorata.

import time


def decorator(func):

    def wrapped():

        a = time.time()
        func()

        print("calcolo tempo esecuzione funzione: ",time.time() - a)
    return wrapped

funzione = decorator(funzione)

funzione()
print("\n---------------------\n")






#Esercizio 3 - Crea un decorator che permette di memorizzare informazioni sulla fibonacci in modo tale che non sia necessario ricalcolare i valori gia 













