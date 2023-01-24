def nacrtaj(ploča):
    print('     |     |')
    print(f'  {ploča[0]:2} |  {ploča[1]:2} |  {ploča [2]:2}')
    print('_________________')
    print('     |     |')
    print(f'  {ploča[3]:2} |  {ploča[4]:2} |  {ploča [5]:2}')
    print('_________________')
    print('     |     |')
    print(f'  {ploča[6]:2} |  {ploča[7]:2} |  {ploča [8]:2}')
    print()

def provjera(ploča):
    if ploča[0] == ploča[1] == ploča[2] or \
       ploča[3] == ploča[4] == ploča[5] or \
       ploča[6] == ploča[7] == ploča[8] or \
       ploča[0] == ploča[3] == ploča[6] or \
       ploča[1] == ploča[4] == ploča[7] or \
       ploča[2] == ploča[5] == ploča[8] or \
       ploča[0] == ploča[4] == ploča[8] or \
       ploča[2] == ploča[4] == ploča[6]:
        return 1
    elif ''.join(ploča).isalpha():
        return 0
    else:
        return -1
        
ploča = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
dozvoljeno = ploča.copy()
znak = ['X', 'O']
runda = 0
igra = -1
odigrano = []
while igra == -1:
    nacrtaj(ploča)
    igrač = runda % 2
    print(f'Na potezu je igrač {znak[igrač]}')
    unos = input()
    if unos in odigrano or unos not in dozvoljeno:
        print('Krivi unos!')
        continue
    odigrano.append(unos)
    ploča[ploča.index(unos)] = znak[igrač]
    igra = provjera(ploča)
    runda += 1

nacrtaj(ploča)
if igra != 0:
    print(f'Pobijedio je igrač {znak[igrač]}!')
else:
    print('Izjednačeno!')
