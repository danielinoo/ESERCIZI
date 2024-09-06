
##############################
print("----------------------------------")

def longest_palindrome(s: str) -> int:
    p = 0
    pp = 0



    for i in set(s):

        p = s.count()

        pp += p // 2 * 2
    

    

    return pp




#############################à



def merge(nums1, m, nums2, n):
    

    nums1 += nums2

    for i in nums1:

        if i == 0:

            nums1.pop(i)


    nums1.sort()

    return nums1

    
#######################

class Queue:
    def __init__(self) -> None:
        self.m = MyStack








class  MyStack:
    def __init__(self) -> None:
        self.l : list = []
    

    def push(self,x : int):

        self.l.append(x)
        
    
    def top(self):
        
        self.l = self.l[::-1]

        return self.l[0]

    def pop(self):

        return self.l.pop(0)
    
    def empty(self):
        a = None

        if len(self.l) <= 0:
            a = True

        else: a = False

        return a
    



#######################################