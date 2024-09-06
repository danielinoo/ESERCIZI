#daniele pietropaolo

#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

from lezione5 import admin

ad = admin("franchino","0139",45)

ad.priv.privilegio = ["amministratore puo gestire i commenti degli utenti","bloccare/eliminare utenti"]

ad.show_privilege()