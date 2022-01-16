# custom exception
class ExamException(Exception):
    pass

# class used to calculate the moving average
class MovingAverage():
    def __init__(self, lunghezza):
        self.lunghezza = lunghezza

    def compute(self, lista):
        
        risultati = []
        i = 0
        k = self.lunghezza

        #try:
        #    for element in lista:
        #        if type(element) != int or float:
        #            tmp = float(element)
        #            
        #except ExamException:
        #    return 'Errore, i valori non sono numerici'

        try:
            if lista == []:
                raise ExamException()
        except ExamException:
            return 'Errore, lista valori vuota'

        try:
            if self.lunghezza > len(lista):
                raise ExamException()
        except ExamException:
            return 'Errore, lunghezza del passo troppo grande'

        for i in range(len(lista)-self.lunghezza+1):
            tmp = lista[i:k]
            risultato = sum(tmp)/self.lunghezza
            risultati.append(risultato)
            k += 1
        return risultati

moving_average = MovingAverage()
#controllare l'input delle liste
#se la lista non è divisibile per la lunghezza?