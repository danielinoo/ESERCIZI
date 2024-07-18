#Daniele Pietropao


import unittest

from lezione26.cifratura import CifratoreAScorrimento



class Test_cifraturaAscorrimento(unittest.TestCase):

    def setUp(self) -> None:
        self.a = CifratoreAScorrimento(chiave= 3)

    def test_codifica(self):

        codif = self.a.codifica(testoInChiaro = "ciao")
        self.assertEqual("fldr",codif,"errore codifica sbagliata")
        
    def test_decodifica(self):

        decodif = self.a.decodifica(testoCodificato= "fldr")
        self.assertEqual("ciao",decodif,"decodifica sbagliata")


if __name__ == "__main__":
    unittest.main()