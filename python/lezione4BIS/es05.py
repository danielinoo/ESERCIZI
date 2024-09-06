#Daniele Pietropaolo
#20/04/2024

#esercizio data una lista di nums interi, spostare gli zeri alla fine di questa lista mantenendo l' ordine originale dei numeri che non sono zeri

def move_zeroes(nums : list[int]):

    for i in range (len(nums)):

        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums

print(move_zeroes(nums = [0,1,2,3,0,9,0,9,6]))