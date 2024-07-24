def frequency_dict(elements: list) -> dict:
    
    d : dict[str,int] = {}
   
    for i in elements:
       
        if i not in d:
       
            d[i] = elements.count(i)
            
    return d


###########################################à
def check_access(username: str, password: "12345", is_active: bool) -> str:
    
    if username == "admin" and password ==  "12345" and is_active == True:
        return  "Accesso consentito"
        
    else:
        return "Accesso negato"
 	


##############################################


def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    d : dict[str,list[int]] = {}


    for i in tuples:

        if i[0] not in d:

            l : list = []
            l = [i[1]]

            d[i[0]] = l

        else:
            l.append(i[1])
            d[i[0]] = l


    return d






##################################################

def sum_above_threshold(numbers: list[int],threshold : int) -> int:
    s = 0
   
    for i in numbers:
       
       if i > threshold:
           
           s += i
           
           
           
    return s

a : int = 0
input(a )
