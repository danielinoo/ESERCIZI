#Daniele Pietropaolo


# Completion requirements
# Esercizio 1

# Crea un context manager usando una classe

# Definisci una classe FileManage che implementa un context manager che gestisce le risorse dei file.

# Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

# Esempio di funzionamento:

# Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

# with FileManager('example.txt', 'w') as f:

#     f.write('Hello, world!')



class FileManager:

    def __init__(self,file_name,mode) -> None:
    
        self.file = None
        self.file_name = file_name
        self.mode : str = mode #modalita apetrura



    def __enter__(self):


        self.file = open(self.file_name,self.mode)
        print("file aperto")

        return self.file
    

    def __exit__(self,exc_type,exc_value,traceback):

    
        if self.file:
            self.file.close()

        print("file chiuso")

        if exc_type is not None:

            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback:{traceback}")
            return False
        

# with FileManager(file_name ='example.txt', mode ='w') as f:

#     f.write('Hello, world!')


# with open('example.txt','w') as f:

#     f.write("ciaoo")



class Timer:

    def __enter__(self):

        import time

        self.time = time.time()

    

    def __exit__(self,exc_type,exc_value,traceback):

    
        import time
        print(f"Time Elapsed : {time.time() - self.time} ")

        if exc_type is not None:

            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback:{traceback}")
            return False
        


with Timer():

    """tutto quello dentro with Timer() viene eseguito"""





    
