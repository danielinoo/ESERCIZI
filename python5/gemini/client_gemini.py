import requests, json, sys


#base api google
sGoogleApiKey = "AIzaSyCo1uqjaqpyx-6a04ow5dEL7c6uVacdjY4"

#modello di AI che si vuole interrogare
sModel = "gemini-1.5-pro-exp-0827" 

#ulr collegamneto di google con propria base api key
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="
api_url = base_url + sGoogleApiKey


iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Inserisci una coppia (file,domanda)")
    print("3. Esci")
    
    iOper = int(input("Cosa vuoi fare? "))

    if iOper == 1:
        squery = input("cosa vuoi chiedere?")
        jsonDataRequest = {"contests" : [{"parts" : [{"text": squery}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify=True)
        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
            

    #coppia (file,domanda)
    elif iOper == 2:
        print("servizio da gestire")

    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")



