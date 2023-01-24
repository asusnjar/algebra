a = int(input('a = '))
b = int(input('b = '))
while a != b:
    if a < b:
        b = b - a
        print (f'a = {a} b = {b}')
    else:
        a = a - b
        print (f'a = {a} b = {b}')
