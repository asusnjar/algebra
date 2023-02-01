class Racun:
    def __init__(self, br, datum, stavke, pdv=25):
        self.br = br
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.iznos = 0
        self.izracunaj_iznos()
        return
    
    def izracunaj_iznos(self):
        for artikl in self.stavke:
            self.iznos += artikl[-1]
        return

    def obracunaj_pdv(self):
        return self.iznos * self.pdv / 100

    def ažuriranje_stavke(self):
        print(self.__repr__())
        id = int(input('Unesi id stavke koju želiš urediti: '))
        while id not in 
        
    def izbaci_stavku(self, x):
        self.stavke.pop(x)
        return

    def __repr__(self):
        prvi_dio = f'{self.br} {self.datum}\n'
        drugi_dio = ''
        for artikl in self.stavke:
            drugi_dio += f'{artikl} {artikl[0]} {artikl[1]}\n'
        treci_dio = f'TOTAL: {self.iznos} od toga pdv: {self.obracunaj_pdv()}\n'
        return prvi_dio + drugi_dio + treci_dio

    def __str__(self):
        return self.__repr__()

br = input('Unesi broj računa: ')
datum = input('Unesi datum u formatu dd.mm.yyyy: ')
i = 1
stavke = dict()
while True:
    proizvod = input('Unesi proizvod (za kraj pritisni enter): ')
    if proizvod == '':
        break
    cijena = float(input('Unesi cijenu: '))
    stavke.append((i, proizvod, cijena))
    i += 1
pdv = input('Unesi pdv (za 25% pristisni enter): ')
if pdv == '':
    r1 = Racun(br, datum, stavke)
else:
    r1 = Racun(br, datum, stavke, pdv)
print(r1)

#promjeni stavku
#izbaci stavku