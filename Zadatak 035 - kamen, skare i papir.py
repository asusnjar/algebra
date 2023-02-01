import random
print ('IGRA: Kamen, škare i papir')
rezkomp = 0
rezigrac = 0
puta = int(input('Do koliko želiš igrati? ')) 

def igra():
    while (rezkomp < puta) or (rezigrac < puta):
        print('')
        pokusaj = (input('kamen, škare ili papir? '))
        lista = ['kamen', 'skare', 'papir']
        komp = random.choice(lista)
        if pokusaj == 'škare':
            pokusaj = 'skare' 
        if pokusaj == komp:
            return ('Izjednačeno.')
        elif (pokusaj == 'kamen' and komp == 'papir') or (pokusaj == 'skare' and komp == 'kamen') or (pokusaj == 'papir' and komp == 'skare'):
            return (f'Komp osvaja bod: {komp} > {pokusaj}')
            rezkomp += 1
        elif (pokusaj == 'pair' and komp == 'kamen') or (pokusaj == 'kamen' and komp == 'skare') or (pokusaj == 'skare' and komp == 'papir'):
            return (f'Osvajaš bod: {komp} > {pokusaj}')
            rezigrac += 1
        print (f'Rezultat je: komp: {rezkomp}, igrač: {rezigrac}')

while True:
    igra()

    
