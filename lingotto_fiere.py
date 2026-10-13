from espositore import Espositore
from stand import Stand
from stand_extra import StandExtra
from stand_premium import StandPremium

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.insieme_stand = {}
        self.insieme_espositore = {}

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        with open(file_path, "r", encoding="UTF-8") as csvfile:
            for riga_grezza in csvfile:
                riga = riga_grezza.strip().split(",")

                if len(riga) == 3:
                    nuovoEspositore = Espositore(riga[0], riga[1]), riga[2])
                    self.insieme_espositore[riga[0]] = nuovoEspositore

                elif len(riga) == 4:
                    nuovoStandard = Stand(riga[0], riga[1], riga[2], riga[3])
                    self.insieme_stand[riga[0]] = nuovoStandard

                elif len(riga) == 5:
                    if riga[4].isdigit():
                        nuovoExtra = StandExtra(riga[0], riga[1], riga[2], riga[3], riga[4])
                        self.insieme_stand[riga[0]] = nuovoExtra
                    else:
                        nuovoPremium = StandPremium(riga[0], riga[1], riga[2], riga[3], riga[4])
                        self.insieme_stand[riga[0]] = nuovoPremium

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

        #riprndere da punto 6 gemini


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
