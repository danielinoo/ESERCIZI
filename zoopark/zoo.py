#daniele pietropaolo
#5/05/24


#-------------------------------#

class zoo_keepers:

    def __init__(self,n : str,c : str,idi : str):

        self.nome = n
        self.cognome = c
        self.id = idi


#-------------------------------#

class animal:

    def __init__(self,name : str,spieces: str,eta : int,alt : float,larg : float,habitat : str):

        self.name_a = name
        self.spieces = spieces
        self.age_s = eta
        self.height = alt
        self.width = larg
        self.prefer_habitat = habitat


#-------------------------------#

class fence:
    def __init__(self,area : float,temperature :float,habitat : str):

        self.area = area
        self.temperature = temperature
        self.habitat = habitat


#-------------------------------#


class zoo:
    def __init__(self,recinto : list[fence],guardia : list[zoo_keepers]):

        self.rec = recinto
        self.gu = guardia



#-------------------------------#









