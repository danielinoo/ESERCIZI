#daniele pietropaolo
#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.


from lezione5 import admin 

ad = admin("giuseppe","bianchi",20)

ad.priv.privilegio = ["l amministratore gestisce i commenti degli utenti","può segnalare gli utenti"]

ad.show_privilege()