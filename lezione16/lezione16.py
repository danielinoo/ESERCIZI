#Daniele Pietropaolo


# Obiettivo:
# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

# Specifiche della Classe Media:
 
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().





class Media:

    def __init__(self,title : str,reviews :list[int]) -> None:
        self.title = title
        self.reviews = reviews
        self.m : float = 0


    def set_title(self, title):
            
            self.title = title

    def get_title(self):
            return f"\nTitolo: {self.title}\n"


    def aggiungiValutazione(self, voto):
            

        if voto <= 5:
            
            self.reviews.append(voto)

        else:
            
            pass


    def getMedia(self):

        self.m : float =sum(self.reviews) / len(self.reviews)

        return self.m


    def getRate(self):
         
        if self.m <= 1.5:
             
             return "TERRIBILE"
        
        elif self.m <= 2.5:
             
             return "BRUTTO"

        elif self.m <=3.5:


            return "BELLO(ma se potevano impegna de più)"  

        elif self.m <= 4.5:
             
             return "BELLO"
        
        elif self.m > 5:
             
            return"GRANDIOSO"

                     
    

    def ratePercentage(self, voto):
        
        p : int =self.reviews.count(voto)

        percentuale = (len(self.reviews) * p) / 100

        return f"{percentuale}%"



    def recensione(self):   
        
        print(f"\ntitolo del film: {self.title}\n")
        print(f"\nvoto medio:{self.m}\n")

        print(f"\ngiudizio:{self.getRate()}\n")
        print(f"\nTerribile: {self.ratePercentage(1)}\n")
        print(f"\nBrutto:{self.ratePercentage(2)}\n")
        print(f"\nNormale:{self.ratePercentage(3)}\n")
        print(f"\nBello:{self.ratePercentage(4)}\n")
        print(f"\nGrandioso:{self.ratePercentage(5)}\n")


class Film(Media):
    def __init__(self, title: str, reviews: list[int]) -> None:
        super().__init__(title, reviews)


    def set_title(self, title):
        return super().set_title(title)
    
    def get_title(self):
        return super().get_title()
    
    def aggiungiValutazione(self, voto):
         return super().aggiungiValutazione(voto)
    
    def getMedia(self):
         return super().getMedia()
    
    def getRate(self):
         return super().getRate()
    
    def ratePercentage(self, voto):
         return super().ratePercentage(voto)
    



film_1 = Film("deadpool","non so")

film_1.set_title("deadpool")
    
film_1.aggiungiValutazione(3)
film_1.aggiungiValutazione(3)
film_1.aggiungiValutazione(3)
film_1.aggiungiValutazione(3)
film_1.aggiungiValutazione(3)
film_1.aggiungiValutazione(5)
film_1.aggiungiValutazione(1)

film_1.getMedia()
film_1.getRate()

film_1.recensione()





    

