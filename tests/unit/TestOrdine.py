import unittest

from ordine.controller.ControllerOrdine import ControllerOrdine

from ordine.model.Ordine import Ordine

"""
    CLASSE DI TEST DELLA SEZIONE ORDINE
"""


class TestOrdine(unittest.TestCase):

    def setUp(self):
        self.ordine = Ordine(cod_fattura="100", cod_fornitore="AD000", stagione="P/E", stato="In negozio",
                                   data_ordine="2020-07-28", data_arrivo_prevista="2021-02-22",
                                   data_arrivo_effettiva="2021-02-22",
                                   importo_totale="3869", calzature_totali="88")

        self.Controller_Ordine = ControllerOrdine(self.ordine)

    # Test di ControllerOrdine
    def test_set_cod_fattura(self):
        right_code = "150"
        wrong_code = "5"
        try:
            self.Controller_Ordine.set_cod_fattura(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_cod_fattura(right_code)
        except (Exception,):
            self.fail()

    def test_set_cod_fornitore(self):
        right_code = "AD001"
        wrong_code = "P0023"
        try:
            self.Controller_Ordine.set_cod_fornitore(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_cod_fornitore(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_ordine(self):
        right_code = "2020-07-14"
        wrong_code = "10-02-2023"
        try:
            self.Controller_Ordine.set_data_ordine(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_data_ordine(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_arrivo_prevista(self):
        right_code = "2020-07-10"
        wrong_code = "10-08-2023"
        try:
            self.Controller_Ordine.set_data_arrivo_prevista(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_data_arrivo_prevista(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_arrivo_effettiva(self):
        right_code = "2020-07-10"
        wrong_code = "10-08-2023"
        try:
            self.Controller_Ordine.set_data_arrivo_effettiva(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_data_arrivo_effettiva(right_code)
        except (Exception,):
            self.fail()

    def test_set_stagione(self):
        right_code = "P/E"
        wrong_code = "E-I"
        try:
            self.Controller_Ordine.set_stagione(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_stagione(right_code)
        except (Exception,):
            self.fail()

    def test_set_stato(self):
        right_code = "In negozio"
        wrong_code = "in_negozio"
        try:
            self.Controller_Ordine.set_stato(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Ordine.set_stato(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
