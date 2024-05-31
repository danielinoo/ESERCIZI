#daniele pietropaolo

"""Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""





class Film:

    def __init__(self,titolo : str,durata : int) -> None:

        self.titolo = titolo
        self.durata = durata


class Sala:

    def __init__(self,id : int,film : Film,posti_tot : int) -> None:
        self.id = id
        self.film = film
        self.posti_tot = posti_tot
        self.posti_prenotati = 0


    def prenota_posti(self,num_posti : int):

        if self.posti_tot - num_posti > 0:

            self.posti_prenotati = self.posti_prenotati + num_posti

        else:
            return 0


        return self.posti_prenotati
    

    def posti_disponibili(self):

        posti_disp : int = self.posti_tot - self.posti_prenotati

        return posti_disp





class Cinema:

    def __init__(self) -> None:

        self.sala : list[Sala] = []

    
    
    def aggiungi_sala(self,sala : Sala):

        self.sala.append(sala)

        


    
    def prenota_film(self,titolo_film, num_posti):

        a = 0
        for i in self.sala:

            if i.film.titolo == titolo_film:

                a = i.prenota_posti(num_posti)

                if a  > 0:

                    return"\nposti prenotati\n"

                else:
                     
                    return "\nposti non disponibili\n"


        




                


        



film_1 = Film("avuengers",120)
film_2  = Film("adagio",157)
film_3 = Film("frozen",104)

sala_1 = Sala(1,film_1,30)
sala_2 = Sala(2,film_2,50)
sala_3 = Sala(3,film_3,60)

cinema = Cinema()


cinema.aggiungi_sala(sala_1)
cinema.aggiungi_sala(sala_2)
cinema.aggiungi_sala(sala_3)

print(cinema.prenota_film("adagio",10))
print(cinema.prenota_film("frozen",100))

print(sala_3.posti_disponibili())
















 