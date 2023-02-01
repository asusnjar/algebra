import os
from datetime import datetime

"""
# Program u banci
# Funkcionalnosti:
# - Izboornik
# - Otvaranje računa tvrtke
# - Prikaz stanja računa
# - Prikaz prometa po računu
# - Polog novca na račun
# - Podizanje novca s računa
# - Izlaz iz programa (pogram se nakon svake akcije vrati na početni izbornik u kojem postoji opcija Izlaz)
"""

iznos = 0.00
racuni = {}

def izbornik(racuni):
    header()
    print(f'{"GLAVNI IZBORNIK":>44}')
    print('1. Kreiranje računa')
    print('2. Prikaz stanja računa')
    print('3. Prikaz prometa po računu')
    print('4. Polog novca na račun')
    print('5. Podizanje novca sa računa')
    print('6. Izlaz')
    if not racuni:
        print('Još niste otvorili račun. Molimo prvo kreirajte račun. Hvala!')
    izbor = int(input('Vaš izbor: '))
    if izbor == 1: 
        kreiranjeracuna(racuni)
    elif izbor == 2:
        stanjeracuna(racuni)
    elif izbor == 3:
        prikazprometa(racuni)
    elif izbor == 4:
        polog(racuni)
    elif izbor == 5:
        podizanje(racuni)
    elif izbor == 6:
        izlaz()

def kreiranjeracuna(racuni):
    header()
    print('GLAVNI IZBORNIK\n')
    print('KREIRANJE RAČUNA\n')
    ime = input('Vlasnik računa - Ime: ')
    prezime = input('Vlasnik računa - Prezime: ')
    oib = input('OIB tvrtke: ')
    naziv = input('Naziv tvrtke: ')
    ulica = input('Ulica: ')
    postanskibroj = input('Poštanski broj: ')
    grad = input('Grad: ')
    year = datetime.now().year
    month = str(datetime.now().month).zfill(2)
    brojracuna = (f'BA-{year}-{month}-00001')
    valuta = (input('Želite li položiti [HRK] kune ili [EUR] eure?' ))
    print('Molimo Vas upišite iznos koji želite položiti na račun.\n')
    print('NAPOMENA Molimo Vas koristite decimalnu točku, a ne zarez.\n')
    iznos = float(input())
    racuni = {
    'brojracuna' : brojracuna,
    'oib' : oib, 
    'naziv' : naziv, 
    'ulica' : ulica, 
    'postanskibroj' : postanskibroj, 
    'grad': grad,
    'ime': ime,
    'prezime' : prezime,
    'iznos' : iznos,
    'valuta' : valuta,
    }
    print(f'Podaci o računu tvrtke {naziv} uspješno su spremljeni.\nZa nastavak pritisnite bilo koju tipku.')
    izbornik(racuni)
    return racuni

def stanjeracuna(racuni):
    print(f'Broj računa: {racuni["brojracuna"]}')
    now = datetime.now()
    print(f'Datum i vrijeme: ', now)
    print(f'Trenutno stanje računa: {racuni["iznos"]} {racuni["valuta"]}')
    
def polog():
    print(f'Broj računa: {racuni["brojracuna"]}')
    print(f'Trenutno stanje računa: {racuni["iznos"]} {racuni["valuta"]}')
    valuta = int(input('Želite li položiti [1] kune ili [2] eure?' ))
    valuta = valuta - 1
    print('Molimo Vas upišite iznos koji želite položiti na račun')
    print('NAPOMENA Molimo Vas koristite decimalnu točku, a ne zarez.\n')
    iznos = float(input())

def main():
    izbornik(racuni)

def header():
    os.system('cls')
    print('*'*80)
    print(f'{"PyBANK ALGEBRA":>43}')
    print()

if __name__ == '__main__':
    main()
