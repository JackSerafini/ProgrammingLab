class Automobile():
    def __init__(self, casa_automo, modello, numero_posti, targa):
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa
    
    def __str__(self):
        print('Casa produttrice: ' + self.casa_automo + ', Modello: ' + self.modello + ', Numero posti: ' + str(self.numero_posti) + ', Targa: ' + self.targa)
    
    def parla(self):
        print('Broom Broom!')

    def confronta(self, auto2):
        if self.casa_automo == auto2.casa_automo and self.modello == auto2.modello and self.numero_posti == auto2.numero_posti:
            print('Le due automobili hanno le stesse caratteristiche!')
        else:
            print('Le due automobili hanno caratteristiche diverse!')

class Transformer(Automobile):
    def __init__(self, nome, generazione, grado, reparto):
        self.nome = nome
        self.generazione = generazione
        self.grado = grado
        self.reparto = reparto
    
    def scheda_militare(self):
        print('Il grado di ' + self.nome + ' è ' + self.grado + ' ed il suo reparto di appartenenza è ' + self.reparto)

Giovanni = Transformer('Giovanni', 2, 'sergente', 'spionaggio')
print(type(Giovanni))