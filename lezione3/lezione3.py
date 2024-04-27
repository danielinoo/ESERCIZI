#Daniele Pietropaolo
#27/04/24

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


num : list = []
for i in range(1,10000001):
    num.append(i)

print(min(num))
print(max(num))

print("\n---\n")

a : int = 1000000 #a --> variabile di supporto
num = sum(a)
print(num)

print("\n")
print("|-----------------------------------------------------------------------------|")
"""-----------------------------------------------------------------------------------------------------------------------------------"""
print("\n")   




