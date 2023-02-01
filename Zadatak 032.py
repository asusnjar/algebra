from random import randint
while True:
    odg = input('Želiš li baciti kocku (da/ne) ')
    if odg == 'ne':
        break
    print(f'Na kocki je pala vrijednost {randint(1,6)}')