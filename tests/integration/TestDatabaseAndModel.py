import os
import unittest
import json
import pickle

from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale
from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti


from utente.model.Utente import Utente
from fornitore.model.Fornitore import Fornitore
from ordine.model.Ordine import Ordine
from prodotto.model.Prodotto import Prodotto
from statistica.model.Statistica import Statistica

class TestDatabaseAndModel(unittest.TestCase):

    def setUp(self):
        self.lista_del_personale = []
        self.lista_fornitori = []
        self.lista_ordini = []
        self.lista_prodotti = []
        self.lista_statistiche = []

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
        Test flusso dati DatabaseDelPersonale
    '''

    def test_db_flow_listadelpersonale(self):
        #Testo il caricamento dei file da JSON
        with open('listadelpersonale/data/DatabaseDelPersonale.json') as f:
                lista_del_personale_json = json.load(f)
                for utente_da_caricare in lista_del_personale_json:
                    self.lista_del_personale.append(Utente(utente_da_caricare["cod_utente"],
                                                           utente_da_caricare["nome"],
                                                           utente_da_caricare["cognome"],
                                                           utente_da_caricare["data_nascita"],
                                                           utente_da_caricare["luogo_nascita"],
                                                           utente_da_caricare["cod_fiscale"],
                                                           utente_da_caricare["inizio_lavoro"],
                                                           utente_da_caricare["scad_contratto"],
                                                           utente_da_caricare["ruolo"],
                                                           utente_da_caricare["indirizzo_residenza"],
                                                           utente_da_caricare["n_telefonico"],
                                                           utente_da_caricare["stipendio"],
                                                           utente_da_caricare["username"],
                                                           utente_da_caricare["password"]))

        self.assertIsNotNone(self.lista_del_personale)

        #Testo il salvataggio dei dati su file pickle 
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'wb') as handle:
            pickle.dump(self.lista_del_personale, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file DatabaseDelPersonale.pickle sia stato correttamente creato e popolato
        if os.path.isfile('listadelpersonale/data/DatabaseDelPersonale.pickle') and os.stat('listadelpersonale/data/DatabaseDelPersonale.pickle').st_size != 0:
            pass
        else:
            self.fail("Errore modulo Pickle: Il file DatabaseDelPersonale.pickle non esiste o è vuoto")

        #inserisco un utente di prova
        utente_test = Utente(99999, "Pino", "Sgargi", "18/05/2022", "Torino", "GACMJS22E18L483Z", "18/05/2022", None, "D", "Via fiori 80", 3333333333, 1500, "pinopino", "sgsg")

        lista_t0= len(self.lista_del_personale)
        self.lista_del_personale.append(utente_test)
        lista_t1= len(self.lista_del_personale)
        #verifico che la lista abbia un elemento in più
        self.assertTrue(lista_t1==lista_t0+1)

        #ottengo il numero di utenti salvati sul file pickle
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'rb') as f:
            num_utenti_t0= len(pickle.load(f))

        #salvo l'utente aggiunto in lista
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'wb') as handle:
            pickle.dump(self.lista_del_personale, handle, pickle.HIGHEST_PROTOCOL)

        #rileggo il numero di utenti salvati e verifico che ce ne sia uno in più
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'rb') as f:
            num_utenti_t1= len(pickle.load(f))
            self.assertTrue(num_utenti_t1==num_utenti_t0+1)

        #Elimino tutti gli utenti dalla lista
        self.lista_del_personale.clear()

        #Salvo
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'wb') as handle:
            pickle.dump(self.lista_del_personale, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file contenga 0 utenti salvati
        with open('listadelpersonale/data/DatabaseDelPersonale.pickle', 'rb') as f:
            self.assertTrue(len(pickle.load(f))==0)


    '''
        Test flusso dati DatabaseFornitori
    '''

    def test_db_flow_listafornitori(self):
        #Testo il caricamento dei file da JSON
        with open('listafornitori/data/DatabaseFornitori.json') as f:
                lista_fornitori_json = json.load(f)
                for fornitore_da_caricare in lista_fornitori_json:
                    self.lista_fornitori.append(Fornitore(fornitore_da_caricare["cod_fornitore"],
                                                           fornitore_da_caricare["nome"],
                                                           fornitore_da_caricare["indirizzo"],
                                                           fornitore_da_caricare["telefono"],
                                                           fornitore_da_caricare["partita_iva"],
                                                           fornitore_da_caricare["sito_web"],
                                                           fornitore_da_caricare["rappresentante"],
                                                           fornitore_da_caricare["data_affiliazione"],
                                                           fornitore_da_caricare["stato"]))

        self.assertIsNotNone(self.lista_fornitori)

        #Testo il salvataggio dei dati su file pickle 
        with open('listafornitori/data/DatabaseFornitori.pickle', 'wb') as handle:
            pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file DatabaseFornitori.pickle sia stato correttamente creato e popolato
        if os.path.isfile('listafornitori/data/DatabaseFornitori.pickle') and os.stat('listafornitori/data/DatabaseFornitori.pickle').st_size != 0:
            pass
        else:
            self.fail("Errore modulo Pickle: Il file DatabaseFornitori.pickle non esiste o è vuoto")

        #inserisco un fornitore di prova
        fornitore_test = Fornitore("CA222", "Pino SPA", "Via fiori 80", 3333333333, 86131519727, "www.Pino&pino.com", "Pino Sgargi", "19/05/2022", "P")

        lista_t0= len(self.lista_fornitori)
        self.lista_fornitori.append(fornitore_test)
        lista_t1= len(self.lista_fornitori)
        #verifico che la lista abbia un elemento in più
        self.assertTrue(lista_t1==lista_t0+1)

        #ottengo il numero di fornitori salvati sul file pickle
        with open('listafornitori/data/DatabaseFornitori.pickle', 'rb') as f:
            num_fornitori_t0= len(pickle.load(f))

        #salvo il fornitore aggiunto in lista
        with open('listafornitori/data/DatabaseFornitori.pickle', 'wb') as handle:
            pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)

        #rileggo il numero di fornitori salvati e verifico che ce ne sia uno in più
        with open('listafornitori/data/DatabaseFornitori.pickle', 'rb') as f:
            num_fornitori_t1= len(pickle.load(f))
            self.assertTrue(num_fornitori_t1==num_fornitori_t0+1)

        #Elimino tutti i fornitori dalla lista
        self.lista_fornitori.clear()

        #Salvo
        with open('listafornitori/data/DatabaseFornitori.pickle', 'wb') as handle:
            pickle.dump(self.lista_fornitori, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file contenga 0 forntiori salvati
        with open('listafornitori/data/DatabaseFornitori.pickle', 'rb') as f:
            self.assertTrue(len(pickle.load(f))==0)


    '''
        Test flusso dati DatabaseOrdini
    '''

    def test_db_flow_listaordini(self):
    #Testo il caricamento dei file da JSON
        with open('listaordini/data/DatabaseOrdini.json') as f:
            lista_ordini_json = json.load(f)
            for ordine_da_caricare in lista_ordini_json:
                self.lista_ordini.append(Ordine(ordine_da_caricare ["cod_fattura"],
                                                        ordine_da_caricare ["cod_fornitore"],
                                                        ordine_da_caricare ["stagione"],
                                                        ordine_da_caricare ["stato"],
                                                        ordine_da_caricare ["data_ordine"],
                                                        ordine_da_caricare ["data_arrivo_prevista"],
                                                        ordine_da_caricare ["data_arrivo_effettiva"],
                                                        ordine_da_caricare ["importo_totale"],
                                                        ordine_da_caricare ["calzature_totali"]))

        self.assertIsNotNone(self.lista_ordini)

        #Testo il salvataggio dei dati su file pickle 
        with open('listaordini/data/DatabaseOrdini.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file DatabaseOrdini.pickle sia stato correttamente creato e popolato
        if os.path.isfile('listaordini/data/DatabaseOrdini.pickle') and os.stat('listaordini/data/DatabaseOrdini.pickle').st_size != 0:
            pass
        else:
            self.fail("Errore modulo Pickle: Il file DatabaseFornitori.pickle non esiste o è vuoto")

        #inserisco un ordine di prova
        ordine_test = Ordine(9999, "CA222", "P/E", "In arrivo", "19/04/2022", "22/05/2022", None, 515, 15)

        lista_t0= len(self.lista_ordini)
        self.lista_ordini.append(ordine_test)
        lista_t1= len(self.lista_ordini)
        #verifico che la lista abbia un elemento in più
        self.assertTrue(lista_t1==lista_t0+1)

        #ottengo il numero di ordini salvati sul file pickle
        with open('listaordini/data/DatabaseOrdini.pickle', 'rb') as f:
            num_ordini_t0= len(pickle.load(f))

        #salvo l'ordine aggiunto in lista
        with open('listaordini/data/DatabaseOrdini.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)

        #rileggo il numero di ordini salvati e verifico che ce ne sia uno in più
        with open('listaordini/data/DatabaseOrdini.pickle', 'rb') as f:
            num_ordini_t1= len(pickle.load(f))
            self.assertTrue(num_ordini_t1==num_ordini_t0+1)

        #Elimino tutti gli ordini dalla lista
        self.lista_ordini.clear()

        #Salvo
        with open('listaordini/data/DatabaseOrdini.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file contenga 0 ordini salvati
        with open('listaordini/data/DatabaseOrdini.pickle', 'rb') as f:
            self.assertTrue(len(pickle.load(f))==0)


    '''
        Test flusso dati DatabaseProdotti
    '''

    def test_db_flow_prodotti(self):
    #Testo il caricamento dei file da JSON
        with open('listaprodotti/data/DatabaseProdotti.json') as f:
            lista_prodotti_json = json.load(f)
            for prodotto_da_caricare in lista_prodotti_json:
                self.lista_prodotti.append(Prodotto(prodotto_da_caricare ["cod_fattura"],
                                                        prodotto_da_caricare ["cod_fornitore"],
                                                        prodotto_da_caricare ["data_ordine"],
                                                        prodotto_da_caricare ["cod_prodotto"]
                                                        , prodotto_da_caricare ["marca"],
                                                        prodotto_da_caricare ["nome"],
                                                        prodotto_da_caricare ["tipo"],
                                                        prodotto_da_caricare ["genere"],
                                                        prodotto_da_caricare ["materiale"],
                                                        prodotto_da_caricare ["colore"],
                                                        prodotto_da_caricare ["taglia"],
                                                        prodotto_da_caricare ["quantita"],
                                                        prodotto_da_caricare ["prezzo_acquisto"],
                                                        prodotto_da_caricare ["prezzo_vendita"],
                                                        prodotto_da_caricare ["stagione"],
                                                        prodotto_da_caricare ["stato"],
                                                        prodotto_da_caricare ["sconto_consigliato"],
                                                        prodotto_da_caricare  ["sconto"],
                                                        prodotto_da_caricare ["data_vendita"]))

        self.assertIsNotNone(self.lista_prodotti)

        #Testo il salvataggio dei dati su file pickle 
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file DatabaseProdotti.pickle sia stato correttamente creato e popolato
        if os.path.isfile('listaprodotti/data/DatabaseProdotti.pickle') and os.stat('listaprodotti/data/DatabaseProdotti.pickle').st_size != 0:
            pass
        else:
            self.fail("Errore modulo Pickle: Il file DatabaseFornitori.pickle non esiste o è vuoto")

        #inserisco un prodotto di prova
        prodotto_test = Prodotto(9999, "CA222", "19/04/2022", "S999", "J&J", "Jon & Jon", "Eleganti", "U", "Grafite", "Nero", 43, 1, 30, 70, "P/E", "In negozio", 10, 12, None)

        lista_t0= len(self.lista_prodotti)
        self.lista_prodotti.append(prodotto_test)
        lista_t1= len(self.lista_prodotti)
        #verifico che la lista abbia un elemento in più
        self.assertTrue(lista_t1==lista_t0+1)

        #ottengo il numero di prodotti salvati sul file pickle
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'rb') as f:
            num_prodotti_t0= len(pickle.load(f))

        #salvo il prodotto aggiunto in lista
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)

        #rileggo il numero di prodotti salvati e verifico che ce ne sia uno in più
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'rb') as f:
            num_prodotti_t1= len(pickle.load(f))
            self.assertTrue(num_prodotti_t1==num_prodotti_t0+1)

        #Elimino tutti i prodotti dalla lista
        self.lista_prodotti.clear()

        #Salvo
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)

        #Verifico che il file contenga 0 prodotti salvati
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'rb') as f:
            self.assertTrue(len(pickle.load(f))==0)


    '''
        Test flusso dati DatabaseStatistiche
    '''

    def test_db_flow_statistiche(self):
    #Testo il caricamento dei file da JSON
        with open('listastatistiche/data/DatabaseStatistiche.json') as f:
            lista_statistiche_json = json.load(f)
            for statistica_da_caricare in lista_statistiche_json:
                self.lista_statistiche.append(Statistica(statistica_da_caricare ["nome"],
                statistica_da_caricare ["quantita"],
                statistica_da_caricare ["quantita"]))
                                                        

        self.assertIsNotNone(self.lista_statistiche)


if __name__ == '__main__':
    unittest.main()
