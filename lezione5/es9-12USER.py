#daniele pietropaolo
#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.


class user:                                       
    def __init__(self,nome : str,cogn : str, eta : int):

        self.name = nome
        self.lname = cogn
        self.age = eta
        self.login_attempts = 0


    def great_user(self):

        print(f"ciao {self.name} sei un grande!")


    #ritarna una stringa
    def __str__(self) -> str:
        return f"user name : {self.name}\nlast name : {self.lname}\nage : {self.age}"
    

    
    print("---")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0