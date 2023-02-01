import datetime as dt

class Vrijeme:
    def __init__(self, datumvrijeme):
        self.dv = datumvrijeme
    def vr(self):
        return self.dv.split()[1]

datumvrijeme = input('Upiši datum i vrijeme: MM.DD.GGGG HH:MM ')
v1 = Vrijeme(datumvrijeme)
print (v1.vr())
