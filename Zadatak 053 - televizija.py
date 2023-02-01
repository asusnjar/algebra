class Televizija:
    def __init__(self, dijagonala, brend, model, rezolucija):
        self.dijagonala = dijagonala
        self.brend = brend
        self.model = model
        self.power = False
        self.program = 1
        self.glasnoca = 10
        self.rezolucija = rezolucija
        return

    def ukljuci(self):
        self.power = True

    def iskljuci(self):
        self.power = False

    def promjeni_program(self, pr):
        self.program = pr

    def promijeni_glasnocu(self, g):
        if g == '+' and self.glasnoca < 100:
            self.glasnoca += 1
        elif g == '-' and self.glasnoca > 0:
            self.glasnoca -= 1

televizija = TV(50, 'UHD', 'Samsung', 'Q50')
print(televizija)
print(televizija.r)
televizor.ukljuci()
televizor.promjeni_glasnocu('+')
