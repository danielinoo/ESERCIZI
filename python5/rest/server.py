from flask import Flask, jsonify, request
from myjson import deserializza_json, serializza_json

api = Flask(__name__)


file_path = "anagrafe.json"
cittadini = deserializza_json(file_path)


@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    #prendo dati della richiuesta
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        #controllo se il codice fiscale è presente nell' anagrafe
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            serializza_json(cittadini, file_path) 
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
       return jsonify({"Esito": "002", "Msg": "content-tyoe non supportato"}), 200



#la url che sta dopo read_cittadino diventa na stringa e flask la usa
@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    cittadino = cittadini.get(codice_fiscale)
    #eseguo la richiesta
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 404


#put -> serve per modificare
@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            serializza_json(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 404
    else:
        return jsonify({"Esito": "002", "Msg": "content-tyoe non supportato"}), 200


@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            serializza_json(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 404
    else:
        return jsonify({"Esito": "002", "Msg": "content-tyoe non supportato"}), 200


api.run(host="127.0.0.1", port=8080)
