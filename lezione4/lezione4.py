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













