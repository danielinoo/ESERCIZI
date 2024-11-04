import dbclient as db 

cur = db.connect()
if cur is None:
    	print("Errore connessione al DB")

print("\n---------------------------------\n")
a = int(input("\n premere:\n1) per fare una query di lettura\n2) per fare una query di scrittura\n"))
print("\n---------------------------------\n")

if a == 1:
    query= input("\ninserire la query di lettura:\n")
    Numrows = db.read_in_db(cur,query)#esegue la query
    if Numrows > 0:
        print("\nquery risuscita correttamente:\n")
        #ciclo per stampare tutte le righe del risultato
        for i in range(0,Numrows):  
            risultato = db.read_next_row(cur)
            print(f"{risultato}")
    else:
        print("\nATTENZIONE PROBLEMI, RIPROVARE\n")

    print("\n---------------------------------\n")
             
if a ==2:
    query= input("\ninserire la query di scrittura:\n")
    Numrows = db.write_in_db(cur,query)
    if Numrows >=0:
            print("\nquery eseguita correttamente")
        
              