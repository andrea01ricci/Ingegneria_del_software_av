import unittest

from utente.controller.ControllerUtente import ControllerUtente

from utente.model.Utente import Utente

"""
    CLASSE DI TEST DELLA SEZIONE PERSONALE
"""


class TestPersonale(unittest.TestCase):

    def setUp(self):
        self.utente = Utente(cod_utente=1, nome="Antonio", cognome="Morelli", data_nascita="16/11/1961",
                                   luogo_nascita="Milano", cf="ZZINTN61S16E799U",
                                   data_inizio_contratto="01/11/1990", data_scadenza_contratto= None, ruolo="A",
                                   indirizzo="Via Marconi, 6", telefono="3430217459",
                                    stipendio=None, username="izziantonio61", password="260234")

        self.Controller_Utente = ControllerUtente(self.utente)

    # Test di ControllerFornitore
    def test_set_cod_utente(self):
        right_code = "1"
        wrong_code = "U1"
        try:
            self.Controller_Utente.set_cod_utente(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_cod_utente(right_code)
        except (Exception,):
            self.fail()

    def test_set_nome(self):
        right_code = "Provaa"
        wrong_code = "Prova34bg4ta"
        try:
            self.Controller_Utente.set_nome(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_nome(right_code)
        except (Exception,):
            self.fail()

    def test_set_cognome(self):
        right_code = "Provaa"
        wrong_code = "Prova34bg4ta"
        try:
            self.Controller_Utente.set_cognome(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_cognome(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_nascita(self):
        right_code = "11/11/2019"
        wrong_code = "2055-12-01"
        try:
            self.Controller_Utente.set_data_nascita(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_data_nascita(right_code)
        except (Exception,):
            self.fail()

    def test_set_luogo_nascita(self):
        right_code = "Milano"
        wrong_code = "Roma 2"
        try:
            self.Controller_Utente.set_luogo_nascita(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_luogo_nascita(right_code)
        except (Exception,):
            self.fail()

    def test_set_cf(self):
        right_code = "ZZINTN61S16E799U"
        wrong_code = "ZZINTN61S16E799UZ"
        try:
            self.Controller_Utente.set_cf(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_cf(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_inizio_contratto(self):
        right_code = "11/11/2019"
        wrong_code = "2055-12-01"
        try:
            self.Controller_Utente.set_data_inizio_contratto(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_data_inizio_contratto(right_code)
        except (Exception,):
            self.fail()

    def test_set_data_scadenza_contratto(self):
        right_code = "11/11/2019"
        wrong_code = "2055-12-01"
        try:
            self.Controller_Utente.set_data_scadenza_contratto(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_data_scadenza_contratto(right_code)
        except (Exception,):
            self.fail()

    def test_set_ruolo(self):
        right_code = "D"
        wrong_code = "P"
        try:
            self.Controller_Utente.set_ruolo(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_ruolo(right_code)
        except (Exception,):
            self.fail()

    def test_set_telefono(self):
        right_code = "3430217459"
        wrong_code = "343s02174A59"
        try:
            self.Controller_Utente.set_telefono(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_telefono(right_code)
        except (Exception,):
            self.fail()

    def test_set_stipendio(self):
        right_code = "800"
        wrong_code = "500d"
        try:
            self.Controller_Utente.set_stipendio(wrong_code)
        except (Exception,):
            print("Eccezione gestita correttamente")
        else:
            self.fail()
        try:
            self.Controller_Utente.set_stipendio(right_code)
        except (Exception,):
            self.fail()

if __name__ == '__main__':
    unittest.main()
