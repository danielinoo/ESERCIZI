# Scrivi una funzione che accetti tre parametri: user, passw e stato dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "manager", la password corrisponde a "67890" e l'account è attivo (True). La funzione ritorna "Ingresso consentito" oppure "Ingresso negato".
# For example:

# Test	Result
# print(verifica_accesso("manager", "67890", True))
# Ingresso consentito
# print(verifica_accesso("manager", "wrongpassword", True))
# Ingresso negato

# #######################################################

# Scrivi una funzione che, data una lista di parole, ritorni un dizionario che mappa ogni parola alla sua lunghezza.
# For example:

# Test	Result
# print(mappa_parole_a_lunghezza(["apple", "banana", "cherry"]))
# {'apple': 5, 'banana': 6, 'cherry': 6}
# print(mappa_parole_a_lunghezza(["elephant"]))
# {'elephant': 8}

# ###################################

# Scrivi una funzione che prenda un dizionario e un valore, e ritorni una lista con tutte le chiavi che corrispondono a quel valore, o una lista vuota se il valore non è presente.
# For example:

# Test	Result
# print(trova_tutte_chiavi({'a': 1, 'b': 2, 'c': 1}, 1))
# ['a', 'c']
# print(trova_tutte_chiavi({}, 1))
# []

# ##########################################àà

# Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa" oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.
# For example:

# Test	Result
# print(verifica_condizioni(True, False, True))
# Azione permessa
# print(verifica_condizioni(True, False, False))
# Azione negata


# ###################################################################

# Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

# Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

# Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

# Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
# For example:

# Test	Result
# print(time_difference(1, 0, 0, 3, 15, 30))
# 8130
# print(time_difference(0, 0, 0, 12, 0, 0))
# 43200


# ############################################################################

# Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che classifichi i numeri in liste separate per numeri positivi e negativi.

# For example:

# Test	Result
# print(classifica_numeri([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
# {'positivi': [1, 3, 5, 7, 9], 'negativi': [-2, -4, -6, -8, -10]}
# print(classifica_numeri([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
# {'positivi': [], 'negativi': [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]}

# #################################################################################


# Question text
# Progettare un semplice sistema di gestione di studenti e corsi con i seguenti requisiti:
 
# 1. Classe Student:
# Attributi:
# student_id: str - identificatore univoco per lo studente.
# courses: list[str] - la lista dei corsi ai quali lo studente è iscritto.
# Metodi:
# enroll(course: str) - aggiunge il corso specificato alla lista dei corsi dello studente oppure stampa il messaggio "Lo studente è già iscritto al corso {course}."
# get_courses(): restituisce la lista dei corsi ai quali lo studente è iscritto.
# Classe School:
# Attributi:
# students: dict[str, Student] - un dizionario per memorizzare gli studenti, in cui la chiave è una stringa ID mentre il valore è un oggetto di tipo Studente.
# Metodi:
# create_student(student_id: str): crea un nuovo studente con l'ID specificato e una lista di corsi vuota oppure stampa il messaggio "Lo studente con ID {student_id} esiste già."
# enroll_student(student_id: str, course: str): se lo studente esiste viene iscritto al corso specificato, altrimenti  stampa il messaggio "Studente non trovato."
# get_student_courses(student_id: str): se lo studente esiste restituisce la lista dei corsi dello studente con l'ID specificato, altrimenti ritorna il messaggio "Studente non trovato."
# get_stundent_list(): Ritorna una lista di tutte le chiavi all'interno del dizionario students.
# search_by_course(self, course: str): Trova e restituisce tutti gli ID degli studenti iscritti ad un determinato corso. Restituisce una lista di tutte le chiavi all'interno del dizionario students che hanno il corso specificato tra i valori oppure il messaggio di errore "Nessuno studente è iscritto al corso {course}." se non ci sono studenti che frequentano il corso specificato.
# For example:

# Test	Result
# # Creazione di una nuova scuola
# scuola = School()

# # Creazione di nuovi studenti
# scuola.create_student("1001")
# scuola.create_student("1002")
# scuola.create_student("1003")

# # Iscrizione degli studenti ai corsi
# scuola.enroll_student("1001", "Matematica")
# scuola.enroll_student("1002", "Fisica")
# scuola.enroll_student("1003", "Chimica")

# # Verifica dei corsi degli studenti
# print(scuola.get_student_courses("1001"))  # Output atteso: ['Matematica']
# print(scuola.get_student_courses("1002"))  # Output atteso: ['Fisica']
# print(scuola.get_student_courses("1003"))  # Output atteso: ['Chimica']
# ['Matematica']
# ['Fisica']
# ['Chimica']
# # Creazione di una nuova scuola
# scuola = School()

# # Creazione di nuovi studenti
# scuola.create_student("1001")

# # Iscrizione degli studenti ai corsi
# scuola.enroll_student("1001", "Matematica")
# scuola.enroll_student("1001", "Matematica")

# # Tentativo di iscrizione di un corso per uno studente non esistente
# scuola.enroll_student("1004", "Fisica")

# # Verifica dei corsi degli studenti
# print(scuola.get_student_courses("1001"))
# print(scuola.get_student_courses("1004"))

# #############################################


# Question text
# Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
# Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
# La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.
# For example:

# Test	Result
# print(calcola_stipendio(40))
# 400.0
# print(calcola_stipendio(0))
# 0.0

# ###########################