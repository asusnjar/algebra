nbr = int(input ('Koliko želiš brojeva: '))
i = 0
zbroj = 0
while i < nbr:
    broj = int(input (f'{i+1}. broj: '))
    zbroj += broj
    i += 1
print (f'Zbroj= {zbroj}')

