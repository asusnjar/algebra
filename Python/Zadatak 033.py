from random import randint

def vecimanji(broj):
    if broj < r:
        return 'Probaj s većim brojem.'
    elif broj > r:
        return 'Probaj s manjim brojem.'
    elif broj == r:
        return 'Nevjerojatno! Pogodak!'


print ('Pogodi broj između 1 i 100')
broj = 0
r = randint(1,100)
brojac = 0
while broj != r:
    broj = int(input('Broj = '))
    print(vecimanji(broj))
    brojac +=1
    if broj == r:
        print(f'Pogodio si iz {brojac}. pokušaja!')

