from flask import Flask, render_template ,request

api = Flask(__name__)

utenti = [["mario","rossi","via tiburtina","Roma","2000-09-25","0"],["gigi","bianchi","via nomentana","Roma","2002-10-01","0"],["pasquale","verdi","via navigli","Milano","1999-16-04","0"]]


@api.route('/', methods=['GET'])
def primapagina():
    return render_template('primapagina.html')

@api.route('/registra', methods=['GET'])
def registra():
    return render_template('registra.html')


@api.route('/accedi', methods=['GET'])
def accedi():
    return render_template('accesso.html')

@api.route('/ordini', methods=['GET'])
def ordini():
    return render_template('ordini.html')

#creare serie di controlli per far visualizzare all utente la propria lista di ordini
@api.route('/passati', methods=['GET'])
def passati():
    return render_template('ordini_passati.html')

@api.route('/attuali', methods=['GET']) #methods = ['GET', 'POST'] --> se si vuole usare pure post 
def attuali():
    return render_template('ordini_attuali.html')

@api.route('/controllo_registrazione', methods=['GET'])
def controllo_reg():

    nome = request.args.get("nome")
    #nome = request.form['nome'] --> con metodo post
    cognome = request.args.get("cognome")
    dataNascita = request.args.get("dataNascita")
    indirizzo = request.args.get("indirizzo")
    citta = request.args.get("citta")

    lr : list[str] = [nome,cognome,indirizzo,citta,dataNascita,"0"]
    for i in utenti:
        if lr == i:
                i[-1] = "1"
                return render_template('reg_ok.html',nome=nome,cognome=cognome)
        
    return render_template('reg_ko.html')


@api.route('/controllo_accesso',methods= ['GET'])
def controllo_accesso():

    nome = request.args.get("nome")
    cognome = request.args.get("cognome")
    la : list[str] = [nome,cognome]

    for i in utenti:
        if la[0] == i[0] and la[1] == i[1] and i[-1] == "1":
             
            return render_template('acc_ok.html',nome=nome,cognome=cognome)
    
        return render_template('acc_ko.html')



api.run(host ="0.0.0.0",port=8085)