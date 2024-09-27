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



def CreaInterfaccia():
    print("\nOperazioni disponibili:\n")
    print("1. Inserisci cittadino (es: atto di nascita)\n")
    print("2. Richiedi dati del cittadini (es: cert. residenza\n")
    print("3. Modifica dati del cittadino\n")
    print("4. Elimina dati del cittadino\n")
    print("5. Exit\n")

CreaInterfaccia()

SOper = (input("seleziona operazione\n"))

while (SOper != "5"):
    
    if SOper =="1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest =  RichiediDatiCittadino()

        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)

        except:
            print("attenzione problemi")

    
    if SOper == "2":
        api_url = base_url + "/gestisci_dati"
        jsonDataRequest = Gestisci_Dati()

        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)

        except:
            print("attenzione problemi")



    CreaInterfaccia()
    SOper = input("\nSeleziona operazione\n")

    