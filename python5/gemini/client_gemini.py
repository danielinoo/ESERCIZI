
import requests
import sys
import myjson as mj

#modello di AI che sto usando
sModel = "gemini-1.5-pro-exp-0827"
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="

#api key di google
sGoogleApiKey = "AIzaSyCo1uqjaqpyx-6a04ow5dEL7c6uVacdjY4"

api_url = base_url + sGoogleApiKey


print("Benvenuti in Google GEMINI")

while True:
    print("\nOperazioni disponibili: ")
    print("1. Chiedi una domanda")
    print("2. Inserisci una coppia(file, domanda)")
    print("3. Esci")

    iOper = int(input('Inserisci opzione: '))
    if iOper == 1:
        sQuery = input('Cosa vuoi chiedere? ')
        jsonDataRequest = {"contents": [{"parts": [{"text" : sQuery}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify= True) # VERIFY true ---> verifica il certificato  VERIFY false ---> non verifica il certificato

        if response.status_code == 200:
            a = response.json()
            #restituisce in maniera pulita la risposta
            answer = {"answer": a["candidates"][0]["content"]["parts"][0]["text"]}

            #salva le risposte nel file json
            mj.serializza_json(answer, "answer.json")

            #stampo risposta
            print(f"\n{answer["answer"]}")
        else:
            print("ATTENZIONE,ERRORE")

    elif iOper == 2:
        print("Servizio da gestire")


    elif iOper == 3:
        sys.exit()

    else:
        print("Operazione non disponibile, riprova.")
