#Daniele Pietropaolo
#6/05/24

class persona:

    def __init__(self,nome : str,
                 cognome : str,
                 data : str,
                 genere : str) -> None:
        
        self.name : str = nome
        self.cognome : str = cognome
        self.data_nascita : str = data
        self.genere : str = genere


    def calcola_eta(self) -> int:
        return 10
    


persona1 = persona(nome = "daniele",
                   cognome = "pietropaolo", 
                   data = "28/05/2004",
                   genere = "maschio")

################################################


class dipendente(persona):

    def __init__(self, nome: str,
                 cognome: str,
                 data: str,
                 genere: str) -> None:
        
        super().__init__(nome, cognome, data, genere)


    def calcola_stipendio(self) -> float:
        return 500.0












##########################################

print(persona1.calcola_eta())

print("\n-------------\n")

dipendente1 : dipendente= dipendente(nome = "daniele",
                   cognome = "pietropaolo", 
                   data = "28/05/2004",
                   genere = "maschio")

print(dipendente1.name)
print(dipendente1.calcola_eta())
print(dipendente1.calcola_stipendio())

print("\n-------------\n")











