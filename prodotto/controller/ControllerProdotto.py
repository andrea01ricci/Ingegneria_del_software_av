from datetime import datetime

"""
    CONTROLLER DEL PRODOTTO
    Contiene i get e set essenziali per gestire il flusso di dati relativo ai prodotti
"""


class ControllerProdotto:
    def __init__(self, prodotto):
        self.model = prodotto

    # ----------------GET------------------

    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        return self.model.data_ordine

    def get_cod_prodotto(self):
        return self.model.cod_prodotto

    def get_genere(self):
        if self.model.genere == "U":
            return "Uomo"
        elif self.model.genere == "D":
            return "Donna"
        elif self.model.genere == "BO":
            return "Bambino"
        elif self.model.genere == "BA":
            return "Bambina"

    def get_nome(self):
        return self.model.nome

    def get_stagione(self):
        return self.model.stagione

    def get_stato(self):
        return self.model.stato

    # ----------------SET------------------

    def set_cod_fattura(self, cod_fattura):
        if len(cod_fattura) > 2 and cod_fattura.isdecimal():
            self.model.cod_fattura = cod_fattura
        else: 
            raise Exception()


    def set_cod_fornitore(self, cod_fornitore):
        if cod_fornitore.startswith("AD") and cod_fornitore.isalnum() and len(cod_fornitore) < 6:
            self.model.cod_fornitore = cod_fornitore
        else: 
            raise Exception()

    def set_cod_prodotto(self, cod_prodotto):
        if cod_prodotto.startswith("S") and cod_prodotto.isalnum():
            self.model.cod_prodotto = cod_prodotto
        else: 
            raise Exception()

    def set_data_ordine(self, data_ordine):
        if datetime.strptime(data_ordine, "%d/%m/%Y"):
            self.model.data_ordine = data_ordine
        else:
            raise Exception()

    def set_nome(self, nome):
        self.model.nome = nome

    def set_stagione(self, stagione):
        if stagione == "P/E" or stagione == "A/I":
            self.model.stagione = stagione
        else:
            raise Exception()

    def set_stato(self, stato):
        if stato == "In negozio" or stato == "In arrivo":
            self.model.stato = stato
        else:
            raise Exception()

