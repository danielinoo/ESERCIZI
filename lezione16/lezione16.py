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


    def create_recipe(self,name, ingredients):

        if name not in self.collezione:

            self.collezione[name] = self.l.append(ingredients)
            return self.collezione[name]

        else:

            return "errore"



    def add_ingredient(self,recipe_name, ingredient):

        if recipe_name in self.collezione:
            self.collezione[recipe_name].append(ingredient)
            return self.collezione[recipe_name]


    def remove_ingredient(self,recipe_name, ingredient):

        if recipe_name in self.collezione:
            self.collezione[recipe_name].remove(ingredient)
            return self.collezione[recipe_name]


    def update_ingredient(self,recipe_name, old_ingredient, new_ingredient):

        
        if recipe_name in self.collezione:

            if old_ingredient in self.collezione[recipe_name]:

                self.collezione[recipe_name] = self.l.remove(old_ingredient)
                self.collezione[recipe_name] = self.l.append(new_ingredient)
                return self.collezione[recipe_name]
        
            else:
                return "l ingrediente non esiste"
        
        
        else:
            return "la ricetta non esiste"


    def list_recipes(self): 

        l2 : list[str] = []
        return f"{l2}"

    def list_ingredients(self,recipe_name):

        if recipe_name in self.collezione:
            return f"{self.collezione.values(recipe_name)}"
        
        else:
            return "la ricetta non esiste"

    def search_recipe_by_ingredient(self,ingredient): 

        l1 : list[str] = []
        
        for k,v in self.collezione.items():

            if ingredient in k:

                l1.append(k)


        if len(l1) != 0:

            return l1
        
        else:

            return "errore la ricetta non esiste"



#
 	

manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))
#


