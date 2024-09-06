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
                 genere: str,
                 ore_lavorate : int)-> None:
        
        super().__init__(nome, cognome, data, genere)

        self.ore_lavorate : int = ore_lavorate


    def calcola_stipendio(self) -> float:

        return 500.0
    

##########################################

class professore(dipendente):
    def __init__(self, nome: str, 
                 cognome: str,
                 data: str, genere: str, 
                 ore_lavorate: int,
                 materia_insegnata: str,
                 ore_lezione : int) -> None:


        super().__init__(nome, cognome, data, genere, ore_lavorate)

        self.materia_insegnata : str = materia_insegnata
        self.ore_lezione : int = ore_lezione












##########################################

print(persona1.calcola_eta())

print("\n-------------\n")

dipendente1 : dipendente= dipendente(nome = "daniele",
                   cognome = "pietropaolo", 
                   data = "28/05/2004",
                   genere = "maschio",
                   ore_lavorate = 200)

print(dipendente1.name)
print("----")
print(dipendente1.calcola_eta())
print("----")
print(dipendente1.calcola_stipendio())
print("----")
print(dipendente1.ore_lavorate)

print("\n-------------\n")


prof1  : professore = professore( nome = "daniele",
                   cognome = "pietropaolo", 
                   data = "28/05/2004",
                   genere = "maschio",
                   ore_lavorate = 200,
                   materia_insegnata = "storia",
                   ore_lezione = 40)




print(prof1.ore_lezione)







print("\n-------------\n")






