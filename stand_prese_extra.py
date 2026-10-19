
from stand import Stand

class StandPreseExtra(Stand):
    def __init__(self,codice,superficie,padiglione,prezzobase,numeroprese):
        super().__init__(codice,superficie,padiglione,prezzobase)
        self.__numeroprese=numeroprese # attributo specifico della classe figlia

    @property
    def numeroprese(self):
        return self.__numeroprese

    def calcola_prezzo(self):
        return super().calcola_prezzo() * (1 + 0.07 * self.__numeroprese) # super().calcola_prezzo()  recupera il prezzo
                                                                        #base attraverso il metodo della classe padre

    def __str__(self):
        return f'{self.codice}: prese extra | {self.superficie}mq - {self.padiglione} -prezzo {self.calcola_prezzo():.2f}euro - prese {self.__numeroprese}'



