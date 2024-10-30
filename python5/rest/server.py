from flask import Flask, jsonify, request
import sys
import dbclient as db #import connessione database
api = Flask(__name__)

#connessione database
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()



@api.route('/login_cittadino', methods=['POST'])
def GestisciAccesso():
    global cur #prendo cur globale
    #prendo i dati dal client
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        jEmail= jsonReq.get('email')
        jPassword = jsonReq.get('password')
        
        #creo query
        squery = f"select privilegi \
                from utenti \
                where username = '{jEmail}' and password = '{jPassword}';"
        
        iNumrows = db.read_in_db(cur,squery)#esegue la query

        #controllo risultato della query
        if iNumrows ==1:
            lrow = db.read_next_row(cur) #risultato query
            sPriv = lrow[1][0]#prende il primo dato (privilegi)
            return jsonify({"Esito": "000", "Msg": "login effettuato","Privilegi" : sPriv}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "utente non esiste"}), 404
    else:
        return jsonify({"Esito": "002", "Msg": "content-type non supportato"}), 200



@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    global cur
    #prendo dati della richiesta
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        #controllo privilegi
        jEmail= jsonReq.get('username')
        jPassword = jsonReq.get('password')
        squery = f"select *\
                from utenti \
                where username = '{jEmail}' and password = '{jPassword}' \
                    and privilegi = 'w';"
        
        iNumrows = db.read_in_db(cur,squery)#esegue la query
        if iNumrows ==1:
                jsonReq = jsonReq.get('datiCittadino')
                nome = jsonReq.get('nome')
                cognome = jsonReq.get('cognome')
                codice_fiscale= jsonReq.get('codFiscale')
                dataNascita = jsonReq.get('dataNascita')

                squery = f"insert into cittadini(codice_fiscale,nome,cognome,data_nascita)\
                        values ('{codice_fiscale}','{nome}','{cognome}','{dataNascita}')"

                #controllo dati
                iRet = db.write_in_db(cur,squery)
                if iRet == -2:
                        return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
                elif iRet == -1:
                    return jsonify({"Esito": "003", "Msg": "permesso non accettato"}), 200
                else:
                    return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
       return jsonify({"Esito": "002", "Msg": "content-tyoe non supportato"}), 200



#la url che sta dopo read_cittadino diventa na stringa e flask la usa
@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    global cur
    squery = f"select *\
                from cittadini \
                where codice_fiscale = '{codice_fiscale}';"
        
    iNumrows = db.read_in_db(cur,squery)#esegue la query

    if iNumrows ==1:
        lrow = db.read_next_row(cur)
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": lrow}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 404



#put -> serve per modificare
@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():

    # update cittadini
    # set nome = 'giuseppe'
    # where codice_fiscale = 'ahdo45swo16h501s'

    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        #controllo privilegi
        jEmail= jsonReq.get('username')
        jPassword = jsonReq.get('password')
        squery = f"select *\
                from utenti \
                where username = '{jEmail}' and password = '{jPassword}' \
                    and privilegi = 'w';"
        iNumrows = db.read_in_db(cur,squery)#esegue la query
        if iNumrows ==1:
            daticit = jsonReq.get('datiCittadino') #entro in datiCittadino
            nome = daticit.get('nome')
            cognome = daticit.get('cognome')
            codice_fiscale= daticit.get('codFiscale')
            dataNascita = daticit.get('dataNascita')

            #modifica cittadino
            squery= f"UPDATE cittadini \
                    SET nome = '{nome}', \
                        cognome = '{cognome}', \
                        data_nascita = '{dataNascita}' \
                    WHERE codice_fiscale = '{codice_fiscale}';"
            
            iRet = db.write_in_db(cur,squery)
            
            if iRet != -1 or iRet != -2:
                return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
            else:
                return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 404
                
        else:
            return jsonify({"Esito": "003", "Msg": "permesso non accettato"}), 200
        
    else:
        return jsonify({"Esito": "002", "Msg": "content-tyoe non supportato"}), 200


@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        #controllo privilegi
        jEmail= jsonReq.get('username')
        jPassword = jsonReq.get('password')
        squery = f"select *\
                from utenti \
                where username = '{jEmail}' and password = '{jPassword}' \
                    and privilegi = 'w';"
        iNumrows = db.read_in_db(cur,squery)#esegue la query
        if iNumrows ==1:

            codice_fiscale = jsonReq.get('codice_fiscale')
            codice_fiscale = codice_fiscale['codFiscale']
            squery= f"DELETE FROM cittadini \
                    WHERE codice_fiscale = '{codice_fiscale}';"

            iRet = db.write_in_db(cur,squery)
            if iRet != -1 or iRet != -2:
                return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
            else:
                return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 404
        else:
            return jsonify({"Esito": "003", "Msg": "permesso non accettato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "content-tyoe non supportato"}), 200


    
api.run(host="127.0.0.1", port=8080,ssl_context = "adhoc")

#crittografia messaggio -> ssl_contexT = "adhoc"

