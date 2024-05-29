#Daniele Pietropaolo

"""In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

 Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
 
SFIDE AGGIUNTIVE:
1. Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
Modificatori mossa:
- La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
- La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
 
2. Energia o Stamina:
Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. L'energia inziale per entrambi gli animali è 100.

Nuove regole di movimento:
- Tartaruga:
    - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia. Non può superare l'energia iniziale.
    - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
    - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

- Lepre:
    - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
    - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
 
3. Ostacoli e Bonus
Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, che influenzano direttamente il movimento degli animali quando vengono calpestati. Gli ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.

Dettagli Implementativi:
- Ostacoli:
Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7). Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso (chiave) ed i relativi effetti (valore). Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.

- Bonus:
Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione dell'animale di un numero determinato di quadrati (es: 5, 3, 10). I bonus sono rappresentati da un dizionario che mappa le posizioni dei bonus sul percorso (chiave) ed i relativi effetti (valore). Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo."""

import random


#posizioni
post = 1
posl = 1

#stamina
stamina_tartaruga :  int = 100
stamina_lepre : int = 100



def posizione(post, posl,stamina_tartaruga,stamina_lepre):

   percorso : list = ["_"] * 70

   ostacoli : dict = {15 : -3,
                     30 : -5,
                     45 :-7}
   
   bonus : dict = {10 : 5,
                     25 : 3,
                     50 : 10}
   

   #mosse
   mt, energia_tartaruga = mossa_tartaruga()
   ml, energia_lepre = mossa_lepre()


   #variazione ambientale
   v : int = None
   if tick == 10:   
      v  : int = random.randrange(1,3)

      if v == 1:
      
         mt = mt -1
         ml = ml - 2

    
   #tartaruga:

   if mt != 0 and stamina_tartaruga  - energia_tartaruga >= 0:

      stamina_tartaruga -= energia_tartaruga


      if stamina_tartaruga > 100:
         
         stamina_tartaruga = 100

      if stamina_tartaruga < 0:

         stamina_tartaruga = 0

      
      post = post + mt


      if post <= 0:
           
         post = 1

      if post >= len(percorso):
       
         post = len(percorso)
   else:
       
      stamina_tartaruga += 10


   #lepre:

   if ml != 0 and stamina_lepre  - energia_lepre != 0:


      stamina_lepre -= energia_lepre

      if stamina_lepre > 100:
         stamina_lepre = 100

      if stamina_lepre < 0:
         stamina_lepre = 0     


      posl = posl + ml
           

      if posl <= 0:
           
         posl = 1

      if posl >= len(percorso):
           
         posl = len(percorso)


   #ASSEGNAZIONE POSIZIONI:
   if post == posl:
       
      percorso[post-1] = "AUCH"

   else:
       
      percorso[post-1] = "T"
      percorso[posl-1] =  "L"


      #OSTACOLI e BONUS:
      if post in ostacoli:

         post += ostacoli[post]
         percorso[post-1] = "T"
         if post <= 0:
            post = 1
         
      elif post in bonus:
         post += bonus[post]
         percorso[post-1] = "T"
         
         if post > len(percorso):
            post = len(percorso)
         


      
      if posl in ostacoli:
        posl += ostacoli[posl]
        if posl <= 0:
            posl = 1
        percorso[posl-1] = "L"

      elif posl in bonus:
         posl += bonus[posl]
         percorso[posl-1] =  "L"

         if posl >= len(percorso):
            posl = len(percorso)


   return percorso,post,posl,stamina_tartaruga,stamina_lepre         
                      

##########################################

def mossa_tartaruga():

    t = random.randrange(1,11)
    mossa : int = 0

    if t <= 5:
      
      mossa = 3
      return mossa,5
    
    elif t == 6 or t == 7:
      
      mossa = -6
      return mossa,10

    else:
      
      mossa = 1
      return mossa,3
      
#####################################################     
    

def mossa_lepre():

    t = random.randrange(1,11)
    mossa : int = 0

    if t <= 2:
       
       mossa = 9

       return mossa,15

    elif t == 3:
       
       mossa = -12
       return mossa,20

    elif t > 3  and t <= 6:
       
       mossa = 1
       return mossa,5

    elif t > 6 and t <= 8:
       
       mossa = -2
       return mossa,8
    
    else:
       
       mossa = 0
       return mossa,-10

####################################################



tick : int = 0

print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

while post <= 69 and posl <= 69:
    

      tick += 1
      percorso, post, posl,stamina_tartaruga,stamina_lepre = posizione(post,posl,stamina_tartaruga,stamina_lepre)
      print("".join(percorso))


      if tick == 10:
       
         tick = 0

       


if post >= 69:
       
       print("TORTOISE WINS! || VAY!!!")
       
if posl >= 69:
    print("HARE WINS || YUCH!!!")
           


if post == 69 and posl == 69:
   
    print( "IT'S A TIE.")