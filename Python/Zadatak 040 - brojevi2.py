nbr = int(input ('Koliko želiš brojeva: '))
i = 0
zbroj = 0
parni = 0
while i < nbr:
    broj = int(input (f'{i+1}. broj: '))
    if broj % 2 == 0:
        zbroj += broj
        parni += 1
    else:
        zbroj += 0
    i += 1
print (f'Zbroj= {zbroj}')
prosjek = zbroj / parni
print (f'Prosjek parnih= {prosjek}')

