
import unittest
from ..lezione12bis.ripasso import Calc

class Testcalculations(unittest.TestCase):



    #setup --> prende le variabili della classe da controllare
    def SetUp(self):
        self.calculation = Calc(8,2)

    def test_sum(self):



        #assertEqual-> funzione che permette di verificare se quello che je giro come parametro è uguale al secondo parametro altrimemti passa un messaggio (dopo la seconda virogla)
        self.assertEqual(self.calculation.get_sum(),10,"sbagliato")