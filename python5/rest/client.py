import json, requests

base_url = "http://127.0.0.1:8080"


def RichiediDatiCittadino():
    nome = input("\ninserisci il nome: \n")
    cognome = input("\ninserisci il cognome: \n")
    dataNascita = input("\ninserisci la data di nascita: \n")
    codFiscale = input("\ninserisci il codice fiscale: \n")
    jRequest = {"nome" : nome, "cognome" : cognome, "data di nascita" : dataNascita, "codice fiscale" : codFiscale}
    return jRequest

def Gestisci_Dati():
    jRequest = input("inserisci il codice fiscale del cittadino per vedere i suoi dati\n")
    return jRequest

def modifica_cit():
    print("\nse non vuoi modificare scrivi \"salta\"\n")
    codFiscale = input("inserisci il codice fiscale del cittadino che vuoi modificare i dati\n")
    nome = input("\ninserisci il nuovo nome: \n")
    cognome = input("\ninserisci il nuovo cognome: \n")
    dataNascita = input("\ninserisci la nuova data di nascita: \n")
    jRequest = {"nome" : nome, "cognome" : cognome, "data di nascita" : dataNascita, "codice fiscale" : codFiscale}
    return jRequest 

def elimina_cit():
    jRequest = input("inserisci il codice fiscale del cittadino che vuoi eliminare\n")
    return jRequest


def CreaInterfaccia():
    print("\nOperazioni disponibili:\n")
    print("1. Inserisci cittadino (es: atto di nascita)\n")
    print("2. Richiedi dati del cittadini (es: cert. residenza\n")
    print("3. Modifica dati del cittadino\n")
    print("4. Elimina dati del cittadino\n")
    print("5. Exit\n")

CreaInterfaccia()

def EseguiOperazione(iOper,sServizio,dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json= dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json= dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json= dDatiToSend)
        if response.status_code==200:
            print(response.json())
        else:
            print("attenzione problemi"+ str(response.status_code))
    except:
        print("\nproblemi di comunicazione col server\n")

SOper = (input("seleziona operazione\n"))

while (SOper != "5"):

    try:
        SOper = int(input("seleziona operazione\n"))
    except ValueError:
        print("numero non valido")
        continue
    
    if SOper ==1:
        api_url = base_url + "/add_cittadino"
        jsonDataRequest =  RichiediDatiCittadino()
        EseguiOperazione(1,api_url,jsonDataRequest)

    
    elif SOper == 2:
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = Gestisci_Dati()
        EseguiOperazione(2,api_url,jsonDataRequest)




    elif SOper == 3:
        print("Modifica cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = modifica_cit()
        EseguiOperazione(3,api_url,jsonDataRequest)

    
    elif SOper == 4:
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = elimina_cit()
        EseguiOperazione(4,api_url,jsonDataRequest)



    CreaInterfaccia()
    SOper = input("\nSeleziona operazione\n")

    