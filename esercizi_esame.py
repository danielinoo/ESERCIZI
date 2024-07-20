
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
            print(f"Il film {self.title} è già noleggiato.")


    def return_movie(self):

        if self.is_rented == True:
            self.is_rented = False

        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")




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
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")

    def return_movie(self,movie: Movie):

        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            movie.return_movie()

        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")



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

        if customer_id not in self.movies:

            self.movies[customer_id] = Customer(customer_id,name)

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


    def get_rented_movies(self,customer_id: str):

        if customer_id in self.customers:

            print(self.customers[customer_id].rented_movies)

        else:
            print( "Cliente non trovato.")
            l = []
            return l
    




