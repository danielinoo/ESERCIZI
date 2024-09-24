mylist1 = "['mario','gino',     'lucrezia']"
mylist2 = ['mario','gino','lucrezia']

def serializza(lvar : list) -> str:
        return str(lvar)

def deserializza(svar : str) -> list:

    l_str = svar.replace("[", "").replace("]", "").replace("'", "")   
    l = l_str.split(",")
    l = [i.strip() for i in l]
          
    return l

# sprova = deserializza(mylist1)
# print("deserializzazione",sprova, type(sprova))

# mylist2 = serializza(mylist2)
# print("serializzazione",mylist2,type(mylist2))



###########################################
import json


mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"

def serializza_json(file_path)-> bool:
    try: 
            # primo modo
        with open(file_path, "w")as fp:
            json.dump(mydict_1,fp)
        return True
    
    except:
        return False

def deserializza_json(file_path)-> dict:
    with open(file_path, "r")as fp:
        return json.load(fp)
    

file_path = "./json/mydict.json"

md1 = serializza_json(file_path)
print(md1)

md2 = deserializza_json(file_path)
print(md2)
    
         

