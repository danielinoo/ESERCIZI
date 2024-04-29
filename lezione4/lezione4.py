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
    

album1 = make_album("Pink Floyd","the wall")
print(album1)
print("-----")
album2 =make_album("Bob marley","Love songs",8)
print(album2)


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











