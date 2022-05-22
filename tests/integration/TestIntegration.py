import os
import unittest

from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale
from utente.model.Utente import Utente
from utente.controller.ControllerUtente import ControllerUtente

from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from fornitore.model.Fornitore import Fornitore
from fornitore.controller.ControllerFornitore import ControllerFornitore

from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.model.Ordine import Ordine
from ordine.controller.ControllerOrdine import ControllerOrdine

from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from prodotto.model.Prodotto import Prodotto
from prodotto.controller.ControllerProdotto import ControllerProdotto


"""
    CLASSE DI TEST DELLA SEZIONE ORDINE
"""


class TestIntegration(unittest.TestCase):

    def setUp(self):
        #setup listadelpersonale e utente
        self.controller_lista_del_personale= ControllerListaDelPersonale()
        self.utente_test = Utente(99999, "Pino", "Sgargi", "18/05/2022", "Torino", "GACMJS22E18L483Z", "18/05/2022", None, "D", "Via fiori 80", 3333333333, 1500, "pinopino", "sgsg")
        self.controller_utente= ControllerUtente(self.utente_test)

        #setup listafornitori e fornitore
        self.controller_lista_fornitori= ControllerListaFornitori()
        self.fornitore_test = Fornitore("CA222", "Pino SPA", "Via fiori 80", 3333333333, 86131519727, "www.Pino&pino.com", "Pino Sgargi", "19/05/2022", "P")
        self.controller_fornitore= ControllerFornitore(self.fornitore_test)

        #setup listaordini e ordine
        self.controller_lista_ordini= ControllerListaOrdini()
        self.ordine_test = Ordine(9999, "CA222", "P/E", "In arrivo", "19/04/2022", "22/05/2022", None, 515, 15)
        self.controller_ordine= ControllerOrdine(self.ordine_test)

        #setup listaprodotti e prodotto
        self.controller_lista_prodotti= ControllerListaProdotti()
        self.prodotto_test = Prodotto(9999, "CA222", "19/04/2022", "S999", "J&J", "Jon & Jon", "Eleganti", "U", "Grafite", "Nero", 43, 1, 30, 70, "P/E", "In negozio", 10, 12, None)
        self.controller_prodotto= ControllerProdotto(self.prodotto_test)
    
    def tearDown(self):

        #finiti i test riprisitino il database eliminando i pickle e riprendendo i file da json
        
        if os.path.isfile('listadelpersonale/data/DatabaseDelPersonale.pickle'):
            os.remove('listadelpersonale/data/DatabaseDelPersonale.pickle')

        if os.path.isfile('listafornitori/data/DatabaseFornitori.pickle'):
            os.remove('listafornitori/data/DatabaseFornitori.pickle')

        if os.path.isfile('listaordini/data/DatabaseOrdini.pickle'):
            os.remove('listaordini/data/DatabaseOrdini.pickle')

        if os.path.isfile('listaprodotti/data/DatabaseProdotti.pickle'):
            os.remove('listaprodotti/data/DatabaseProdotti.pickle')

        self.controller_lista_del_personale= ControllerListaDelPersonale()
        self.controller_lista_fornitori= ControllerListaFornitori()
        self.controller_lista_ordini= ControllerListaOrdini()
        self.controller_lista_prodotti= ControllerListaProdotti()

        self.controller_lista_del_personale.refresh_data()
        self.controller_lista_del_personale.save_data()
        self.controller_lista_fornitori.refresh_data()
        self.controller_lista_fornitori.save_data()
        self.controller_lista_ordini.refresh_data()
        self.controller_lista_ordini.save_data()
        self.controller_lista_prodotti.refresh_data()
        self.controller_lista_prodotti.save_data()
        



    '''
        Test modulo listadelpersonale e utente
    '''

    def test_listadelpersonale(self):
        
        lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()

        #inserimento di un utente
        lista_t0= len(lista_del_personale)
        
        self.controller_lista_del_personale.inserisci_utente(self.utente_test)
        lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()
        lista_t1= len(lista_del_personale)
        self.assertTrue(lista_t1==lista_t0+1)
        self.assertTrue(self.utente_test in lista_del_personale)

        #modifica di un utente
        self.assertFalse(self.controller_utente.get_nome() == "Edoardo")
        self.controller_utente.set_nome("Edoardo")
        self.assertTrue(self.controller_utente.get_nome() == "Edoardo")

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_del_personale.refresh_data()
        lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()
        self.assertTrue(self.utente_test not in lista_del_personale)
        #reinserisco l'utente
        self.controller_lista_del_personale.inserisci_utente(self.utente_test)
        self.controller_lista_del_personale.save_data()
        self.controller_lista_del_personale.refresh_data()
        self.assertTrue(self.utente_test in lista_del_personale)

        #eliminazione di un utente
        ultimo_utente = lista_del_personale[-1]
        self.controller_lista_del_personale.elimina_utente(ultimo_utente)
        lista_del_personale= self.controller_lista_del_personale.get_lista_del_personale()
        self.assertTrue(ultimo_utente not in lista_del_personale) 

    '''
        Test modulo listafornitori e fornitore
    '''

    def test_listafornitori(self):
        
        lista_fornitori = self.controller_lista_fornitori.get_lista_fornitori()

        #inserimento di un fornitore
        lista_t0= len(lista_fornitori)
        
        self.controller_lista_fornitori.inserisci_fornitore(self.fornitore_test)
        lista_fornitori = self.controller_lista_fornitori.get_lista_fornitori()
        lista_t1= len(lista_fornitori)
        self.assertTrue(lista_t1==lista_t0+1)
        self.assertTrue(self.fornitore_test in lista_fornitori)

        #modifica di un fornitore
        self.assertFalse(self.controller_fornitore.get_nome() == "EdoardoSPA")
        self.controller_fornitore.set_nome("EdoardoSPA")
        self.assertTrue(self.controller_fornitore.get_nome() == "EdoardoSPA")

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_fornitori.refresh_data()
        lista_fornitori = self.controller_lista_fornitori.get_lista_fornitori()
        self.assertTrue(self.fornitore_test not in lista_fornitori)
        #reinserisco il fornitore
        self.controller_lista_fornitori.inserisci_fornitore(self.fornitore_test)
        self.controller_lista_fornitori.save_data()
        self.controller_lista_fornitori.refresh_data()
        self.assertTrue(self.fornitore_test in lista_fornitori)

        #eliminazione di un fornitore
        ultimo_fornitore = lista_fornitori[-1]
        self.controller_lista_fornitori.elimina_fornitore(ultimo_fornitore)
        lista_fornitori= self.controller_lista_fornitori.get_lista_fornitori()
        self.assertTrue(ultimo_fornitore not in lista_fornitori) 


    '''
        Test modulo listaordini e ordine
    '''
    def test_listaordini(self):
        
        lista_ordini = self.controller_lista_ordini.get_lista_ordini()

        #inserimento di un ordine
        lista_t0= len(lista_ordini)
        
        self.controller_lista_ordini.inserisci_ordine(self.ordine_test)
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        lista_t1= len(lista_ordini)
        self.assertTrue(lista_t1==lista_t0+1)
        self.assertTrue(self.ordine_test in lista_ordini)

        #modifica di un ordine
        self.assertFalse(self.controller_ordine.get_cod_fattura() == "1111")
        self.controller_ordine.set_cod_fattura("1111")
        self.assertTrue(self.controller_ordine.get_cod_fattura() == "1111")

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_ordini.refresh_data()
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        self.assertTrue(self.ordine_test not in lista_ordini)
        #reinserisco l'ordine
        self.controller_lista_ordini.inserisci_ordine(self.ordine_test)
        self.controller_lista_ordini.save_data()
        self.controller_lista_ordini.refresh_data()
        self.assertTrue(self.ordine_test in lista_ordini)

        #eliminazione di un fornitore
        ultimo_ordine = lista_ordini[-1]
        self.controller_lista_ordini.elimina_ordine(ultimo_ordine)
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        self.assertTrue(ultimo_ordine not in lista_ordini) 

    '''
        Test modulo listaprodotti e prodotto
    '''
    def test_listaprodotti(self):
        
        lista_prodotti = self.controller_lista_prodotti.get_lista_prodotti()

        #inserimento di un prodotto
        lista_t0= len(lista_prodotti)
        
        self.controller_lista_prodotti.inserisci_prodotto(self.prodotto_test)
        lista_prodotti= self.controller_lista_prodotti.get_lista_prodotti()
        lista_t1= len(lista_prodotti)
        self.assertTrue(lista_t1==lista_t0+1)
        self.assertTrue(self.prodotto_test in lista_prodotti)

        #modifica di un prodotto
        self.assertFalse(self.controller_prodotto.get_nome() == "Nike")
        self.controller_prodotto.set_nome("Nike")
        self.assertTrue(self.controller_prodotto.get_nome() == "Nike")

        #refresh e salvataggio della lista
        #testo che se non salvo, con il refresh perdo le ultime modifiche
        self.controller_lista_ordini.refresh_data()
        lista_ordini= self.controller_lista_ordini.get_lista_ordini()
        self.assertTrue(self.ordine_test not in lista_ordini)
        #reinserisco il prodotto
        self.controller_lista_prodotti.inserisci_prodotto(self.prodotto_test)
        self.controller_lista_prodotti.save_data()
        self.controller_lista_prodotti.refresh_data()
        self.assertTrue(self.prodotto_test in lista_prodotti)

        #eliminazione di un prodotto
        ultimo_prodotto = lista_prodotti[-1]
        self.controller_lista_prodotti.elimina_prodotto(ultimo_prodotto)
        lista_prodotti= self.controller_lista_prodotti.get_lista_prodotti()
        self.assertTrue(ultimo_prodotto not in lista_prodotti) 



if __name__ == '__main__':
    unittest.main()