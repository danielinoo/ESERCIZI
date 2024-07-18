#Daniele Pietropaolo


import unittest

from cifratura import CifratoreAScorrimento,CodificaACombinazione



class Test_cifraturaAscorrimento(unittest.TestCase):

    def setUp(self) -> None:
        self.a = CifratoreAScorrimento(chiave= 3)

    def test_codifica(self):

        codif = self.a.codifica(testoInChiaro = "ciao")
        self.assertEqual("fldr",codif,"errore codifica sbagliata")
        
    def test_decodifica(self):

        decodif = self.a.decodifica(testoCodificato= "fldr")
        self.assertEqual("ciao",decodif,"decodifica sbagliata")


class Test_codificaACombinazione(unittest.test):

    def setUp(self):

        self.a = CodificaACombinazione(chiave = 3)

    def test_codifica(self):

        codif = self.a.codifica(testoInChiaro=)

        self.


if __name__ == "__main__":
    unittest.main()