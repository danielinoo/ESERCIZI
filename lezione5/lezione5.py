#Pietropaolo Daniele
#5/05/2024

#esercizio 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

	
class resturant:

    def __init__(self,ristorante : str,cucina : str) -> None:
        
        self.ris : str = ristorante
        self.cuc : str = cucina

    def des_resturant(self):

        print(f"nome ristorante: {self.ris} co cucina di tipo {self.cuc}\n")


    def open_resturant(self):
        print(f"il nuovo ristorante {self.ris} è aperto!")


r1 = resturant(ristorante= "Da Baffo",cucina="romana")

r1.des_resturant()
r1.open_resturant()


print("\n----------------------------------------------\n")

