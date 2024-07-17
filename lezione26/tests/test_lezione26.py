#Daniele Pietropao


from unittest import TestCase

import lezione26
import lezione26.lezione26


class Test_cifraturaAscorrimento(TestCase):

    def setUp(self) -> None:
        self.a = lezione26.lezione26.CifratoreAScorrimento(chiave= 3)

    def test_codifica(self):

        codif = self.a.codifica(testoInChiaro = "ciao")
        self.assertEqual("fldr",codif,"errore codifica sbagliata")

        decodif = self.a.decodifica(testoCodificato= "fldr")
        self.assertEqual("ciao",decodif,"decodifica sbagliata")