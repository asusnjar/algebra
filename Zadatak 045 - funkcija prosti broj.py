broj = int(input ('Unesi broj: '))

def prosti(broj):
    for i in range(broj):
        zbr = 0
        if (broj % i == 0) and (i != broj) and (i != 1):
            zbr += i
            if zbr > 1:
                print ('Prime!')