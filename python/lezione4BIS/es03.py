#Daniele Pietrpaolo
#22/04/2024

#ESERCIZIO dato un intero col_number, restituisce il suo corrispondente titolo di colonna come ad esempio compare su un folgio excel

def convert_to_title(col_number : int) -> str:

    r : str = ""

    while col_number > 0:
        resto : int = (col_number -1) % 26 #resto
        r =chr(resto + ord("A")) + r
        col_number = (col_number -1) // 26
    return r
    
print(convert_to_title(5))

    
    
    
