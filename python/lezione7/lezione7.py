#Daniele Pietropaolo
#10/05/24



def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:

    d : dict = {}

    for k,v in dizionario.items():

        if k and v not in d:


            d[v] = k

    dizionario = d

    return dizionario

########################################################

def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:

    l1 : list = []

    for i in range(len(lista_numeri)):

        if lista_numeri[i] % 2 == 0:

            lista_numeri[i * fattore]
            l1.append(lista_numeri[i])

    return l1







########################################################################

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    

    for k,v in da_rimuovere.items():

        if k in lista:

            for j in range(v):

                lista.remove(k)

    return lista



################################################################################


def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    
    d : dict = {}
    l : list = []


    for i in voti:
        
        k = i["nome"]
        v = i["voto"]


        if k  not in d:

            

            d[k] = [v]

        else: 
            d[k] = d[k].append(v)




    return d


print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))



#######################################################4


def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:


    ps : dict =  {}
    for k,v in prodotti.items():


        key = k
        if v > 20:

           s = v * 0.9
           ps[key] = s



    return ps


##################################################à


def create_contact(name: str, email: str=None, telefono: int=None) -> dict:

    dictionary : dict = {"nome" : name,"email": email}

    

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    
    pass



##########################################################



    




















