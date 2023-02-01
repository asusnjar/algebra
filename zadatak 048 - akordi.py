def akordi(ton):

    abeceda = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
    print('Lista tonova: ')

    print(' '.join(abeceda))

    abeceda.extend(abeceda) 

    poz = abeceda.index(ton)
    a = f'{ton} dur: {ton} {abeceda[poz + 4]} {abeceda[poz + 7]}'
    b = f'{ton.lower()} mol: {ton} {abeceda[poz + 3]} {abeceda[poz + 7]}'
    return a + '\n' + b

ton = input('Unesi početni ton: ').upper()
print(akordi(ton))
