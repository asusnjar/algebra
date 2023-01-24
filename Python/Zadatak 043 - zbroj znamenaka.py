broj = (input ('Upiši broj: '))

def zbroj(broj):
    zbr = 0
    for i in broj:
        zbr += int(i)
    return zbr

print('Zbroj znamenki je: ', zbroj(broj))


