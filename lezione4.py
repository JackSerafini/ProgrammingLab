class CSVFile():
    def __init__(self, name):
        self.name = name
    
#aprire il file, dividere la data dai valori ed assegnare questi valori in una lista di liste
    def get_data(self):
        lista = []
        my_file = open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            lista.append(elements)
        my_file.close()
        
        return lista

my_var = CSVFile('shampoo_sales.csv')
print(my_var.get_data())