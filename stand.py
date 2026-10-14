#questa classe "stand" rappresenta gli stand standard
#questa è la classe padre
class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = float(prezzo_base)
        self.espositore = None

    #calcolare il prezzo tramite un metodo (prezzo_finale()) invece che usare direttamente
    # l'attributo (prezzo_base) è un trucco fondamentale dell'OOP:
    # quando creeremo gli stand Premium, andremo a sovrascrivere (override) questo
    # metodo per fargli calcolare il sovrapprezzo, ma il resto del codice continuerà a
    # funzionare chiamando semplicemente prezzo_finale()
    def prezzo_finale(self):
        return float(self.prezzo_base)

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.codice == other.codice
        return False

    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.prezzo_finale() < other.prezzo_finale()
        return False

    def __str__(self):
        if self.espositore is None:
            return f'{self.codice}: Standard | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo_finale():.2f}€ - Disponibile'
        else:
            return f'{self.codice}: Standard | {self.superficie} mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo_finale():.2f}€ - Assegnato a: {self.espositore}'



