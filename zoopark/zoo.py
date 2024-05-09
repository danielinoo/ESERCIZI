#daniele pietropaolo
#5/05/24


#-------------------------------#

class Animal:

    def __init__(self,name : str,spieces: str,eta : int,height : float,width : float,prefer_habitat : str):

        self.name = name
        self.spieces = spieces
        self.age = eta
        self.height = height
        self.width = width
        self.prefer_habitat = prefer_habitat


        self.health = round(100 * (1 /self.age), 3)



#-------------------------------#

class Fence:
    def __init__(self,animals : list[Animal],area : float,temperature :float,habitat : str):

        self.animals = animals
        self.area = area
        self.temperature = temperature
        self.habitat = habitat



#-------------------------------#



class zoo_keepers:

    def __init__(self,nome : str,cognome : str,id : str):

        self.nome = nome
        self.cognome = cognome
        self.id = id

    def add_animal(animal: Animal, fence: Fence):

        if animal.prefer_habitat != fence.habitat and fence.area < animal.height*animal.width:
            pass

        
        else: 
            #lista degli animali del recinto aggiunge un nuovo animale
            fence.animals.append(animal)

            #sottraggo all' area del recinto l'area del nuovo animale
            fence.area = fence.area - (animal.height * animal.width)


    def remove_animal(animal: Animal, fence: Fence):

        #lista degli animali del recinto rimuove l animale
        fence.animals.remove(animal)

        #aggiungo all'area del recinto l'area dell'animale appena uscito
        fence.area = fence.area + (animal.height*animal.width)



    def feed(animal: Animal):    

        while Fence.area >= animal.height * animal.width:

            #aumento salute animale del 1%
            animal.health = animal.health * 1.01

            #aumento altezza e larghezza del 2%
            animal.height = animal.height * 1.02
            animal.width : float = animal.width * 1.02

        


#######################TEST PRINT######################



class zoo:
    def __init__(self,fence : list[Fence],zoo_keepers : list[zoo_keepers]):

        self.fence = fence
        self.zoo_keepers = zoo_keepers



#-------------------------------#









