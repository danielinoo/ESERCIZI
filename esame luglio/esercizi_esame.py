
# Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.

# For example:

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    
    for k,v in dizionario.items():
        
        if valore == v:
            return k
            
    return None


"""----------------------------------------------------------------"""




# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.



def frequency_dict(elements: list) -> dict:
    
    d : dict [str: int] = {}
    
    for i in elements:
        
        d[i] = elements.count(i)
        
        
    return d

"""-------------------------------"""


# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.



def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    d : dict[str:float] = {}
    for k,v in prodotti.items():
        if v > 20:
            sconto = v *0.1
            d[k] = v - sconto
            
            
    return d




"""----------------------------------"""



def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    d : dict[str : list[int]] = {}
    
    for i in tuples:
        
            if i[0] not in d :
                d[i[0]] = []

                d[i[0]].append(i[1])  
                
            else:
                d[i[0]].append(i[1])  
            
                
                
    return d

"""-----------------------------------------------------"""

# Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".

def check_access(username: str, password: str, is_active: bool) -> str:
    
    
    if username == "admin" \
    and password == "12345"\
    and is_active == True:
        return "Accesso consentito"
        
    else:
        
        return "Accesso negato"
    


# Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.




"""--------------------------------------------------------------------------------"""

# Progettare un sistema di videonoleggio con i seguenti requisiti:

# 1. Classe Movie:

# Attributi:

# movie_id: str - Identificatore di un film.
# title: str - Titolo del film.
# director: str - Regista del film.
# is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
# Metodi:

# rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il film {self.title} è già noleggiato."
# return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato imposta is_rented a False, altrimenti stampa il messaggio "Il film {self.title} non è attualmente noleggiato."
# 2. Classe Customer:

# Attributi:

# customer_id: str - Identificativo del cliente.
# name: str - Nome del cliente.
# rented_movies: list[Movie] - Lista dei film noleggiati.
# Metodi:

# rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, altrimenti stampa il messaggio "Il film {movie.title} è già noleggiato."
# return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, altrimenti stampa il messaggio "Il film {movie.title} non è stato noleggiato da questo cliente."
# 3. Classe VideoRentalStore:

# Attributi:

# movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
# customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.
# Metodi:

# add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
# register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
# rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
# return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
# get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.


class Movie:

    def __init__(self,movie_id,title,director) -> None:
        self.movie_id: str = movie_id
        self.title: str = title
        self.director: str = director
        self.is_rented: bool = False

    
    def rent(self):

        if self.is_rented == False:
            self.is_rented = True

        else:
            print(f"Il film \'{self.title}\' è già noleggiato.")


    def return_movie(self):

        if self.is_rented == True:
            self.is_rented = False

        else:
            print(f"Il film \'{self.title}\' non è stato noleggiato da questo cliente.")




class Customer:

    def __init__(self,id,name: str) -> None:
        self.customer_id : str = id
        self.name : str = name
        self.rented_movies: list[Movie] = []

    def rent_movie(self,movie : Movie):

        if movie.is_rented not in self.rented_movies:
            movie.rent()
            self.rented_movies.append(movie)

        else:
            print(f"Il film \'{movie.title}\' non è stato noleggiato da questo cliente.")

    def return_movie(self,movie: Movie):

        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            movie.return_movie()

        else:
            print(f"Il film \'{movie.title}\' non è stato noleggiato da questo cliente.")



class  VideoRentalStore:

    def __init__(self) -> None:
        self.movies : dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}

    def add_movie(self,movie_id: str, title: str, director: str):

        if movie_id not in self.movies:

            self.movies[movie_id] = Movie(movie_id,title,director)
        else:
            print(f"Il film con ID {movie_id} esiste già.")

    def register_customer(self,customer_id: str, name: str):

        if customer_id not in self.customers:

            self.customers[customer_id] = Customer(customer_id,name)

        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")

    def rent_movie(self,customer_id: str, movie_id: str):

        if customer_id in self.customers and \
        movie_id in self.movies:
            
            self.customers[customer_id].rent_movie(movie =self.movies[movie_id])
            
        else:

            print("Cliente o film non trovato.")

    def return_movie(self,customer_id: str, movie_id: str):

        if customer_id in self.customers and \
        movie_id in self.movies:
            self.customers[customer_id].return_movie(movie = self.movies[movie_id])
        
        else:

            print("Cliente o film non trovato.")


    def get_rented_movies(self,customer_id: str):

        if customer_id in self.customers:

            return self.customers[customer_id].rented_movies

        else:
            print( "Cliente non trovato.")
            l = []
            return l
    



"""-------------------------------------------------"""

# n questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
 
# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
# Attributi:
# - marca (stringa)
# - modello (stringa)
# - anno (intero)

# Metodi:
# - __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
# - descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:
# - numero_porte (intero)

# Metodi:
# - __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il - numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:
# - tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

# Metodi:
# - __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".






class Veicolo:

    def __init__(self,marca,modello,anno) -> None:
            self.marca : str = marca
            self.modello : str = modello
            self.anno : int = anno

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


class Auto(Veicolo):

    def __init__(self, marca, modello, anno,numero_porte) -> None:
        super().__init__(marca, modello, anno)

        self.num_porte = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.num_porte}")


class Moto(Veicolo):

    def __init__(self, marca, modello, anno,tipo) -> None:
        super().__init__(marca, modello, anno)

        self.tipo = tipo


    def descrivi_veicolo(self): 

        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")


"""--------------------------------------------------"""

# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.
# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.
#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#     - list_recipes(): Elenca tutte le ricette esistenti.
#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

class RecipeManager:

    def __init__(self) -> None:
        self.ricette : dict[str,list[str]] = {}

    def create_recipe(self,name, ingredients):

        if name not in self.ricette:
            self.ricette[name] = ingredients
            return self.ricette

        else:
            return "errore la ricetta è gia esistente"
        
    def add_ingredient(self,recipe_name, ingredient):

        if recipe_name in self.ricette and ingredient not in self.ricette[recipe_name]:

            self.ricette[recipe_name].append(ingredient)
            return self.ricette
        else:
            return"errore la ricetta non esiste o esiste già l ingrediente"
        

    def remove_ingredient(self,recipe_name, ingredient):

        if recipe_name in self.ricette and ingredient in self.ricette[recipe_name]:

            self.ricette[recipe_name].remove(ingredient)
            return self.ricette
        
        else:
            return"errore la ricetta non esiste o non esiste l ingrediente da rimuovere dentro la ricetta"
        

    def update_ingredient(self,recipe_name, old_ingredient, new_ingredient):

        if recipe_name in self.ricette \
        and old_ingredient in self.ricette[recipe_name]:
                    
            for k,v in self.ricette.items():

                for i in range(len(v)):

                    if v[i] == old_ingredient:

                        v.insert(i,new_ingredient)
                        v.remove(old_ingredient)
                return self.ricette
        else:

            return"errore la ricetta non esiste o l inngrediente da modificare non esiste"
        

    def list_recipes(self):
        a : list = []
        for i in self.ricette.keys():
            a.append(i)

        return a
    

    def list_ingredients(self,recipe_name):

        if recipe_name in self.ricette:

            return self.ricette[recipe_name]
        
    
        else:
            return"errore la ricetta non esiste"
        


    def search_recipe_by_ingredient(self,ingredient):

        a : list = []

        for k,v in self.ricette.items():

            if ingredient in v:
                return self.ricette


"""-----------------------------"""


# Progettare un semplice sistema bancario con i seguenti requisiti:

#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.



class Account:

    def __init__(self,account_id,balance) -> None:
        self.account_id : str = account_id
        self.balance : float = balance


    def deposit(self,amount: float):

        self.balance += amount

    def get_balance(self):

        return self.balance
    
class Bank:

    def __init__(self) -> None:
        self.accounts : dict[str,Account] = {}

    def create_account(self,account_id):

        if account_id not in self.accounts:

            self.accounts[account_id] = Account(account_id,0)

            return Account(account_id,0)
        
        else:
            print("Account with this ID already exists")
            


    def deposit(self,account_id, amount):

        self.accounts[account_id].deposit(amount)

    def get_balance(self,account_id):

        if account_id in self.accounts:

            return self.accounts[account_id].get_balance()

        
        else:
            print("Account not found")



"""----------------------------------------"""

# Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

#     Classe Book:
#         Attributi:
#             book_id: str - Identificatore di un libro.
#             title: str - titolo del libro.
#             author: str - autore del libro
#             is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
#         Metodi:
#             borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
#             return_book()- Contrassegna il libro come restituito.

#     Classe Member:
#         Attributi:
#             member_id: str - identificativo del membro.
#             name: str - il nome del membro.
#             borrowed_books: list[Book] - lista dei libri presi in prestito.
#         Metodi:
#             borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
#             return_book(book): rimuove il libro dalla lista borrowed_books.

#     Classe Library:
#         Attributi:
#             books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
#             members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
#         Metodi:
#             add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
#             register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
#             borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
#             return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
#             get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.




class Book:

    def __init__(self,book_id : str,title : str, author : str) -> None:
        
        self.book_id : str = book_id
        self.title : str = title
        self.author : str = author
        self.is_borrowed : bool = False

    def borrow(self):

        if self.is_borrowed == False:
            self.is_borrowed = True
    
    def return_book(self):

        if self.is_borrowed == True:
            self.is_borrowed = False


class Member:

    def __init__(self,member_id : str,name : str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books : list[Book] = []

    def borrow_book(self,book : Book):

        if book.is_borrowed == False:
            self.borrowed_books.append(book)

    
    def return_book(self,book : Book):
            self.borrowed_books.remove(book)

            


class Library():

    def __init__(self) -> None:
        self.books : dict[str,Book] = {}
        self.members : dict[str,Member] = {}

    def add_book(self,book_id: str, title: str, author: str):
        self.books[book_id] = Book(book_id,title,author)

    def register_member(self,member_id:str, name: str):
        self.members[member_id] = Member(member_id,name)

    def borrow_book(self,member_id: str, book_id: str):
    
        if member_id in self.members:
            if book_id in self.books:
                if self.books[book_id].is_borrowed == False:
                    self.members[member_id].borrow_book(self.books[book_id])
                    self.books[book_id].borrow()
                
                else:
                    print("Book is already borrowed")
            else:
                print("Book not found")

        else:
            print("Member not found")

    def return_book(self,member_id: str, book_id: str):
            
        if self.books[book_id] in self.members[member_id].borrowed_books:
            self.members[member_id].return_book(self.books[book_id])
            self.books[book_id].return_book()

        else: 
            print("Book not borrowed by this member")



    def get_borrowed_books(self,member_id):
        l : list = []
        for i in self.members[member_id].borrowed_books:
            l.append(i.title)

        return l

            






 	




