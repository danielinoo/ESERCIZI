# Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.
# Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() per impostare il testo. Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.

# Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.
# Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
# Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
# Da: alice@example.com, A: bob@example.com
# Titolo: Incontro
# Messaggio: Ciao Bob, possiamo incontrarci domani?
 
# Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
 
# Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
# Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
# I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
# Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
# Percorso: nomePercorso/document.txt
# Contenuto: Questo e' il contenuto del file.


class Documento:

    def __init__(self) -> None:
        
        self.testo  : str = ""


    def getText(self):

        return self.testo
    
    def setText(self,testo):

        self.testo = testo


    def  isInText(self,parola):

        if parola in self.testo:

            return True
        
        else:

            return False
        


class Email(Documento):

    def __init__(self,mittente : str,destinatario : str) -> None:
        super().__init__()

        self.mittente = mittente
        self.destinatario = destinatario
        self.messaggio = self.testo


    def getMittente(self):

        return self.mittente
    
    def setMittente(self,mittente):

        self.mittente = mittente

    

    def getDestinatario(self):

        return self.destinatario
    
    def setDestinatario(self,destinatario):

        self.destinatario = destinatario


    def getTitolo(self):

        return self.titolo
    
    def setTitolo(self,titolo):

        self.titolo = titolo


    def getMessaggio(self):

        return self.messaggio
    
    def setMessaggio(self,messaggio):

        self.messaggio = messaggio

    
    def getText(self):

        return f"\nDa: {self.mittente}, A: {self.destinatario}\n \
                Titolo: {self.titolo}\n \
                Messaggio: {self.messaggio}\n"
    

    def  writeToFile(self, path):

        with open(path,"w") as f:

            f.write(self.getText())



class File(Documento):

    def __init__(self) -> None:

        self.nomePercorso  : str = "/project/ESERCIZI/lezione24/directory/document.txt"
        super().__init__()



    def decorator(self):

        def wrapped():

            print(f"Percorso:{self.nomePercorso}\nContenuto:")
            self.getText()

        return wrapped
    
    @decorator
    def leggiTestoDaFile():
        pass
    
    









