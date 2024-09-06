



#se è simmetrico interno              1                   
#                                   /   \
#                                  2     2
#                                   \   /
#                                    3 3




#se è simmetrico esterno              1
#                                   /   \
#                                  1      2
#                                   \    /
#                                    3  3




def is_simmetric(tree : list[int]) -> bool:

    return are_mirrored(tree, 1,2)





def are_mirrored(tree, left_index,right_index):
    
    if left_index >= len(tree) and right_index >= len(tree):
        return True
    
    elif ( left_index >= len(tree) and right_index < len(tree))\
            or (left_index < len(tree) and right_index >= len(tree)):
        return False


    if tree[left_index] != tree[right_index]:
        return False


    left_of_left = 2 * left_index +1 #sinistro del sinistro
    right_of_left = 2 * left_index +2 #destro del sinistro

    left_of_right = 2 * right_index +1 #sinistro del destro
    right_of_right = 2 * right_index+2 #destro del destro



    is_simmetric_external : bool = are_mirrored(tree, left_of_left,right_of_right)          
    is_simmetric_internal : bool = are_mirrored(tree,right_of_left,left_of_right)          

    return is_simmetric_internal and is_simmetric_external
