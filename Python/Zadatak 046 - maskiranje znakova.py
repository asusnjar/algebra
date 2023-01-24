bk = input('Unesi broj kartice: ')
znak = input('Unesi znak za maskiranje: ')

def listaustring (lista):
    str1 =''
    for i in lista:
        str1 += i
    return str1

def maskiranje (bk):
    lista = list(bk)
    for i in range(len(lista)-4):
        if lista[i].isdigit():
            lista[i] = znak
    return listaustring(lista)

print(maskiranje(bk))

