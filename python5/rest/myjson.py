import json



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
