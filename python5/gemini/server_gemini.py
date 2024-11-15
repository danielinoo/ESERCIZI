from flask import Flask, render_template ,request
import requests


api = Flask(__name__)
#modello di AI che sto usando
sModel = "gemini-1.5-pro-exp-0827"
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="

#api key di google
sGoogleApiKey = "AIzaSyCo1uqjaqpyx-6a04ow5dEL7c6uVacdjY4"

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
    domanda = request.args.get['domanda']
    jsonDataRequest = {"contents": [{"parts": [{"text" : domanda}]}]}
    response = requests.post(api_url, json=jsonDataRequest, verify= True) # VERIFY true ---> verifica il certificato  VERIFY false ---> non verifica il certificato

    if response.status_code == 200:

            a = response.json()
            #restituisce in maniera pulita la risposta
            answer = {"answer": a["candidates"][0]["content"]["parts"][0]["text"]}
            #salva le risposte nel file json
            # mj.serializza_json(answer, "answer.json")

            context = {'risposta' : answer,
                       'chiesto' : True}
            #stampo risposta
            return render_template('domanda.html',**context)
    else:
            print("ATTENZIONE,ERRORE")





api.run(host ="0.0.0.0",port=8085)