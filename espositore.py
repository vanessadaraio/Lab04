class Espositore:
    def __init__(self,codice,nome,cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome
        self.__stand=None

    @property
    def codice(self):
        return self.__codice

    @property
    def nome(self):
        return self.__nome

    @property
    def cognome(self):
        return self.__cognome

    @property
    def stand(self):
        return self.__stand

    @stand.setter
    def stand(self, valore):
        self.__stand = valore


    def __str__(self):
        if self.__stand is None:
            info_stand='nessuno stand assegnato'
        else:
            info_stand=f'Stand assegnato: {self.__stand.codice}'

        return   f'{self.__codice}:  {self.__nome} {self.__cognome}- {info_stand}'


    def __eq__(self,other):
        if not isinstance(other,Espositore):
            return False
        return self.__codice == other.__codice
