n = int(input ('Koliko n prirodnih brojeva? '))

def zbroj(n):
    a = n
    i = 0
    zb = 0
    while i < a+1:
        zb += i
        i += 1
    return zb

print ((f'Zbroj {n} brojeva je: '), zbroj(n))