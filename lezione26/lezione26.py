#daniele pietropaolo


# Codificatori Messaggio
# Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

# Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

# Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
# Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà sostituita da 'f' e così via.

#      Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


# Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.

#     Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).


# Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

#     Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al metodo sposta_carattere().

#     Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al metodo combinazione().


# Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

# ### Test tramite codice driver:
# Test del Cifratore a Scorrimento:
# - Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
# - Lettura del testo: Il testo in chiaro viene letto da un file.
# - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
# - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
# - Stampa del testo codificato: Il testo codificato viene stampato.
# - Decodifica: Il testo codificato viene decodificato.
# - Stampa del testo decodificato: Il testo decodificato viene stampato.

# Test del Cifratore a Combinazione:
# - Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
# - Lettura del testo: Il testo in chiaro viene letto da un file.
# - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
# - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
# - Stampa del testo codificato: Il testo codificato viene stampato.
# - Decodifica: Il testo codificato viene decodificato.
# - Stampa del testo decodificato: Il testo decodificato viene stampa



from abc import ABC,abstractmethod



class CodificatoreMessaggio(ABC):

    def __init__(self) -> None:
        super().__init__()


    @abstractmethod
    def  codifica(testoInChiaro):
        pass


class  DecodificatoreMessaggio(ABC):
    
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def decodifica(testoCodificato):
        pass




class CifratoreAScorrimento(DecodificatoreMessaggio, CodificatoreMessaggio):

    def __init__(self,chiave : int) -> None:
        super().__init__()

        self.chiave  : int= chiave


    def sposta_carattere(self,c):
        import string
        alfabeto = list(string.ascii_lowercase)
        c = c.lower()
        if c in alfabeto:
            c = ord(c)
            c += self.chiave
            c = chr(c)
            return c

    def codifica(self,testoInChiaro):
        testoInChiaro = list(testoInChiaro)
        testoCodificato = []

        for i in range(len(testoInChiaro)):
            c = testoInChiaro[i]
            ci = self.sposta_carattere(c)
            testoCodificato.append(ci)

        testoCodificato = "".join(testoCodificato)

        print(testoCodificato)




    def decodifica_carattere(self,c : str):
        import string
        alfabeto = list(string.ascii_lowercase)
        c = c.lower()
        if c in alfabeto:
            c = ord(c)
            c -= self.chiave
            c = chr(c)
            return c


            
    def decodifica(self,testoCodificato):
        testoCodificato : list= list(testoCodificato)
        testoInChiaro : list = []

        for i in range(len(testoCodificato)):
            c = testoCodificato[i]
            ci = self.decodifica_carattere(c)
            testoInChiaro.append(ci)
        testoInChiaro = "".join(testoInChiaro)


        print(testoInChiaro)
    


class CodificaACombinazione(DecodificatoreMessaggio, CodificatoreMessaggio):

    def __init__(self,chiave : int) -> None:
        super().__init__()

        self.chiave = chiave

    def combinazione(self,testo):

        parte1 : list = []
        parte2 : list = []

        if len(testo) % 2 == 0:

            for i in range(len(testo) // 2):

                parte1.append(testo[i])


            for i in range(len(testo) // 2,len(testo)):

                parte2.append(testo[i])

        else:


            #se il testo è disparo 

            for i in range(len(testo) // 2 +1):
                parte1.append(testo[i])

        
            for i in range(len(testo) //2,len(testo)):

                    parte2.append(testo[i])

        return parte1,parte2



 

    def codifica(self,testoInChiaro):

        import copy

        for i in range(self.chiave):

            p1,p2 = self.combinazione(testoInChiaro)

            testoCodificato = []

            for j in range(len(p1)):

                
                    testoCodificato.append(p1[j])
                    testoCodificato.append(p2[j])

            
            testoInChiaro = copy.deepcopy(testoCodificato)

        testoCodificato = "".join(testoCodificato)

        print(testoCodificato)

            


    def decodifica_combinazione(self,testo):
        p2 : list = []
        p1 : list = []

        
        for i in range(len(testo)):
                
            if i % 2 == 0:
                p1.append(testo[i])
            
            else:
                p2.append(testo[i])

        return p1,p2


        
    def decodifica(self,testoCodificato):
        
        testoInChiaro : list = list(testoCodificato)

        for i in range(self.chiave):
            parte1,parte2 = self.decodifica_combinazione(testo = testoInChiaro)

            testoInChiaro = parte1 + parte2

        testoInChiaro = "".join(testoInChiaro)

        print(testoInChiaro)









            



        
    






    












