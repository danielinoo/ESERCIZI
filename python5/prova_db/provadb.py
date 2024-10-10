import sys
import os
import os.path
import time

#pip3 install psycopg2-binary
import dbclient as db


#connesione al database
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()

sQuery = "select * from cittadini where codice_fiscale = '"+ sCodicefiscaleCittadino+ "';"

iNumRows = db.read_in_db(cur,sQuery)

if iNumRows == 0:
	print("\ncodice fiscale non presente nel database\n")
else:
	#invio query al database


for ii in range(0,iNumRows):
	myrow = db.read_next_row(cur)
	print(myrow)
	