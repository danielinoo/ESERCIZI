def frequency_dict(elements: list) -> dict:
    
    d : dict[str,int] = {}
   
    for i in elements:
       
        if i not in d:
       
            d[i] = elements.count(i)
            
    return d


###########################################à
def check_access(username: str, password: "12345", is_active: bool) -> str:
    
    if username == "admin" and password ==  "12345" and is_active == True:
        return  "Accesso consentito"
        
    else:
        return "Accesso negato"
 	


##############################################


def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    d : dict[str,list[int]] = {}


    for i in tuples:

        if i[0] not in d:

            l : list = []
            l = [i[1]]

            d[i[0]] = l

        else:
            l.append(i[1])
            d[i[0]] = l


    return d






##################################################

def sum_above_threshold(numbers: list[int],threshold : int) -> int:
    s = 0
   
    for i in numbers:
       
       if i > threshold:
           
           s += i
           
           
           
    return s


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
            self.ricette[name]= ingredients
            return self.ricette
        else:
            return "errore la ricetta esiste già"
        
    def add_ingredient(self,recipe_name, ingredient): 

        if recipe_name in self.ricette:
                if ingredient not in self.ricette[recipe_name] :
                    self.ricette[recipe_name].append(ingredient)
                    return self.ricette
        else:
            return "errore l' ingrediente esiste già"
        
    def  remove_ingredient(self,recipe_name, ingredient):

        if recipe_name in self.ricette \
        and ingredient in self.ricette[recipe_name]:
            self.ricette[recipe_name].remove(ingredient)
            return self.ricette
        else:
            return "errore la ricetta non eiste o l' ingrediente non è presente"
        
    def update_ingredient(self,recipe_name, old_ingredient, new_ingredient):
        if recipe_name in self.ricette \
        and old_ingredient in self.ricette[recipe_name]:   
            a : int = self.ricette[recipe_name].index(old_ingredient)
            self.ricette[recipe_name].insert(a,new_ingredient)
            self.ricette[recipe_name].remove(old_ingredient)
            return self.ricette
        else:
            return "errore la ricetta non eiste o l' ingrediente non è presente"
        
    def list_recipes(self):
        l : list[str]= []

        for k,v in self.ricette.items():
            l.append(k)

            return l
    
    def list_ingredients(self,recipe_name):

        if recipe_name in self.ricette:
            return self.ricette[recipe_name]
        else:
            "errore la ricetta non esiste"

    def search_recipe_by_ingredient(self,ingredient):
        l: list[str] = []
        for k,v in self.ricette.items():
            for i in v:
                if ingredient == i:
                    return self.ricette
        return"errore nessuna ricetta contiene l' ingrediente"



############################################

def seconds_since_noon(ore : int,minuti : int,secondi : int):

    ore = ore - 12

    #calcolo secondi
    ris : int = (ore * 3600) + (minuti * 60) + secondi

    return ris

def time_difference(ore1 : int,minuti1 : int,secondi1 : int,ore2 : int,minuti2 : int,secondi2 : int):

    orario1 = seconds_since_noon(ore1,minuti1,secondi1)
    orario2 = seconds_since_noon(ore2,minuti2,secondi2)

    quantita_tempo = orario1 - orario2
    return abs(quantita_tempo)
