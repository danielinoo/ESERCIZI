#daniele pietropaolo
#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from lezione5 import user

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