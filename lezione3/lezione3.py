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

#esercizio 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.









print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")  


#esercizio 4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.



