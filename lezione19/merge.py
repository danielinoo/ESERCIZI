#Daniele Pietropaolo


def mergeSort(input_list : list[list]):



    #punto medio
    mid_point : int  = len(input_list) // 2


    mergeSort(input_list = input_list[0:mid_point]) #prende prima meta dellla lista
    mergeSort(input_list = input_list[mid_point :]) #prende seconda meta


if __name__ == "__main__":


    input_list : list[int] = [0,1,2,3,4,5,6,7]


    mergeSort( input_list = input_list)
