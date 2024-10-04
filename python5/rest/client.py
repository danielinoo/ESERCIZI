import requests, json, sys

base_url = "http://127.0.0.1:8080"


def GetDatiCittadino():
    nome = input("\nInserisci il nome: \n")
    cognome = input("\nInserisci il cognome: \n")
    dataN = input("\nInserisci la data di nascita (gg/mm/aaaa): \n")
    codF = input("\nInserisci il codice fiscale: \n")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    utente = {"username": sUsername,"password": sPassword , "datiCittadino": datiCittadino}
    return utente


def GetCodicefiscale():
    cod = input('\nInserisci codice fiscale: \n')
    return {"codFiscale": cod}


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova più tardi.")

    

def EffettuaPrimoLogin():
    #inserisci username
    #inserisci password
    #componi Jrequest
    #invia richesta al server
    global iPrimoLoginEffetuato
    global sUsername
    global sPassword
    
    sUsername = input("\ninserisci  username utente \n")
    sPassword = input("\ninserisci la password\n ")
    jsonDataRequest = {"email" : sUsername ,"password" : sPassword}
    print(f"login con {sUsername}")
    #collegamento col server
    api_url = base_url + "/login_cittadino"
    response = requests.post(api_url, json=jsonDataRequest)
    #risposta del server
    if response.status_code==200:
        jsonResponse = response.json()
        if jsonResponse["Esito"]=="000":
            print("login effetuato correttamente")
            iPrimoLoginEffetuato = 1
        else:
            print("\nerrore durante il login\n")
    else: 
        print("Problemi di comunicazione con il server, riprova più tardi.")

    
            
   

sUsername = ""
sPassword = ""
iPrimoLoginEffetuato = 0
while  iPrimoLoginEffetuato == 0:
    iPrimoLoginEffetuato = EffettuaPrimoLogin()

while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci\n")


    try:
        iOper = int(input("\nCosa vuoi fare? \n"))
    except ValueError:
        print("\nInserisci un numero valido!\n")
        continue


    if iOper == 1:
        print("Aggiunta cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        EseguiOperazione(1, api_url, jsonDataRequest)

    # Richiesta dati cittadino
    elif iOper == 2:
        print("Richiesta dati cittadino")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = GetCodicefiscale()
        EseguiOperazione(2, api_url + "/" + jsonDataRequest['codFiscale'],None)

    elif iOper == 3:
        print("Modifica cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = GetDatiCittadino()
        EseguiOperazione(3, api_url, jsonDataRequest)


    elif iOper == 4:
        print("Eliminazione cittadino")
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = GetCodicefiscale()
        EseguiOperazione(4, api_url, jsonDataRequest)

    elif iOper == 5:
        print("Buona giornata!")
        sys.exit()

    else:
        print("Operazione non disponibile, riprova.")

