
# def ciao():

#     print("bello gigi")


# def decorator(func):

#     def wrapped(*args):
#         func(*args)
#         print("ciaooooo come stai?")

        

#     return wrapped


# ciao = decorator(ciao)


# ciao()


# def generatore():
#     yield "A"
#     yield "B"
#     yield "C"

# prova_generatore = generatore()

# print(next(prova_generatore))
# print(next(prova_generatore))
# print(next(prova_generatore))
# print(next(prova_generator


from contextlib import contextmanager

@contextmanager
def conterxt_manager_decorator():
    import time

    start_time : float = time.time()

    yield

    end_time : float = time.time()

    elapsed_time = end_time - start_time

    print(f"{elapsed_time=}")


@conterxt_manager_decorator
def area_cerchio(raggio : float):

    return raggio * raggio *3.14

area_cerchio(1)


################################

import sys

a = []
b = a
print(sys.getrefcount(a))

def thread_funcion(name):

    print(f"{}")


