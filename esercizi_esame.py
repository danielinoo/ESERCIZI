
# Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.

# For example:

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    
    for k,v in dizionario.items():
        
        if valore == v:
            return k
            
    return None


"""----------------------------------------------------------------"""




# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.



def frequency_dict(elements: list) -> dict:
    
    d : dict [str: int] = {}
    
    for i in elements:
        
        d[i] = elements.count(i)
        
        
    return d

"""-------------------------------"""


# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.



def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    d : dict[str:float] = {}
    for k,v in prodotti.items():
        if v > 20:
            sconto = v *0.1
            d[k] = v - sconto
            
            
    return d




"""----------------------------------"""



def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    d : dict[str : list[int]] = {}
    
    for i in tuples:
        
            if i[0] not in d :
                d[i[0]] = []

                d[i[0]].append(i[1])  
                
            else:
                d[i[0]].append(i[1])  
            
                
                
    return d

"""-----------------------------------------------------"""

# Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".

def check_access(username: str, password: str, is_active: bool) -> str:
    
    
    if username == "admin" \
    and password == "12345"\
    and is_active == True:
        return "Accesso consentito"
        
    else:
        
        return "Accesso negato"
    


# Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.


