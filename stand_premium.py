
from stand import Stand

class StandPremium(Stand):
    def __init__(self,codice,superficie,padiglione,prezzobase,posizione):
        super().__init__(codice,superficie,padiglione,prezzobase)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    def calcola_prezzo(self):
        return super().calcola_prezzo() * 1.30


    def __str__(self):
        return f'{self.codice}:Premium - {self.superficie}mq-  padiglione{self.padiglione} - prezzo {self.calcola_prezzo():.2f} - posizione {self.__posizione}'



