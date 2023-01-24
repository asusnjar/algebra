import re

def mask(broj, jocker):
    maskirani = ''
    a = re.match(r'(\d\d\d\d)',n)
    if a = 
    for znak in broj[:-4]: 
        if znak == '-':
            maskirani += '-'
        else:
            maskirani += jocker
    return maskirani + broj[-4:]

broj = input('Unesi broj kartice: ')
jocker = input('Unesi znak kojim ćeš maskirati broj kartice: ')
print(mask(broj, jocker))

