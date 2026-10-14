from stand import  Stand

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def prezzo_finale(self):
        prezzo_finale = self.prezzo_base * 1.30
        return prezzo_finale

    def __str__(self):
        if self.espositore is None:
            return f'{self.codice}: Premium | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo_finale():.2f}€ - Posizione: {self.posizione} - Disponibile'
        else:
            return f'{self.codice}: Premium | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo_finale():.2f}€ - Posizione: {self.posizione} - Assegnato a: {self.espositore}'

