#Pietropaolo Daniele
#18/04/24

import copy

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

#creazione lista
nomi : list = ["snoop dog ","Paolo Bonolis ","Francesco Totti "]

#creazione messaggio
mes : str = " vieni a cena "
for i in range (len(nomi)):
    
    print(f"ciao {nomi[i]}{mes}")

"""----------------------------------------------------------------------"""


#esercizio 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
 #Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

print("\n")
print("snoop dog non può venire")
print("\n")

#inserimento nuovo nome
nomi[0] = "Angelina Mango "

for i in range (len(nomi)):
    
    print(f"ciao {nomi[i]}{mes}")


#esercizio 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.


print("\n")
print("trovato un tavolo più grande ")
print("\n")

#inserimento altri nomi
nomi.insert(0,"The rock")
nomi.insert(2,"gigi proietti")
nomi.append("max verstappen")


for i in range (len(nomi)):
    
    print(f"ciao {nomi[i]}{mes}")

print("-----------------------")

print("\n")


#esercizio 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.




#messaggio disdetta tavolo ed eliminazione persone nella lista
while len(nomi) > 2:
    print(f"ciao {nomi.pop(0)},mi dispiace ma il tavolo è stato annullato",)

print("\n")



#messaggio di conferma dei due invitati ed eliminazione dalla lista
while len(nomi) > 0:
    print(f"ciao {nomi[0]} voi siente ancora invitati")
    del(nomi[0])
print(nomi)


print("tavolo annullato")

print("-----------------------")
print("\n")


"""----------------------------------------------------------------------"""


#esercizio 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.


#lista posti da visitare

v : list = ["cuba", "porto rico", "grecia","maldive", "costa del sol"]
print("lista originale: ",v)

#lista ordinata
v1  : list= sorted(v) #v1--> variabile di supporto
print("\nlista ordinata: ",v1)

#lista con ordine originale
print("\nlista originale: ",v)
v2 : list = v  #v2 --> seconda variabile di supporto

#lista modifica ordine inverso
v = v1 
v.reverse()
print("\nlista con ordine alfabetico inverso: ",v)

#lista ritorno ordine originale
print("\nlista con ritorno ad ordine originale: ",v2)

#lista con ordine alfabetico con SORT
v2.sort(reverse=False)
print("\nlista con ordine alfabetico con SORT: ",v2)

#lista con ordine alfabetico inverso con SORT
v2.sort(reverse=True)
print("\nlista con ordine alfabetico inverso con SORT: ",v2)


print("-----------------------")
print("\n")


"""----------------------------------------------------------------------"""

#esercizio 3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.

#numero di invitati alla cena(risulta zero perchè la lista èstata azzerata)
print(len(nomi))


print("-----------------------")
print("\n")


"""----------------------------------------------------------------------"""


#esercizio 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

#lista di paesi
p : list = ["italia","francia","germania","inghilterra","francia","giappone","croazia","spagna"]

print("lista di paesi: ",p)

#inserimento di un elemento alla fine,all inizio, in un punto a caso
p.append("irlanda")
p.insert(0,"messico")
p.insert(4,"grecia")

print("\nlista di paesi con l' inserimento di un elemento alla fine,all inizio, in un punto a caso: ",p)


# copia della lista di paesi ma senza gli ultimi 4 paesi


p2 : list = copy.deepcopy(p) #p2--> copia della lista P
c : int = 0#c --> contatore
p2 = p2[::-1]#inverto ordine lista
for i in range(len(p2)):

    print(f"\n{p2.pop(0)} eliminato dalla lista")
    c += 1

    if c == 4:
        break

#riposizionare l ' ordine della copia della lista nella versione originale 
p2.sort(reverse=True) 

print("\ncopia lista paesi P2 senza gli ultimi 4 paesi: ",p2)

#mettere la lista originale in ordine alfabetico
p.sort()
print("\nmettere la lista originale in ordine alfabetico: ",p)

#eliminare i duplicati cambiando la lista in un set
p = set(p)
print("\nlista originale trasformata in un set per l' eliminazione di duplicati:",p)



print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")


#esercizio 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

d : dict = {"nome": "marco", "cognome" :"rossi","eta": 19 , "citta": "roma"}
print(d)

dc6_7 : dict = copy.deepcopy(d)

print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")


#esercizio 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

#dizionario numeri fortunati
dii : dict = {"marco" : 69, "riccardo" : 4, "gaia" : 3, "daniele" : 23, "gianmarco": 9}

for k, v in dii.items():
    print(f"{k} {v}")



print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")

#esercizio 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.


#dizionario con parole e significato
dii2 : dict = {"tuple:" : "sono elementi sequenziali costituiti da una concatenazione di valori di qualsiasi tipo, ognuno memorizzato per posizione.Permettono la presenza di duplicati ma non sono modificabili.", "lista:" : "è una struttura dati sequenziale che memorizza gli elementi in un determinato ordine, ammette duplicati e permette di modificare gli oggetti che contiene.", "stringhe:":"valori di tipo testuale, cioè un insieme di caratteri inseriti tra apici o doppi apici, numeri e simboli compresi.", "int:" : "sono i numeri a virgola mobile, i numeri decimali. Ad esempio, 5.7 o 5.4", "boolean:": "calcolano un valore booleano, ossia un valore che può essere solo vero o falso"}

for k, v in dii2.items():

    print(f"{k}\n{v}")
    print("\n")






print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")


#esercizio 6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

d1 : dict = {"nome": "giuseppe", "cognome" :"bianchi","eta": 22 , "citta": "genova"}

d2 : dict = {"nome": "riccardo", "cognome" :"proietti","eta": 23 , "citta": "milano"}

person : list = [dc6_7, d1, d2] #lista con i tre dizionari dentro


for i in person:

    print(f"{i} \n")


print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")

#esercizio 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet. 


dp1: dict = {"tipo" :"gatto" , "specie" :"siamese" , "proprietario": "Marco"}

dp2 : dict = {"tipo" :"cane" , "specie" :"pitbull" , "proprietario": "Francesco"}

dp3 : dict = {"tipo" :"cane" , "specie" :"carlino" , "proprietario": "Roberto"}

dp4 : dict = {"tipo" :"gatto" , "specie" :"persiano" , "proprietario": "Maria"}

dp5 : dict = {"tipo" :"uccello" , "specie" :"ara" , "proprietario": "Giada"}

pets :  list = [dp1, dp2,dp3,dp4,dp5] #lista con i dizionari dentro

for i in pets:

    print(f"{i} \n")


print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")

#esercizio 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places : dict = {"Aldo" : "Rambla, central park, fotana di trevi ", "Giovanni" : "Courmayeur", "Giacomo" : "Copagabana, time square"}

for k, v in favorite_places.items():

    print(f"{k}: {v} \n")



print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")

#esercizio 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.


#.update--> modica valori dentro il dizionario
dii.update({"marco" : "34,7"})

dii.update({"riccardo" : "4,30"})

dii.update({"gianmarco" : "9,21"})

dii.update({"daniele" : "23,30,9"})

dii.update({"gaia" : "3,56,2"})

for k, v in dii.items():

    print(f"{k}: {v} \n")


print("\n")
print("-----------------------")
"""----------------------------------------------------------------------"""
print("\n")

#esercizio 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.




