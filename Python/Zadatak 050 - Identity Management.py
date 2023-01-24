userdict = {
1 : ['Ante', 'Šušnjar', 'asusnjar', '1234567890'],
2 : ['Testo', 'Testić', 'test', 'test']
}

def login():
    username = (input ('username= '))
    # for i in userdict:
    #     while username not in userdict[i][2]:
    #         username = (input ('username= '))
    password = (input ('password= '))
    while len(password) < 10:
        print ('Password mora sadržavati minimalno 10 znakova!')
        password = (input ('password= '))
    if username == userdict[1][2] and password == userdict[1][3]:
        print (f'Dobro došao admin {userdict[1][0]} {userdict[1][1]}!')
        adminusers(userdict)
    else:
        for i in userdict:
            if username == (userdict[i][2]) and password == userdict[i][3]:
                print (f'Dobro došao user {userdict[i][0]} {userdict[i][1]}!')

#def logout():

def adminusers(userdict):

    print('Izbornik:')
    print('[1] Dodaj novog korisnika')
    print('[2] Obriši korisnika')
    print('[3] Modificiraj korisnika')
    izbornik = int(input('Unesi izbor: '))
    if izbornik == 1:
        x = (len(userdict)+1)
        ime = input('Upiši Ime: ')
        prezime = input('Upiši Prezime: ')
        create_user = input('Upiši username: ')
        create_pass = input('Upiši password: ')
        userdict.update({x: [ime, prezime, create_user, create_pass]})
        print ('Popis korisnika:')
        print (userdict)
    if izbornik == 2:
        print ('Popis korisnika:')
        print (userdict)
        x = int(input ('Unesi redni broj korisnika kojeg želiš izbrisati: '))
        del userdict[x]
        print (userdict)
    if izbornik == 3: 
        print ('Popis korisnika:')
        print (userdict)
        x = int(input ('Unesi redni broj korisnika kojeg želiš izmjeniti: '))
        ime = input('Upiši Ime: ')
        prezime = input('Upiši Prezime: ')
        create_user = input('Upiši username: ')
        create_pass = input('Upiši password: ')
        userdict.update({x: [ime, prezime, create_user, create_pass]})
        print ('Popis korisnika:')
        print (userdict)        

def main():
    login()

if __name__ == '__main__':
    main()
