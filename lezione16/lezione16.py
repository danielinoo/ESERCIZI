#Pietropaolo Daniele


# Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

# Classe Contatore
# Attributi:
# - conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

# Metodi:
# - __init__(): Inizializza l'attributo conteggio a 0.
# - setZero(): Imposta il conteggio a 0.
# - add1(): Incrementa il conteggio di 1.
# - sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
# - get(): Restituisce il valore corrente del conteggio.
# - mostra(): Stampa a schermo il valore corrente del conteggio.






class Contatore:
    def __init__(self) -> None:
        self.conteggio = 0


    def setZero(self):
        
        self.conteggio = 0


    def add1(self): 
        
        self.conteggio += 1


    def sub1(self):

        if self.conteggio > 0:
            self.conteggio -= 1

        else:
            print("Non è possibile eseguire la sottrazione")

    def get(self):
        return self.conteggio

    def mostra(self):
        print( f"Conteggio attuale: {self.conteggio}")


    
##############################################################

# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.




class RecipeManager:

    def __init__(self) -> None:
        self.collezione : dict[str: list[str]] = {}


    def create_recipe(self,name : str, ingredients : list):

        if name not in self.collezione:
            self.collezione[name] = ingredients
            return self.collezione

        else:

            return "errore"



    def add_ingredient(self,recipe_name : str, ingredient : str):

        if recipe_name in self.collezione:
            self.collezione[recipe_name].append(ingredient)
            return self.collezione


    def remove_ingredient(self,recipe_name, ingredient):

        if recipe_name in self.collezione:
            self.collezione[recipe_name].remove(ingredient)
            return self.collezione


    def update_ingredient(self,recipe_name, old_ingredient, new_ingredient):

        
        if recipe_name in self.collezione:

            if old_ingredient in self.collezione[recipe_name]:

                self.collezione[recipe_name].remove(old_ingredient)
                self.collezione[recipe_name].append(new_ingredient)
                return self.collezione
        
            else:
                return "l ingrediente non esiste"
        
        
        else:
            return "la ricetta non esiste"


    def list_recipes(self): 

        return list(self.collezione.keys())

    def list_ingredients(self,recipe_name : str):

        l : list[str] = []

        if recipe_name in self.collezione:

            for v in self.collezione[recipe_name]:

                l.append(v)

            

            return l
        
        else:
            return "la ricetta non esiste"

    def search_recipe_by_ingredient(self,ingredient): 

        l1 : dict[str : list[str]] = {}
        
        for k,v in self.collezione.items():

            if ingredient in v:

                l1[k] = v


        if len(l1) != 0:

            return l1
        
        else:

            return "errore la ricetta non esiste"



#
 	

# manager = RecipeManager()
# print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
# print(manager.add_ingredient("Torta di mele", "Zucchero"))
# print(manager.list_recipes()) # ['Torta di mele']
# print(manager.list_ingredients("Torta di mele"))
# print(manager.search_recipe_by_ingredient("Uova"))
# #



##################################################################

# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
# Attributi:

#     marca (stringa)
#     modello (stringa)
#     anno (intero)

# Metodi:

#     __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
#     descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     numero_porte (intero)

# Metodi:

#     __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
#     descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

# Metodi:

#     __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
#     descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".




class Veicolo:
    def __init__(self,marca : str,modello : str,anno : int) -> None:

        self.marca = marca
        self.modello = modello
        self.anno = anno

    
    def descrivi_veicolo(self):

        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

    

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int,numero_porte : int) -> None:

        self.numero_porte = numero_porte
        super().__init__(marca, modello, anno)


    def descrivi_veicolo(self):

        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
        


class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int,tipo : str) -> None:

        self.tipo = tipo
        super().__init__(marca, modello, anno)



    def descrivi_veicolo(self):

        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
        


# #
# veicolo = Veicolo("Generic", "Model", 2020)
# auto = Auto("Toyota", "Corolla", 2021, 4)
# moto = Moto("Yamaha", "R1", 2022, "sportiva")


# veicolo.descrivi_veicolo() 
# auto.descrivi_veicolo()
# moto.descrivi_veicolo()
# #


#######################################################################à


# Obiettivo
# L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

# Descrizione del problema
# Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
# - In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
# - n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
# Specifiche tecniche

# 1. Classe Specie
# - Attributi:

#     nome (str): Nome della specie.
#     popolazione (int): Popolazione iniziale.
#     tasso_crescita (float): Tasso di crescita annuo percentuale.

# - Metodi:

#     __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
#     cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
#     anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
#     getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².

 

# 2. Sottoclassi BufaloKlingon e Elefante
# Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
# Formule Matematiche:

#     Aggiornamento della popolazione per l'anno successivo:
#         Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
#     Calcolo della densità di popolazione:
#         Formula: popolazione / area_kmq
#         Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
#     Calcolo degli anni necessari per superare la popolazione di un'altra specie:
#         Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra. Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000. 

























