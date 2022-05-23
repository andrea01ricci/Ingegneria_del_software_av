import unittest

from fornitore.controller.ControllerFornitore import ControllerFornitore

from fornitore.model.Fornitore import Fornitore

"""
    CLASSE DI TEST DELLA SEZIONE FORNITORE
"""


class TestFornitore(unittest.TestCase):

    def setUp(self):
        self.fornitore = Fornitore(cod_fornitore="AD008", nome="Geox", indirizzo="Via Giuseppe Garibaldi",
                                   telefono="32545345",
                                   partita_iva="11256971425", sito_web="https://www.geox.it/",
                                   rappresentante="Gianni Rossi",
                                   data_affiliazione="10/01/2010", stato="P")

        self.Controller_Fornitore = ControllerFornitore(self.fornitore)

    # Test di ControllerFornitore
    def test_set_cod_fornitore(self):
        right_code = "AD005"
        wrong_code = "GHF005"
        try:
            self.Controller_Fornitore.set_cod_fornitore(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_cod_fornitore(right_code)
        except (Exception,):
            self.fail()

    def test_set_nome(self):
        right_code = "Provaa"
        wrong_code = "Prova34bg4ta"
        try:
            self.Controller_Fornitore.set_nome(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_nome(right_code)
        except (Exception,):
            self.fail()

    def test_set_indirizzo(self):
        right_code = "Via roma"
        wrong_code = "a"
        try:
            self.Controller_Fornitore.set_indirizzo(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_indirizzo(right_code)
        except (Exception,):
            self.fail()

    def test_set_partita_iva(self):
        right_code = "81334418114"
        wrong_code = "IT025466G256"
        try:
            self.Controller_Fornitore.set_partita_iva(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_partita_iva(right_code)
        except (Exception,):
            self.fail()

    def test_set_telefono(self):
        right_code = "836599"
        wrong_code = "5624866a"
        try:
            self.Controller_Fornitore.set_telefono(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_telefono(right_code)
        except (Exception,):
            self.fail()

    def test_set_sito_web(self):
        right_code = "https://www.imac-italia.it"
        wrong_code = "geox.com"
        try:
            self.Controller_Fornitore.set_sito_web(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_sito_web(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_affiliazione(self):
        right_code = "11/11/2019"
        wrong_code = "2055-12-01"
        try:
            self.Controller_Fornitore.set_data_affiliazione(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_data_affiliazione(right_code)
        except (Exception,):
            self.fail()

    def test_set_stato(self):
        right_code = "Standard"
        wrong_code = "Storico"
        try:
            self.Controller_Fornitore.set_stato(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Fornitore.set_stato(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
