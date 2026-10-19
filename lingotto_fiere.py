import csv
from stand import Stand
from stand_standard import StandStandard
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome=nome
        self.__stand=[] # crea una lista vuota in cui inserire gli oggetti stand
        self.__espositori=[] # crea una lista vuota in cui inserire gli oggetti espositori

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        file = open(file_path, "r",encoding='utf-8',newline='')
        lettore=csv.reader(file)
        for riga in lettore:
            if not riga:
                continue


            riga=[campo.strip() for campo in riga] # elimina spazi superflui

            while riga and riga[-1]=='':
                riga.pop()

            if not riga:
                continue


            codice=riga[0]

            if codice.startswith('ST'):
                superficie=float(riga[1])
                padiglione=int(riga[2])
                prezzo=float(riga[3])


                if len(riga)==4:
                    stand=StandStandard(codice,superficie,padiglione,prezzo)
                elif len(riga)==5:
                    caratteristica=riga[4]

                    if caratteristica.isdigit():
                        stand=StandPreseExtra(codice,superficie,padiglione,prezzo,int(caratteristica))

                    else:
                        stand=StandPremium(codice,superficie,padiglione,prezzo,caratteristica)
                else:
                    raise ValueError('Formato dello stand non valido ')
                self.__stand.append(stand)



            elif codice.startswith('ES'):
                if len(riga)!=3:
                    raise ValueError('Formato espositore non valido ')

                espositore=Espositore(codice, riga[1],riga[2])

                self.__espositori.append(espositore)
            else:
                raise ValueError(f'tipo di riga non riconosciuto:{riga}')
        file.close()

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_trovato=None
        espositore_trovato=None

        # cerco lo stand
        for stand in self.__stand: # esaminiamo tutti gli stand della lista
            if stand.codice == codice_stand: # controlliamo se il codice dell'oggetto corrisponde a quello inserito dall'utente
                stand_trovato=stand
                break


        # cerco espositore
        for espositore in self.__espositori:
            if espositore.codice == codice_espositore:
                espositore_trovato=espositore
                break

        # verifico che lo stand esista
        if stand_trovato is None:
            raise Exception('stand non trovato')

        # verifico che l'espositore esista
        if espositore_trovato is None:
                raise Exception("Espositore non trovato")

        # verifico che lo stand sia disponibile
        if not stand_trovato.disponibile:
            raise Exception('stand non disponibile')

        # verifico che espositore non abbia gia uno stand
        if espositore_trovato.stand  is not None:
            raise Exception("l'espositore ha gia uno stand assegnato")

        stand_trovato.disponibile=False
        stand_trovato.espositore=espositore_trovato
        espositore_trovato.stand=stand_trovato




    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.__espositori:
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.__stand)
