#Daniele Pietropaolo
#29/04/24

#5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
#ate to 10. If you want to try more comparisons, write more tests and add them
#to conditional_tests.py. Have at least one True and one False result for each of
#the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list


#test uguaglianza e disuguaglianza fra stringhe
stringa1 : str = "Ciao, sono Marco e vengo da roma"
stringa2 : str = "ciao sono mario e vengo da milano"

if stringa1 == stringa2:

    print(True)

else:

    print(False)


print("\n|||||||||\n")


if stringa1 != stringa2:

    print(True)

else:

    print(False)


print("\n|-----------|\n")

#test che utilizzano il metodo lower()
stringa1 : str = "CIAO"
stringa2 : str = "ciao"

if stringa1 == stringa2.lower():

    print(True)

else:

    print(False)


print("\n|||||||||\n")

if stringa2 == stringa1.lower():

    print(True)

else:

    print(False)

print("\n|-----------|\n")

#test numerici

n1 : int = 20
n2 : int = 15

if n1 < n2:

    print(True)

else:

    print(False)


print("\n|||||||||\n")

if n1 > n2:

    print(True)

else:

    print(False)


print("\n|||||||||\n")

if n1 <= n2:

    print(True)

else:

    print(False)


print("\n|||||||||\n")

if n1 >= n2:

    print(True)

else:

    print(False)


print("\n|||||||||\n")

if n1 != n2:

    print(True)

else:

    print(False)


print("\n|||||||||\n")

if n1 == n2:

    print(True)

else:

    print(False)


print("\n|-----------|\n")


#verifica utilizzando la parola chiave

if n1< 35 and n1 > 10:

    print(True)

else:
    print(False)

print("\n|||||||||\n")

if n2 <= 5 and n2 > 30:
    print(True)
else:
    print(False)
print("\n|-----------|\n")
#verifica se un elemento è o non è in un elenco

macchina : list = ["mercedes","maserati","fiat"]


if "bmw" in macchina:
    print(True)

else:

    print(False)


print("\n|||||||||\n")

if "fiat" in macchina:   
    print(True)

else:

    print(False)

print("\n|-----------|\n") 