#Daniele Pietropaolo

# Creare un file chiamato "dottore.py".
# In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

# Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale), ed una parcel per le visite in studio (si usi il tipo float). Gli attributi della classe dottore devono essere anch'essi privati.

# - Definire i seguenti metodi:

#     costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcel (parcel). Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcel inserita non è un float!".
#     setSpecialization(specialization): consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".
#     setParcel(parcel): consente di impostare la parcel di un dottore, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario, stamapre un messaggio di errore, ad esempio "La parcel inserita non è un float!".
#     getSpecialization(): consente di ritornare la specializzazione del dottore.
#     getParcel(): consente di ritornare la parcel del dottore.
#     isAValidDoctor(): stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. In caso contrario, stampare "Doctor nome e cognome is not valid!".
#     doctorGreet():tale metodo richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto "Sono un medico {specializzazione}"



from gestione_ospedale.persona import Persona


class Dottore(Persona):

    def __init__(self, first_name, last_name,specialization : str,parcel : float) -> None:
        super().__init__(first_name, last_name)

        self.specialization = specialization



        if isinstance(parcel,float):

            self.parcel = parcel

        else:

            print("la parcella inserita non è di tipo float!")
        self.parcel = parcel

    
    #####################################


    def setSpecialization(self,specialization):

        if isinstance(specialization,str):

            self.specialization = specialization

        else:

            print("la specializzazione inserita non è una stringa!")


    #####################################   


    def setParcel(self,parcel):

        if isinstance(parcel,float):

            self.parcel = parcel

        else:

            print("la parcella inserita non è di tipo float!")
        self.parcel = parcel

    ############################


    def getSpecialization(self):

        return self.specialization


    ########################

    def getParcel(self):

        return self.parcel
    

    ############################

    def isAValidDoctor(self):


        if self.age > 30:

            print(f"Doctor {self.first_name} {self.last_name}is valid!")
            return 1


        else:

            print(f"Doctor {self.first_name} {self.last_name}is not valid!")
            return 0


    ############################

    
    def doctorGreet(self):

        self.greet()
        print(f"Sono un medico {self.specialization}")




    





    


