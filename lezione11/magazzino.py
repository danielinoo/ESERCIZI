#daniele pietropaolo


"""Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.

"""

class Prodotto:

    def __init__(self,nome : str,quantita : int) -> None:

        self.nome = nome
        self.quantita = quantita        






class Magazzino:

    def __init__(self) -> None: 

        self.prodotto : list[Prodotto] = []
        

    
    def aggiungi_prodotto(self,prodotto : Prodotto):

        self.prodotto.append(prodotto)


    def cerca_prodotto(self,nome : str):

        for i in self.prodotto:

            if i.nome == nome:

                return nome
            

    def verifica_disponibilità(self,nome : str):


        for i in self.prodotto:

            if i.nome == nome:

                if i.quantita > 0:

                    return "disponibile"
                
            



prodotto1 = Prodotto("tappo",30)
prodotto2 = Prodotto("latte",2)
prodotto3 = Prodotto("lattuga",0)

m = Magazzino()

m.aggiungi_prodotto(prodotto1)
m.aggiungi_prodotto(prodotto2)
m.aggiungi_prodotto(prodotto3)


print(m.cerca_prodotto("latte"))

print(m.verifica_disponibilità("lattuga"))
print(m.verifica_disponibilità("tappo"))





            
















