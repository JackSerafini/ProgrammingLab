class Calcolatrice():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def somma(self):
        return self.number1 + self.number2
    
    def sottrazione(self):
        return self.number1 - self.number2

    def prodotto(self):
        return self.number1 * self.number2
    
    def divisione(self):
        return self.number1 / self.number2
    
    def potenza(self):
        return self.number1 ** self.number2

    def modulo(self):
        pass

    def radice(self):
        from math import sqrt
        return sqrt(self.number1)

    def conversione_di_base(self):
        pass

coppia = Calcolatrice(5, 9)