#Pietropaolo Daniele
#18/04/24

print("-----------------------")
print("hello word")
print("-----------------------")

#esercizio 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

nome : str = "Mario"

#mes: variabile che contiene il messaggio
mes : str = f"ciao {nome}, ti va di imparare un po di python insieme?"
print(mes)
print("-----------------------")


"""----------------------------------------------------------------------"""

#esercizio 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name : str = "Marco"

#n_u = name_upper ----> nome maiuscolo
#n_l = name_lower -----> nome minuscolo
n_u : str = name.upper()
n_l : str = name.lower()


#stampa i nomi in maiscolo,minuscolo e "come scritto"
print(f" {name}, {n_u}, {n_l}")
print("-----------------------")

# METODO COMPRESSO   ------>   print(f" {name}, {name.upper()}, {name.lower()}")




