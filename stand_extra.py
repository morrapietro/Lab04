from stand import Stand

#claase figlia della classe padre "stand"
class StandExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, prese_extra):
        #con la riga di codice successiva sto invocando il metodo def __init__ della claasse padre
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.prese_extra = int(prese_extra)

    def prezzo_finale(self):
        #qui sto overidando
        prezzo_finale = self.prezzo_base * (1 + 0.07 * self.prese_extra)
        return prezzo_finale

    def __str__(self):
        if self.espositore is None:
            return f'{self.codice}: Prese extra | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo_finale():.2f}€ - Prese aggiuntive: {self.prese_extra} - Disponibile'
        else:
            return f'{self.codice}: Prese extra | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo_finale():.2f}€ - Prese aggiuntive: {self.prese_extra} - Assegnato a: {self.espositore}'
