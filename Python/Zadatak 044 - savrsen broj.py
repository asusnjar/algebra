from re import X


broj = int(input ('Upiši broj: '))

def savrsen(broj):
    lista = []
    i = 0
    for i in range(1, broj):
        if broj % i == 0:
            lista.append(i)
    zbr = 0
    for i in range(lista):
        zbr += lista[i]
    if broj == zbr:
        return True

print ('Broj je savršen: ', savrsen(broj))
