#Daniele Pietropaolo



def merge(a,i1,f1,f2):

    x = f2 - i1 +1

    i = 1
    i2 = f1 +1

    while (i1 <= f1 and i2 <= f2):

        if a[i1] <= a[i2]:
            x[i] = a[i1]

            i,i1 += 1

        else:
            x[i] = a[i2]

            i,i2 += 1

    if i1 < f1:

        a[i2] = f1 















def mergeSort(a : list[int],i : int,f : int):

    if i >= f:

        return i
    
    m = (i + f) / 2

    merge(a,i,m)
    merge(a, m + 1,f)
    merge(a,i,f,m)


print(mergeSort(a = [1,2,3,4,5,6],i = 1,f = 2))

