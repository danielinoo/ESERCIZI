



from multiprocessing import Process

import time


def bubble_sort():
    from random import randint

    x = [randint (0,5000000) for _ in range(100000)]

    ho_fatto_swap : bool = True

    for i in range(len(x)):

        for j in range(len(x) -i -1):

            if x[j] > x[j+1]:

                ho_fatto_swap = False

                temp : int = x[j]

                x[j] = x[j+1]

                x[j+1] = temp

        if ho_fatto_swap:
            break

def sleep():

    print(f"sono nella funzione")

    time.sleep(60)

    print(f"sto uscendo")



if __name__ == "__main__": #tutta la roba sotto if __name ecc.   quando viene importato il file non viene eseguito

    tic : float = time.time()

    t1 = Process(target = bubble_sort)
    t2 = Process(target = bubble_sort)
    t3 = Process(target = bubble_sort)
    t4 = Process(target = bubble_sort)
    t5 = Process(target = bubble_sort)
    

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    toc : float = time.time()

    time_elapsed: float = toc - tic

    print(f"{time_elapsed =}")



##############################




