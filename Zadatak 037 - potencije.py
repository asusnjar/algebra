broj = (input ('Upiši broj: '))
broja = int(broj)
lista = []
i = 0
zbroj = 0
while broja > 0:
    lista.append(broja % 10)
    broja //=10
while i < len(broj):
    zbroj += lista[i]**len(broj)
    i += 1
if int(broj) == zbroj:
    print (f'Broj {broj} je Amstrongov!')
else:
    print ('Broj nije Amstrongov!')
