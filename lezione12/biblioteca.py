#Daniele Pietropaolo


# Sistema di Gestione Biblioteca
# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#     Metodi:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

# Test Cases:
# - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
# - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
# - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
# - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
 


class Libro:

    def __init__(self,titolo : str,autore : str) -> None:

        self.titolo : str = titolo
        self.autore : str = autore
        self.disponibile : bool = True

class Biblioteca:

    def __init__(self) -> None:
        
        self.libri : list[Libro] = []


    def aggiungi_libro(self,libro):

        self.libri.append(libro)

        return "\nLIBRO AGGIUNTO\n"

    def presta_libro(self,titolo):

        for i in self.libri:

            if titolo == i.titolo and i.disponibile == True:

                i.disponibile = False

                return "\nLibro prestato\n"
            

    def restituisci_libro(self,titolo):

         for i in self.libri:

            if titolo == i.titolo and i.disponibile == False:

                i.disponibile = True

                return "\nLibro restituito\n"
            

    def mostra_libri_disponibili(self):

        ld : list[str] = [i.titolo for i in self.libri if i.disponibile]


        ld = "".join(ld)


        if len(ld) != 0:

            return ld
        
        else:

            return "errore non ci sono libri disponibili"
        

# Esempio di utilizzo del programma
biblioteca = Biblioteca()
biblioteca.aggiungi_libro('Il Signore degli Anelli')
biblioteca.aggiungi_libro('1984')
biblioteca.aggiungi_libro('To Kill a Mockingbird')

biblioteca.mostra_libri_disponibili()

biblioteca.presta_libro('1984')
biblioteca.mostra_libri_disponibili()

biblioteca.restituisci_libro('1984')
biblioteca.mostra_libri_disponibili()

biblioteca.presta_libro('Il Signore degli Anelli')
biblioteca.mostra_libri_disponibili()

biblioteca.restituisci_libro('To Kill a Mockingbird')
biblioteca.mostra_libri_disponibili()



        
 
