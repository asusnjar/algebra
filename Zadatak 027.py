s = (input('Ime i prezime: '))
print ('Inicijali su: ',end='')
    # for i in s:
    # # if i.isalpha() and i == i.upper():
    # if i.isupper():
    #         print (f'{i}. ',sep=' ', end='')
    #         #if s[i] = ' 's.index(i)

# for i in range(len(s)):
#     if s[i] == ' ':
#         print(s[i + 1].upper() + '. ', end ='')

s = s.title()
lista = s.split()
for rijec in lista:
    print(rijec[0] + '. ', end ='')
print(lista)