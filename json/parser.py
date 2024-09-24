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

def serializza_json(dData,file_path)-> bool:
    try: 
        with open(file_path, "w")as fp:
            json.dump(dData,fp)
        return True
    
    except:
        return False
    


def deserializza_json(file_path)-> dict:
    with open(file_path, "r")as fp:
        return json.load(fp)

def deserializza2_json(file_path)-> dict:
    sData = ""
    sAppo =  ""
    dData = {}
    try:
        
        with open(file_path, "r")as fp:
            sAppo = fp.read(500)
            while len(sAppo) == 500:
                sData += sAppo
                sAppo = fp.read(500)
            if len(sAppo) > 0:
                sData += sAppo
        if len(sData)>0:
            dData = json.loads(sData)
            return dData
    
        else:
            return None
    except:
        return None


       
def serializza2_json(dData,file_path)-> bool:
    try:             
        sData = json.dumps(dData)
        with open(file_path, "w")as fp:
            fp.write(sData)

        return True
    
    except:
        return False    

file_path = "./json/mydict.json"

md1 = serializza_json(mydict_1,file_path)
print(md1)

md2 = deserializza_json(file_path)
print(md2)
    
         

