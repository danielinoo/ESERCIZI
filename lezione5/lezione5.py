#Pietropaolo Daniele
#5/05/2024

#esercizio 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

	
class restaurant:

    def __init__(self,ristorante : str,cucina : str) -> None:
        
        self.ris : str = ristorante
        self.cuc : str = cucina

    def des_restaurant(self):

        print(f"nome ristorante: {self.ris} co cucina di tipo {self.cuc}\n")


    def open_restaurant(self):
        print(f"il nuovo ristorante {self.ris} è aperto!")


r1 = restaurant(ristorante= "Da Baffo",cucina="romana")

r1.des_restaurant()
r1.open_resaturant()


print("\n----------------------------------------------\n")


#esercizio 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

class user:                                       
    def __init__(self,nome : str,cogn : str, eta : int):

        self.name = nome
        self.lname = cogn
        self.age = eta
        
        #es 9-5
        self.login_attempts = 0


    def great_user(self):

        print(f"ciao {self.name} sei un grande!")


    #ritarna una stringa
    def __str__(self) -> str:
        return f"user name : {self.name}\nlast name : {self.lname}\nage : {self.age}"
    

    #esercizio 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
    print("---")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



r2 = user("marco","rossi",23)
r2.great_user()
print(r2)

print("---") #es9-5

#incremento numero di accessi dell'utente
r2.increment_login_attempts()
r2.increment_login_attempts()
r2.increment_login_attempts()
print("tentativi di accesso:\n",r2.login_attempts)

#resetto il numero di acessi
r2.reset_login_attempts()
print("tentativi di accesso:\n",r2.login_attempts)
print("\n----------------------------------------------\n")


#esercizio 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
	
class Restaurant:

    def __init__(self,ristorante : str,cucina : str, num : int) -> None:
        
        self.ris : str = ristorante
        self.cuc : str = cucina
        self.num_served = num

    def des_Restaurant(self):

        print(f"nome ristorante: {self.ris} co cucina di tipo {self.cuc}\n")


    def open_Restaurant(self):
        print(f"il nuovo ristorante {self.ris} è aperto!")

    def set_numer_served(self,new_number_served : int):

        self.num_served = new_number_served

    def increment_number(self):
        self.num_served += 1
    

r3 = Restaurant(ristorante= "Da Baffo",cucina="romana",num= 2)



print(r3.num_served)
r3.set_numer_served(4)
print(r3.num_served)
r3.increment_number()
print(r3.num_served)



print("\n----------------------------------------------\n")

#esercizio 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 


class IceCreamStand(Restaurant):
    def __init__(self, ristorante: str, cucina: str, num: int,sapori : list [str]) -> None:

        super().__init__(ristorante, cucina, num)
        self.sapori = sapori

    def gelato(self):

        for i in self.sapori:
            print(i)




ic = IceCreamStand(ristorante="bruno",
                   cucina="romana",
                   num= 10,
                   sapori=["cioccolato","fiordilatte","crema","fragola"])

ic.gelato()


print("\n----------------------------------------------\n")

#esercizio 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 

class admin(user):
    def __init__(self, nome: str, cogn: str, eta: int,privilegi : list[str]):

        super().__init__(nome, cogn, eta)


        self.privilegi = privilegi

    def show_privileges(self):

        for i in self.privilegi:
            print(i)



ad = admin("amministratore",
            "am",
           30,
           ["può aggiungere post", "può eliminare post", "può eliminare i commenti l'utente"])

ad.show_privileges()



print("\n----------------------------------------------\n")
#esercizio 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

class Privilegio:
    def __init__(self, privilegio : list[str]) -> None:
        self.privilegio = privilegio

    def show_privileges(self):

        for i in self.privilegio:
            print(i)


        



class admin(user):
    def __init__(self, nome: str, cogn: str, eta: int):
        self.nome = nome
        self.cognome = cogn
        self.eta = eta
        self.priv = Privilegio(privilegio=[])

    def show_privilege(self):

        self.priv.show_privileges()



ad1 = admin("gigi","proietti",70)


ad1.priv.privilegio = ["può aggiungere post", "può eliminare post", "può bloccare l'utente"]


ad1.show_privilege()

print("\n----------------------------------------------\n")
#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.


import random
class die:
    def __init__(self,lati : int = 6) -> None:
        self.lati = lati

    def roll_die(self):
        self.lati = random.random(1,6)
        print(self.lati)
        

        






print("\n----------------------------------------------\n")




