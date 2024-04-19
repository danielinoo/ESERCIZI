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


"""----------------------------------------------------------------------"""

#esercizio 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”


#variabili

nome : str = "Pirandello"
testo : str = "Imparerai a tue spese che nel lungo tragitto della vita incontrerai tante maschere e pochi volti."

print( f"{nome} una volta disse:\n\" {testo}\" ")
print("-----------------------")


"""----------------------------------------------------------------------"""

#esercizio 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.


file_name : str = "python-notes.txt"


#rimuove .txt dalla stringa
file_name =file_name.removesuffix(".txt")

print(file_name)
print("-----------------------")


"""----------------------------------------------------------------------"""

#esercizio 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

nomi : list = ["marco","luigi","leonardo","valerio"]

for i in range (len(nomi)):

    print(nomi[i])


print("-----------------------")


"""----------------------------------------------------------------------"""

#esercizio 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

nomi : list = ["marco","luigi","leonardo","valerio"]

mes : str = " come stai? ti saluto "
for i in range (len(nomi)):

    print(f"ciao,{nomi[i]}{mes}")

print("-----------------------")


"""----------------------------------------------------------------------"""

#esercizio 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

nomi : list = ["Rolls-Royce ","Lamborghini ","Ferrari" ,"Aston Martin ","Bentley"]

mes : str = " vorrei guidare una"
for i in range (len(nomi)):

    print(f"{mes} {nomi[i]}")

print("-----------------------")


"""----------------------------------------------------------------------"""

#esercizio 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

nomi : list = ["snoop dog ","Miriam Leone ","Ludovica Pagani "]

mes : str = "vieni a cena "
for i in range (len(nomi)):
    
    print(f"ciao {nomi[i]}{mes}")

"""----------------------------------------------------------------------"""


#esercizio 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
 #Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

print("\n")
print("snoop dog non può venire")
print("\n")

nomi[0] = "Angelina Mango "

for i in range (len(nomi)):
    
    print(f"ciao {nomi[i]}{mes}")

print("-----------------------")











