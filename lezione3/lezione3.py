#Daniele Pietropaolo
#27/04/24

import copy

#esercizio 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!


pizza : list = ["margherita", "margherita con wustel", "boscaiola"]
mes : str = "mi piace davvero la pizza"

#ciclo che stampa il singolo nome
for i in pizza:
    print(i,"\n")

print("\n---\n")

#ciclo che stampa la frase
for i in pizza:
    print(f"{mes} {i}\n")

print("adoro la pizza")

print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")

#esercizio 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!


animali : list = ["cane", "gatto", "pappagallo"]
mess : str = "sarebbe un ottimo animale da compagnia"

for i in animali:
    print(i,"\n")

print("\n---\n")

for i in animali:
    print(f"un {i} {mess}\n")

print("ognuno di questi animali sarebbe un ottimo animale domestico")


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")

#esercizio 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.



for i in range(1,21):
    print(i)




print()
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")


#esercizio 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)


#per avviare i numeri da 1 a un milione togliere il "#" affianco al for e al print
#for i in range(1,10000001):
    #print(i)



print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")

#esercizio 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.


num : list =list(range(1,1000001))

#numero minimo e numero massimo
print(min(num))
print(max(num))


#aggiunge un milione con sum()
sm = sum(num)
print(sm)

print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")   


#esercizio 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

#lista di numeri dispari
x = list(range(1, 20, 2))

for n in x:
  print(n)


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  


#esercizio 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

x = list(range(3,31,3))

for i in x:
    print(i)


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  


#esercizio 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.


cubo : list = []

for i in range(1,11):
   c : int= i**3
   cubo.append(c)

print(cubo)

print("---")

#esercizio 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

for i in cubo:

    print(i)


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  

#esercizio 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.



#primi tre numeri della lista dei multipli di tre
print("i primi tre numeri della lista di multipli di tre sono: ", x[0], x[1], x[2])
print("---")

#i tre numeri al centro della lista
print("i tre numeri in mezzo alla lista dei multipli di tre sono: ",x [4], x[5],x[6])
print("---")

#i tre numeri alla fine della lista

x.sort(reverse=True)
print("i numeri alla fine della lista dei multipli di tre sono: ", x[0], x[1], x[2])


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  



#esercizio 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.


#copia della lista "pizza"
friend_pizzas = copy.deepcopy(pizza)

pizza.append("capricciosa")
friend_pizzas.append("diavola")

#stampa della lista originale ("pizza")
print("le mie pizze preferite sono: \n",pizza)

print("---")

#stampa della copia della lista("friend_pizzas")
print("le pizze preferite dei miei amici sono:\n ",friend_pizzas)


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  

#esercizio 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

#stampa della lista originale ("pizza")
print("le mie pizze preferite sono: \n")
for i in pizza:
    print(i)

print("---")

#stampa della copia della lista("friend_pizzas")
print("le pizze preferite dei miei amici sono:\n ")

for i in friend_pizzas:
    print(i)


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  


#esercizio 4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.










print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  


#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.

macchina1 : str = "audi"
print("audi è un marchio di un auto?")
if macchina1 == "audi":
    print(True,"\n")

print("balocco è un marchio di un auto?")
if macchina1 != "balocco":

    print(False,"\n")

print("---")


macchina2 : str = "bmw"
print("bmw è un marchio di un auto?")
if macchina2 == "bmw":
    print(True,"\n")

print("feltrinelli è un marchio di un auto?")
if macchina2 != "feltrinelli":

    print(False,"\n")

print("---")

macchina3 : str = "fiat"
print("fiat è un marchio di un auto?")
if macchina3 == "fiat":
    print(True,"\n")

print("lenovo è un marchio di un auto?")
if macchina3 != "lenovo":

    print(False,"\n")

print("---")


macchina4 : str = "mercedes"

print("mercedes è un marchio di un auto?")
if macchina4 == "mercedes":
    print(True,"\n")

print("lavazza è un marchio di un auto?")
if macchina4 != "lavazza":

    print(False,"\n")

print("---")


macchina5 : str = "maserati"
print("maserati è un marchio di un auto?")
if macchina5 == "maserati":
    print(True,"\n")

print("nike è un marchio di un auto?")
if macchina5 != "nike":

    print(False,"\n")


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n") 

#esercizio 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


alien_color = "verde"

if alien_color == "verde":

    print("il giocatore1 ha appena ottenuto 5 punti")

if alien_color == "rosso":

    pass


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n") 

#esercizio 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and another that runs the else block.

alien_color2 : str = "rosso"

if alien_color2 == "verde":

    print("complimenti hai guadagnato 5 punti per aver sparato all' alieno")

else:

    print("complimenti hai guadagnato 10 punti")

print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n") 



#esercizio 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color2 : str = "rosso"

if alien_color2 == "verde":
    
    print("complimenti hai guadagnato 5 punti")

elif alien_color2 == "giallo":

    print("complimenti hai guadagnato 10 punti")

else:

    print("complimenti hai guadagnato 15 punti")


print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n") 

# esercizio 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.

eta : int = 17

if eta < 2:
    print("la persona è un neonato")

elif eta > 2 and eta < 4:

    print("la persona è un bambino piccolo")

elif eta >= 4 and eta < 13:

    print("la persona è un bambino")

elif eta >= 13 and eta < 20:

    print("la persona è un adolescente")

elif eta >= 20 and eta < 65:

    print("la persona è maggiorenne")

else:

    print("la persona è un anziano") 

print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")

#esercizio 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!

favorite_fruit : list = ["mela","fragola","lamponi"]

if "mela" in favorite_fruit:
    print("mi piacciono davvero le mele")
    print("---")

if "pera" in favorite_fruit:
    print("buone le pere")
    print("---")

if "arance" in favorite_fruit:
    print("buone le arance")
    print("---")



if "fragola" in favorite_fruit:
    print("le fragole sono davvero ottime")
    print("---")
    
if "lamponi" in favorite_fruit:
    print("i lamponi sono davvero buoni")

print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")

#esercizio 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.


utenti : list = ["utente1","utente2","utente3","utente4","admin","utente5"]

for i in utenti:

    if i == "admin":

        print("CIAO AMMINISTRATORE,desideri visualizzare un rapposto sullo stato?\n")
        print("---")

    else:

        print(f"ciao {i} grazie per avere effetuato l'accesso oggi!\n")
        print("---")



print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")

#esercizio 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#• If the list is empty, print the message We need to find some users!
#• Remove all of the usernames from your list, and make sure the correct message is printed

utenti.clear()

if not utenti:
    print("dobbiamo trovare altri utenti")

print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")



#esercizio 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_user : list = ["marcolino98","giggi","Mario_77","AnDreaaa11","steFano88"]

new_users : list = ["deadly_combination","TRUCEBOIZ","GIggi","Concetta33","giovanni0139"]

#copia delle liste in minuscolo
copiaC : list = []
for i in current_user:

    copiaC.append(i.lower())

copiaN : list = []
for i in new_users:

    copiaN.append(i.lower())

#verifica disponibilità del nome
for i in range(len(new_users)):

    if copiaN[i] in copiaC:

        print(f"{new_users[i]} nome non disponibile,scegliere un altro nome \n")
        print("---")
    
    else:

        print(f"{new_users[i]} nome disponibile\n")
        print("---")
