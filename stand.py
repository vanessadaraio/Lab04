class Stand:
    def __init__(self,codice,superficie,padiglione,prezzobase):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzobase = prezzobase
        self.__disponibile=True # lo stand è disponibile
        self.__espositore=None # non ancora associato a nessun espositore

    @property
    def codice(self):
        return self.__codice

    @property
    def superficie(self):
        return self.__superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzobase(self):
        return self.__prezzobase

    @property
    def disponibile(self):
        return self.__disponibile

    @disponibile.setter
    def disponibile(self, valore):
        self.__disponibile = valore

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self, valore):
        self.__espositore = valore


    def calcola_prezzo(self):
        return self.__prezzobase

    def __str__(self):
        return f'{self.__codice}:Standard| {self.__superficie}mq - Padiglione:{self.__padiglione} - prezzo:{self.calcola_prezzo():.2f}euro'

    def __lt__(self, other):
        return self.calcola_prezzo() < other.calcola_prezzo()


    def __eq__(self, other):
        if not isinstance(other, Stand):
            return False
        return self.__codice==other.__codice




