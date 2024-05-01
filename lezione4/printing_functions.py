#Daniele Pietropaolo
#1\05\2024

#esercizio 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

def make_shirt(taglia = "L", mes ="i love python") -> str:

    
    maglietta : str = f"la taglia della maglietta è {taglia} e il messaggio da stampare sopra è \"{mes}\""
    
    return maglietta