broj = (input ('Upiši broj: '))
x = 0
while x < int(broj):
    lista = []
    i = 0
    zbroj = 0
    broja = x
    pot = len(str(x))
    while broja > 0:
        lista.append(broja % 10)
        broja //=10
    while i < len(str(x))-1:
        zbroj += lista[i]**x
        i += 1
    if x == zbroj:
        print (f'Broj {broj} je Amstrongov!')
    x += 1
