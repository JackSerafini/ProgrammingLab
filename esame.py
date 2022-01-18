# classe per le eccezioni
class ExamException(Exception):
    pass

# classe per calcolare la differenza
class Diff():
    # inizializzazione
    def __init__(self, ratio = 1):

        # check del ratio: NO NONE
        if ratio == None:
            raise ExamException('Errore! Il ratio deve essere un valore valido!')

        # check del ratio: NUMERO 
        if type(ratio) != int and type(ratio) != float and ratio != None:
            raise ExamException('Errore! Il valore immesso per il ratio non è un numero!')

        # check del ratio: NO ZERO
        if ratio == 0:
            raise ExamException('Errore! Impossibile dividere per zero!')

        # check del ratio: POSITIVO
        if ratio < 0:
            raise ExamException('Errore! Non ha significato un ratio minore di zero!')

        # check passato
        self.ratio = ratio
        #if self.ratio == None:
        #    self.ratio = default_ratio

    # metodo per calcolare la differenza
    def compute(self, lista = None):

        # se nessuna lista passata
        if lista == None:
            raise ExamException('Errore! Non è stata passata alcuna lista!')

        # check esistenza della lista
        if type(lista) != list:
            raise ExamException('Errore! Quella inserita non è una lista!')

        # check della lista: NON VUOTA 
        if lista == []:
            raise ExamException('Errore! La lista è vuota!')

        # check della lista: NUMERI 
        for index, element in enumerate(lista):
            try:
                element = float(element)
                lista[index] = element
            except:
                raise ExamException('Errore! I valori inseriti nella lista non sono numeri!')
        
        # check della lista: >1 ELEMENTO
        if len(lista) < 2:
            raise ExamException('Errore! Impossibile fare la differenza con un singolo elemento!')

        # check passato
        final_list = []
        i = 0
        while i in range(len(lista) - 1):
            tmp = lista[i+1] - lista[i]
            final_list.append(tmp/self.ratio)
            i += 1

        return final_list