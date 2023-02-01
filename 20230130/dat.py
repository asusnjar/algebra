ulaz = open("20230130\ime.txt", encoding='utf-8')
print(ulaz.read())
print(ulaz.tell())
ulaz.close()

izlaz = open("20230130\serije.txt", 'a')
serija = input('Unesi seriju: ')
while serija != '.':
    izlaz.write(serija + '\n')
    serija = input('Unesi seriju: ')
izlaz.close()

with open ("20230130\serije.txt", encoding='utf-8') as f:
    sve = f.readlines()
for red in sve:
    print(red, end = '')

