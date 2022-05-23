import unittest
from prodotto.controller.ControllerProdotto import ControllerProdotto

from prodotto.model.Prodotto import Prodotto

"""
    CLASSE DI TEST DELLA SEZIONE ORDINE
"""


class TestProdotto(unittest.TestCase):

    def setUp(self):
        self.prodotto = Prodotto(cod_fattura=100, cod_fornitore="AD000", data_ordine="28/07/2020", cod_prodotto="S01",
                            marca="Pier One", nome=None, tipo="Eleganti", genere="U", materiale="Grafite",
                            colore="Nero", taglia=49,
                            quantita=1, prezzo_acquisto=60, prezzo_vendita=120, stagione="P/E", stato="Venduto",
                            sconto_consigliato=20, sconto=15, data_vendita="26/03/2021")
        self.Controller_Prodotto = ControllerProdotto(self.prodotto)

    # Test di ControllerProdotto
    def test_set_cod_fattura(self):
        right_code = "150"
        wrong_code = "5"
        try:
            self.Controller_Prodotto.set_cod_fattura(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_cod_fattura(right_code)
        except (Exception,):
            self.fail()

    def test_set_cod_fornitore(self):
        right_code = "AD001"
        wrong_code = "P0023"
        try:
            self.Controller_Prodotto.set_cod_fornitore(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_cod_fornitore(right_code)
        except (Exception,):
            self.fail()

    def test_set_cod_prodotto(self):
        right_code = "S01"
        wrong_code = "A101"
        try:
            self.Controller_Prodotto.set_cod_prodotto(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_cod_prodotto(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_ordine(self):
        right_code = "28/07/2020"
        wrong_code = "10-08-2023"
        try:
            self.Controller_Prodotto.set_data_ordine(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_data_ordine(right_code)
        except (Exception,):
            self.fail()

    def test_set_stagione(self):
        right_code = "P/E"
        wrong_code = "E-I"
        try:
            self.Controller_Prodotto.set_stagione(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_stagione(right_code)
        except (Exception,):
            self.fail()

    def test_set_stato(self):
        right_code = "In negozio"
        wrong_code = "in_negozio"
        try:
            self.Controller_Prodotto.set_stato(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Prodotto.set_stato(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
            
