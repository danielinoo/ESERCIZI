#Daniele Pietropaolo
#29/04/24

#esercizio 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

def display_message():
    mes : str ="in questo capitolo stiamo imparando le funzioni"

    return mes

print(display_message())

print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(tit : str) -> str:

    par = f"uno dei miei libri preferiti è {tit}"

    return par

print(favorite_book("Gomorra"))


print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

#funzione
def make_shirt(taglia : str, mes : str) -> str:

    maglietta : str = f"la taglia della maglietta è {taglia} e il messaggio da stampare sopra è \"{mes}\""
    
    return maglietta



#primo caso
print(make_shirt("M","DAJE ROMA"))

print("-----")

#secondo caso
print(make_shirt(taglia = "L", mes ="star wars"))

print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message

def make_shirt(taglia = "L", mes ="i love python") -> str:

    
    maglietta : str = f"la taglia della maglietta è {taglia} e il messaggio da stampare sopra è \"{mes}\""
    
    return maglietta

print(make_shirt())

print("-----")

print(make_shirt("M"))

print("-----")

print(make_shirt("S","LAURENTINA"))


print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
def  describe_city(citta : str,paese : str = "messico"):

    print(f"{citta}, si trova in {paese}")
    print("-----")

describe_city("citta del messico")
describe_city("dublino","irlanda")
describe_city("miami","florida")



print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
def describe_city(citta : str, paese : str) -> str:

    print(f"\"{citta}, {paese}\"")
    print("-----")

describe_city("Roma","Italia")
describe_city("Parigi","Francia")
describe_city("Londra", "Regno unito")


print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

def  make_album(artista : str,nomA : str,numero_brani : None = None)-> dict:
    
    album = {"artista": artista,"album": nomA}

    if numero_brani:
        album["numero brani"] = numero_brani

    return album
    

print( make_album("Pink Floyd","the wall"))
print("-----")
print(make_album("Bob marley","Love songs",8))


print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-8. User Albums:Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

while True:

    artista = input("inserisci il nome dell'artista\n")
    nomA = input("inserisci il nome dell' album\n")
    numero_brani = input("inserisci il numero di brani dell' album (non obbligatorio premere invio per saltare)\n")

    print("\n",make_album(artista,nomA),"\n")

    print("-----")
    risposta : str= input("\n vuoi terminare? (scrivi si)\n")
    print("-----")
    if risposta == "si":
        break


print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

lisMes = ["ciao","come va","tutto bene","io sto andando a lavoro"]

def show_messages(lisMes : list) -> list:

    for i in lisMes:
        print(i,"\n")


show_messages(lisMes)


print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly
#esercizio 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

def  send_messages(lisMes : list) -> list:

    copiaMes : list = []
    for i in lisMes:
        print(i,"\n")
        copiaMes.append(i)
    
    print(copiaMes,lisMes)
    print("-----")   
    

send_messages(lisMes)


print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.


def sandwiches(ni : int) -> list:

    panino : list = []
    for i in range(ni):
        ing : str = input("\ninserire un ingradiente:\n")
        panino.append(ing)

    print("\npanino finito ,il tuo panino è:\n",panino)

sandwiches(2)
print("-----")
sandwiches(3)
print("-----")
sandwiches(4)

print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""
# esercizio 8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def  build_profile(nome : str,cognome : str,eta : int,colore_capelli : str,peso : int):
    profile : str =f"{nome} {cognome},eta {eta}, capelli {colore_capelli},peso {peso}"

    print(profile)

build_profile("Daniele","Pietropaolo",19, "neri",55)

print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""

#esercizio 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 

def auto(produttore : str,modello : str, **altreInfo) -> dict:

    car : dict = {"produttore" : produttore,"modello" : modello}

    car.update(altreInfo)

    print(car)

auto("toyota","fuoristrada",colore = "blu")

print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""
#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *

import module_name
print(module_name.fra("marco"))
print("-----")

from module_name import fra
print(fra("francesco"))
print("-----")

from module_name import fra as ns
print(ns("giggi"))
print("-----")

import module_name as mn
print(mn.fra("peppe"))
print("-----")

from module_name import*
print(fra("antonio"))
print("-----")



print("\n|--------------------------------------|\n")
"""---------------------------------------------------------------------------------------------------------------------------"""
#esercizio 8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.

#Styling Functions es 8-14
def auto(produttore : str,modello : str, **altreInfo) -> dict:

    car : dict = {"produttore" : produttore,"modello" : modello}

    car.update(altreInfo)

    for k,v in car.items(): 
        print(f"{k} {v}\n")

auto("toyota","fuoristrada",colore = "blu")

print("\n||||||||||||||\n")

#Styling Functions es 8-13

def  build_profile(nome : str,cognome : str,eta : int,colore_capelli : str,peso : int):
    profile : str =f"{nome} {cognome}\neta {eta}\ncapelli {colore_capelli}\npeso {peso}"

    print("profilo:\n",profile)

build_profile("Daniele","Pietropaolo",19, "neri",55)


print("\n||||||||||||||\n")

#Styling Functions es 8-12
def sandwiches(ni : int) -> list:

    panino : list = []
    for i in range(ni):
        ing : str = input("\ninserire un ingradiente:\n")
        panino.append(ing)

    print("\npanino finito ,il tuo panino è:\n")

    for i in panino:
        print(i)

sandwiches(2)
print("-----")
sandwiches(3)
print("-----")
sandwiches(4)
