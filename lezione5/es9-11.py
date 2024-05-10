#daniele pietropaolo

#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.




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


############################

class Privilegio:
    def __init__(self, privilegio : list[str]) -> None:
        self.privilegio = privilegio

    def show_privileges(self):

        for i in self.privilegio:
            print(i)

##########################################################

class admin(user):
    def __init__(self, nome: str, cogn: str, eta: int):
        self.nome = nome
        self.cognome = cogn
        self.eta = eta
        self.priv = Privilegio(privilegio=[])

    def show_privilege(self):

        self.priv.show_privileges()