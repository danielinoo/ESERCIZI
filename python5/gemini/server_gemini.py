from flask import Flask, render_template ,request,jsonify
import requests


api = Flask(__name__)
#modello di AI che sto usando
sModel = "gemini-1.5-pro-exp-0827"
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="

#api key di google
sGoogleApiKey = "AIzaSyAAs2zpIStk9hHteZz0M8CRkwdbPPK6GBQ"

api_url = base_url + sGoogleApiKey

@api.route('/', methods=['GET'])
def primapagina():
    return render_template('prima.html')


@api.route('/1', methods=['GET'])
def registra():
    context = {'risposta': '',
               'chiesto':False}
    return render_template('domanda.html')

@api.route('/risposta', methods = ['GET'])
def risposta():
    domanda = request.args.get('domanda')
    jsonDataRequest = {"contents": [{"parts": [{"text": domanda}]}]}
    response = requests.post(api_url, json=jsonDataRequest, verify=True)

    if response.status_code == 200:
        a = response.json()
        answer = a["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({'answer': answer})
    else:
        return jsonify({'answer': 'Mi dispiace, si è verificato un errore con la richiesta.'}), 500






api.run(host ="0.0.0.0",port=8085)