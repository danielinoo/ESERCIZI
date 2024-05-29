#Daniele Pietropaolo


#dichiarazione classe astratta
from abc import ABC,abstractmethod

class AbcAnimal(ABC): 



    @abstractmethod #dichiarazione metodo astratto
    def verso():

        pass



class Cane(AbcAnimal):

    def __init__(self,nome : str) -> None:
        super().__init__()

        self.nome = nome

        self.velocita : float = 10.0




    def verso(self):
         print("BAU!")
    

    def movimento(self,t : int):

        print(self.velocita * t)
    








class Gatto(AbcAnimal):

    def __init__(self,nome : str) -> None:
        super().__init__()

        self.nome = nome

    def verso(self):
        return print("MIAO!")
    




"""

cane_1 : Cane = Cane(nome = "pluto")

cane_1.verso()

cane_1.movimento(t = 10)


gatto_1 : Gatto = Gatto(nome = "giggi")

gatto_1.verso()"""




#######################################################


class ContoBancario:

    total_account = 0
    def __init__(self,iban,saldo,nome) -> None:

        self.iban = iban
        self.saldo = saldo
        self.nome = nome

        ContoBancario.total_account += 1


    def deposito(self,importo):

        self.saldo += importo
        print(f"{importo} depositato. Il nuovo saldo è {self.saldo}")


    def prelievo(self,importo):

        self.saldo -= importo
        print(f"{importo} prelevato. Il nuovo saldo è {self.saldo}")


    @classmethod  #classmethod --> assegna una funzione alla classe e non a una variabile tipo funzione locale (ContoBancario.gets_account)
    def get_accounts(cls):
        print(f"totale account creati {cls.total_account}")


    @staticmethod #staticmethod --> funzione che si trova all' interno della classe ma  prende parametri "esterni" non da SELF(puo sta tranquillamente fori ma logicamente sta mejo dentro la classe)
    def vailida_account(iban):
        if isinstance(iban,int) and len(str(iban)) == 10:    #insinstance -> controlla se la varibile (iban) corrisponde alla tipologia specificata (int)

            print("valido")
            return True

        else:

            print("invalido")
            return False



account1 = ContoBancario(1234567890,0,"ALICE")
account2 = ContoBancario(9876543210,1000,"ROBERTO")

account1.deposito(500)
account1.prelievo(200)

account2.deposito(200)
account2.prelievo(150)

ContoBancario.get_accounts()

ContoBancario.vailida_account(1234567890)
ContoBancario.vailida_account("1234567890")




class Banca:

    def __init__(self,nome,indirizzo) -> None:
        self.nome = nome
        self.indirizzo = indirizzo

        











    
















    




    

