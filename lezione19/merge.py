#Daniele Pietropaolo


def mergeSort(input_list : list[list]):



    #punto medio
    if len(input_list) == 1:

        return input_list

    
    mid_point : int  = len(input_list) // 2


    list_1 = mergeSort(input_list = input_list[0:mid_point]) #prende prima meta dellla lista
    list_2 = mergeSort(input_list = input_list[mid_point :]) #prende seconda meta

    return merge(list_1,list_2)




#due liste ordinate(il primo indice è il più piccolo)
def merge(list_1 : list[int], list_2 : list[int]):

    i,j = 0,0

    result : list[int] = [None for _ in range(len(list_1 + list_2))]

    for k in range(len(result)): #K indice che tiene traccia nella lista che è la somma delle due liste

        
        if list_1[i] > list_2[j]: #l elemento della lista 1 è più grande delle elemento della lista 2

            result[k] = list_2[j] #assegno all' indice di k J e incremento di 1 j

            if j == len(list_2):

                break
            """aggiungere i controlli pe i e j vanno fuori dalla lunghezza della lista"""

        else:
            j += 1

        

        if list_1[i] < list_2[j]:


            result[k] = list_1[i]

            if i == len(list_1):

                break


        else:

            i += 1

    return result






if __name__ == "__main__":


    input_list : list[int] = [0,1,2,3,4,5,6,7]


    print(mergeSort( input_list = input_list))
