class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        pass

    def get_data(self):
        pass

def compute_avg_monthly_difference(first_year, last_year):
    pass

#se il file passato non esiste
#se il file passato non è una stringa
#se l'anno passato non appartiene al file
#se l'anno passato in stringa non rappresenta un anno
#se gli anni non sono in ordine va alzata un eccezione
#se c'è un anno duplicato va alzata un eccezione