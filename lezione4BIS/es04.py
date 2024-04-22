#Daniele Pietropaolo
#22/04/2024

#esercizio data una lista NUMS di N elementi, restituire l' elemento che compare più di n/2 volte


def majority_element(nums : list) -> int:

    d : dict[int,int] = {}

    for i in nums:

        d[i] = nums.count(i)
    l = len(nums)

    for key in d:
        d[key] /= l

        if d[key] > 0.5:
            return key
        
    return None
    
print(majority_element(nums = [2,2,2,2,4,1]))
        
        
        

