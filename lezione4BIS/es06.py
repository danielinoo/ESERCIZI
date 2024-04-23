#daniele pietropaolo
#22/04/2024

#esercizio 

def intersection(l1 : list, l2 : list):


    #r--> lista dei numeri in comune fra le due liste
    r : list = []
   

    for i in l1 and i in l2 :
    
        
       r.append(i)

    
    ri = set(r)
    return ri

print(intersection(l1 = [1,3,4,2,6],l2 = [3,2,1]))
        