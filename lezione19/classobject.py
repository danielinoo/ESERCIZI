def ciao(name : str):

    return f"ciao, {name}"
    
def saluta_bob(func : function):

    return func("bob")


def salve(name : str):

    return f"salve, {name}"
    
print(saluta_bob(ciao))
print(saluta_bob(salve))