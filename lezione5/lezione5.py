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


#esercizio 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

class user:
    def __init__(self,nome : str,cogn : str, eta : int):

        self.name = nome
        self.lname = cogn
        self.age = eta


    def great_user(self):

        print(f"ciao {self.name} sei un grande!")


    #ritarna una stringa
    def __str__(self) -> str:
        return f"user name : {self.name}\nlast name : {self.lname}\nage : {self.age}"
    

r2 = user("marco","rossi",23)

r2.great_user()
print(r2)


print("\n----------------------------------------------\n")

#esercizio 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 



	
class resturant:

    def __init__(self,ristorante : str,cucina : str, num : int) -> None:
        
        self.ris : str = ristorante
        self.cuc : str = cucina
        self.num_served = num

    def des_resturant(self):

        print(f"nome ristorante: {self.ris} co cucina di tipo {self.cuc}\n")


    def open_resturant(self):
        print(f"il nuovo ristorante {self.ris} è aperto!")

    def set_numer_served(self,new_number_served : int):

        self.num_served = new_number_served

    def increment_number(self):
        self.num_served += 1


    

r3 = resturant(ristorante= "Da Baffo",cucina="romana",num= 2)



print(r3.num_served)
r3.set_numer_served(2)
print(r3.num_served)
r3.increment_number()
print(r3.num_served)



print("\n----------------------------------------------\n")

#esercizio 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.






