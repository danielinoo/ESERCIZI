#Danile Pietropaolo
#Esercizi opzionali lezione5

# esercizio 1. Create a Playlist:

#Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. The function should return a dictionary with the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.

#Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

#Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.

#Example: add_like(dictionary, “Road Trip”, liked=True)


def create_playlist(nome : str,*args : str):


    d : str = {}

    s : set = set(args)


    d[nome] = s


    print(d,"\n")


create_playlist("Road Trip", "Song 1", "Song 2")



def add_like(v : str,b : bool):

    d : dict = {}

    d[v] = b

    print("dictionary",v,"apprezzato",b)


add_like("road trip", True)




        
print("\n-------------------------------------\n")


###############################################


def add_book(autore : str,*args : str):

    d : dict = {}
    l : list = list(args)

    d[autore] = l


    print(d)

add_book("Mark Twain", "Le avventure di Tom Sawyer", "Life on the Mississippi")








print("\n-------------------------------------\n")


###############################################











