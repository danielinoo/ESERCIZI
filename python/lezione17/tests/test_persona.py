#Daniele Pietropaolo

### Creazione di Test Case con UnitTest

# Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
# Istruzioni
# Creare un nuovo file Python denominato "test_persona.py".
# Importare il modulo unittest e tutte le classi definite.

# Test della Classe Persona
# - Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi first_name, last_name e age.
#   - Il funzionamento dei metodi setName, setLastName e setAge.

# Test della Classe Dottore
# - Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Dottore.
#   - Il funzionamento del metodo isValidDoctor con diverse età.

# Test della Classe Paziente
# - Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta degli attributi specifici di Paziente.

# Test della Classe Fattura
# - Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
# - Scrivere test per verificare:
#   - L'inizializzazione corretta della classe Fattura.
#   - Il calcolo corretto del salario e del numero di fatture.
#   - L'aggiunta e la rimozione di pazienti dalla lista.





import unittest
from gestione_ospedale.persona import Persona

class TestPersona(unittest.TestCase):

    def setUp(self) -> None:
        self.persona_1 : Persona = Persona("riccardo","bianchi")


    def test_attributi(self):

        self.assertEqual(self.persona_1.getName(),"riccardo")
        self.assertEqual(self.persona_1.getLastname(),"bianchi")
        self.assertEqual(self.persona_1.age,0)

        self.persona_1.setName("marco")
        self.persona_1.setLastName("rossi")
        self.persona_1.setAge(20)

        self.assertEqual(self.persona_1.getName(),"marco")
        self.assertEqual(self.persona_1.getLastname(),"rossi")
        self.assertEqual(self.persona_1.age,20)



from gestione_ospedale.dottore import Dottore

class TestDottore(unittest.TestCase):

        def setUp(self) -> None:
            self.dottore_1 : Dottore = Dottore("riccardo","bianchi","dietologo",15.5)

            self.dottore_1.setAge(35)

        def test_attributi(self):

            self.assertEqual(self.dottore_1.getName(),"riccardo")
            self.assertEqual(self.dottore_1.getLastname(),"bianchi")
            self.assertEqual(self.dottore_1.getParcel(),15.5)

    




from gestione_ospedale.paziente import Paziente

class TestPaziente(unittest.TestCase):
     
    def setUp(self) -> None:
         
        self.paziente_1 = Paziente("frank","verdi","12345")
        self.paziente_1.setAge(20)

    def test_attributi(self):

        self.assertEqual(self.paziente_1.getName(),"frank")
        self.assertEqual(self.paziente_1.getLastname(),"verdi")
        self.assertEqual(self.paziente_1.age,20)





from gestione_ospedale.fatture import Fattura

class TestFattura(unittest.TestCase):

    def setUp(self) -> None:

        self.paziente_1 = Paziente("frank","verdi","12345")
        self.paziente_1.setAge(20)
        self.paziente_2 = Paziente("maurizio","bianchi","56783")
        self.paziente_2.setAge(40)

        self.dottore_1 : Dottore = Dottore("riccardo","esposito","dietologo",30)
        self.dottore_1.setAge(35)
        


        self.fattura_1 = Fattura(pazienti=[self.paziente_1],doctor=self.dottore_1)

    
    def test_fattura(self):

        self.fattura_1.addPatient(self.paziente_2)
        self.assertEqual(len(self.fattura_1.pazienti),2)

        self.fattura_1.getFatture()
        self.fattura_1.getSalary(self)
        self.assertNotEqual(self.fattura_1.salary,0)
        self.assertNotEqual(self.fattura_1.fatture,0)

        self.fattura_1.removePatient(self.paziente_1)
        self.assertEqual((len(self.fattura_1.pazienti),1))

    

if __name__ == "__main__":
    unittest.main()