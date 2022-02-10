# classe per le eccezioni dell'esame
class ExamException(Exception):
    pass

# classe per aprire il file ed ottenere una lista di liste
class CSVTimeSeriesFile():
    # inizializzazione con il nome del file
    def __init__(self, name = None):
        # check del name: NO NONE
        if name == None:
            raise ExamException('The name must be valid')
        # check del name: STRINGA
        if not isinstance(name, str):
            raise ExamException('The name must be a string')
        # check passato
        self.name = name

    # metodo per creare una lista di liste contenenti le date e il numero di passeggeri
    def get_data(self):

        time_series = [] # time series che sarà poi ritornata

        # check del file: ESISTENZA
        existence_check = False
        try:
            my_file = open(self.name, 'r')
            existence_check = True
        except:
            existence_check = False
        if existence_check == False:
            raise ExamException('The given file does not exist')

        # check del file
        for line in my_file:
            elements = line.split(',') #["data", numero passeggeri, eventuali]
            if len(elements) >= 2: # check della lunghezza della riga (almeno due elementi)
                data = elements[0]
                passeggeri = elements[1]
                try: data = data.rstrip()
                except: pass
                try: passeggeri = passeggeri.rstrip()
                except: pass
                data = data.split('-')
                if len(data) >= 2: # check della lunghezza della data (almeno due elementi: YY-MM)
                    anno = data[0]
                    mese = data[1]
                    try: # check anno, mese, passeggeri: INTERI
                        anno = int(anno)
                        mese = int(mese)
                        passeggeri = int(passeggeri)
                    except: 
                        continue # ricomincio il ciclo senza considerare la riga
                    if anno > 0: # anno maggiore di 0 (consegna)
                        if mese >= 1 and mese <= 12: # mese compreso tra 1 e 12
                            if passeggeri > 0: # passeggeri maggiori di 0 (consegna)
                                if len(time_series) > 0: # già presenti altri elementi
                                    # check della time series: NO DUPLICATI E ORDINATA
                                    tmp = time_series[-1] # ultimo elemento della time series
                                    tmp1 = tmp[0]
                                    data_precedente = tmp1.split('-')
                                    anno_precedente = int(data_precedente[0])
                                    mese_precedente = int(data_precedente[1])
                                    if anno_precedente == anno: # se analizziamo lo stesso anno
                                        # check del mese: MAGGIORE DEL PRECEDENTE
                                        if mese_precedente < mese:
                                            lista = []
                                            lista.append(str(anno) + '-' + '{:02d}'.format(mese))
                                            lista.append(passeggeri)
                                            time_series.append(lista)
                                        else:
                                            raise ExamException('The given timestamp must be valid')
                                    else:
                                        # check dell'anno: MAGGIORE DEL PRECEDENTE
                                        if anno_precedente < anno:
                                            lista = []
                                            lista.append(str(anno) + '-' + '{:02d}'.format(mese))
                                            lista.append(passeggeri)
                                            time_series.append(lista)
                                        else:
                                            raise ExamException('The given timestamp must be valid')
                                else:
                                    lista = []
                                    lista.append(str(anno) + '-' + '{:02d}'.format(mese))
                                    lista.append(passeggeri)
                                    time_series.append(lista)

        my_file.close

        return time_series

# funzione per calcolare la differenza media mensile di passeggeri in un intervallo dato di anni
def compute_avg_monthly_difference(time_series=None, first_year=None, last_year=None):
    # check della time series: NO NONE
    if time_series == None:
        raise ExamException('The given list must be valid')
    # check del primo anno: NO NONE
    if first_year == None:
        raise ExamException('The given "first year" must be valid')
    # check dell'ultimo anno: NO NONE
    if last_year == None:
        raise ExamException('The given "last year" must be valid')
    # check della time series: LISTA
    if not isinstance(time_series, list):
        raise ExamException('The given "time series" is not a list')
    # check della time series: NON VUOTA
    if len(time_series) == 0:
        raise ExamException('The given "time series" is empty')
    # check del primo anno: STRINGA
    if not isinstance(first_year, str):
        raise ExamException('The given "first year" is not a string')
    # check dell'ultimo anno: STRINGA
    if not isinstance(last_year, str):
        raise ExamException('The given "last year" is not a string')
    # check del primo anno: NUMERO
    existence_check = False
    try:
        first_year = int(first_year)
        existence_check = True
    except:
        existence_check = False
    if existence_check == False:
        raise ExamException('The given "first year" is not valid')
    # check dell'ultimo anno: NUMERO
    existence_check = False
    try:
        last_year = int(last_year)
        existence_check = True
    except:
        existence_check = False
    if existence_check == False:
        raise ExamException('The given "last year" is not valid')
    # check del primo anno: <= ULTIMO ANNO
    if first_year > last_year:
        raise ExamException('The given interval is not valid')
    # check del primo anno: != ULTIMO ANNO
    if first_year == last_year:
        raise ExamException('The given interval is not valid')
    # check del primo anno: ESISTENZA IN TIME_SERIES
    first_year_existence = False
    for elemento in time_series:
        if str(first_year) in elemento[0]:
            first_year_existence = True
    if first_year_existence == False: 
        raise ExamException('The given "first year" is not in the time series')
    # check dell'ultimo anno: ESISTENZA IN TIME_SERIES
    last_year_existence = False
    for elemento in time_series:
        if str(last_year) in elemento[0]:
            last_year_existence = True
    if last_year_existence == False:
        raise ExamException('The given "last year" is not in the time series')

    #creo una lista di liste contenente l'anno ed il numero di passeggeri mensili, dove se un mese manca lo rimpiazzo con None
    passengers_per_year = []
    lista_passeggeri = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    flag = 1
    for elemento in time_series:
        data = elemento[0]
        passeggeri = int(elemento[1])
        tmp = data.split('-')
        anno = int(tmp[0])
        mese = int(tmp[1])

        if flag == 1: # se è il primo ciclo
            anno_corrente = anno
            lista_passeggeri[0] = anno
            flag = 0

        if anno_corrente == anno:
            lista_passeggeri[mese] = passeggeri
        else:
            passengers_per_year.append(lista_passeggeri)
            lista_passeggeri = [None, None, None, None, None, None, None, None, None, None, None, None, None]
            lista_passeggeri[0] = anno
            lista_passeggeri[mese] = passeggeri
            anno_corrente = anno
    passengers_per_year.append(lista_passeggeri)
    
    # calcoliamo la media
    result = []
    
    # cerchiamo gli indici nella passengers_per_year degli anni cercati
    a = -1
    b = 0
    for elemento in passengers_per_year:
        # cerchiamo l'indice del primo anno
        if elemento[0] == first_year:
            if a == -1:
                a = passengers_per_year.index(elemento)
        # cerchiamo l'indice dell'ultimo anno
        if elemento[0] == last_year:
            b = passengers_per_year.index(elemento)
    
    i = range(1, 13)
    for n in i: # per n da 1 a 12
        divisor = 0
        b_tmp = b
        risultato = 0
        if b - a == 1: # se l'intervallo è tra due anni
            divisor = 1
            tmp1 = passengers_per_year[b_tmp]
            tmp1 = tmp1[n]
            tmp2 = passengers_per_year[b_tmp-1]
            tmp2 = tmp2[n]
            if tmp1 == None or tmp2 == None:
                risultato = risultato
            else:
                risultato = tmp1 - tmp2
        else:
            while b_tmp-1 >= a:
                tmp1 = passengers_per_year[b_tmp]
                tmp1 = tmp1[n]
                tmp2 = passengers_per_year[b_tmp-1]
                tmp2 = tmp2[n]
                if tmp1 == None or tmp2 == None:
                    risultato = risultato
                    divisor = divisor
                else:
                    risultato = tmp1 - tmp2 + risultato
                    divisor += 1
                b_tmp -= 1
        
        if divisor == 0:
            divisor = 1

        risultato = risultato / divisor

        result.append(risultato)
    
    return result