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

    def add_animal(self,animal: Animal, fence: Fence):

        if animal.prefer_habitat != fence.habitat and fence.area < animal.height*animal.width:
            pass
            
        
        else: 
            #lista degli animali del recinto aggiunge un nuovo animale
            fence.animals.append(animal)

            #sottraggo all' area del recinto l'area del nuovo animale
            fence.area = fence.area - (animal.height * animal.width)

        
        
        

    
        




    def remove_animal(self,animal: Animal, fence: Fence):

        #lista degli animali del recinto rimuove l animale
        fence.animals.remove(animal)

        #aggiungo all'area del recinto l'area dell'animale appena uscito
        fence.area = fence.area + (animal.height*animal.width)

        


    def feed(self,animal: Animal): 


        while Fence >= animal.height * animal.width:

            #aumento salute animale del 1%
            animal.health = animal.health * 1.01

            #aumento altezza e larghezza del 2%
            animal.height = animal.height * 1.02
            animal.width = animal.width * 1.02

            return animal.health,animal.height
        

    def clean(fence: Fence) -> float:

        if fence.area == 0:
            return "area occupata"

        #area occupata dagli animali
        area_animali : float = 0

        for i in fence.animals:
            area_animali = fence.animals.height * fence.animals.width

        if fence.area / area_animali <= 0:
            return "area occupata"
        else:
            return fence.area / area_animali






        




#######################TEST PRINT######################

c1 = Animal("pippo", "lupo",20,4,5,"bosco")
c2 = Fence(animals= ["francesco"],area= 50, temperature= 20,habitat="bosco")
c3 = zoo_keepers("franco","rossi","1234")

print(c3.feed(c1))





class zoo:
    def __init__(self,fence : list[Fence],zoo_keepers : list[zoo_keepers]):

        self.fence = fence
        self.zoo_keepers = zoo_keepers


    def describe_zoo(self):

        print("\nGuardians:\n")
        print(f"{self.zoo_keepers}\n")


        for i in self.fence:
            print("Fence:\n")
            print(f"{self.fence}")





#-------------------------------#









