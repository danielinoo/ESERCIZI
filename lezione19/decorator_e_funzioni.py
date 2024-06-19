# name = "marco"

# def ciao(name : str):

#     return f"ciao, {name}"
    
# def saluta_bob(func = ciao):

#     return func("bob")


# def salve(name : str):

#     return f"salve, {name}"
    
# print(saluta_bob(ciao))
# print(saluta_bob(salve))

# ##################################

# #funzioni dentro funzioni (per funzionare la funzione principale (parent)deve essere richiamata)

# def parent():

#     print("sono in funzione parent")

#     def firts_child():

#         print("sono dentro funzione 1")

#     def second_child():

#         print("sono in funzione 2")

#     firts_child()
#     second_child()

# parent() #richiamo la funzione parent



"""decorators"""

#decorator-> serve per modificare la funzione applicando un wrapper
def decorator(func):

    def wrapper():  #aggiunge due print alla funzione ciao
        print("prima di func")

        func()

        print("dopo func")

    return wrapper

def ciao():
    print("ciaooo")

#aggiorna la funzione ciao
ciao = decorator(ciao)

ciao()

print("\n ---------------------------------------\n")
################

"""esempio decorator:"""


def decorator(func):

    def wrapper():  #modifica la funzione ciao
       import time

       start = time.time()
 
       func()
       
       print(f"tempo: {time.time() - start}")
       
    return wrapper


ciao = decorator(ciao)

ciao()





    










