from flask import Flask, render_template ,request

api = Flask(__name__)

utenti = [["mario","rossi","via tiburtina","Roma","2000-09-25","0"],["gigi","bianchi","via nomentana","Roma","2002-10-01","0"],["pasquale","verdi","via navigli","Milano","1999-16-04","0"]]


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/regok', methods=['GET'])
def regOk():
    return render_template('reg_ok.html')


@api.route('/regko', methods=['GET'])
def regKo():
    return render_template('reg_ko.html')



@api.route('/registrazione', methods=['GET'])
def registrazione():

    nome = request.args.get("nome")
    cognome = request.args.get("cognome")
    dataNascita = request.args.get("dataNascita")
    indirizzo = request.args.get("indirizzo")
    citta = request.args.get("citta")

    l : list[str] = [nome,cognome,indirizzo,citta,dataNascita,"0"]
    for i in utenti:
        if l == i:
                i[-1] = "1"
                return render_template('reg_ok.html')
        
    return render_template('reg_ko.html')






api.run(host ="0.0.0.0",port=8085)