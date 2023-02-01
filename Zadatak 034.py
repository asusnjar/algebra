print ('Konvezije: ')
print ('[1] km <-> milje')
print ('[2] °F <-> °C')
print ('[3] kg <-> funta')
print ('[4] litre <-> galoni')
print ('[5] kW <-> ks')
izbor = int(input('Odaberi konverziju: '))
a = int(input('Unesi vrijednost: '))


km = a * 0.6214
milja = a / 0.6214
f = (a * 1.8) + 32
c = (a - 32) * 0.5555
kg = a / 2.2046
pound = a * 2.2046
l = a / 0.2642
g = a * 0.2642
kw = a / 1.3596
hp = a * 1.3596

if izbor == 1:
    print (f'{a} km = {milja} milja')
    print (f'{a} milja = {km} km')
elif izbor == 2:
    print (f'{a} °F = {c} °C')
    print (f'{a} °C = {f} °F')

elif izbor == 3:
    print (f'{a} kg = {pound} lbs')
    print (f'{a} lbs = {kg} kg')

elif izbor == 4:
    print (f'{a} l = {g} galona')
    print (f'{a} galona = {l} l')

else izbor == 5:
    print (f'{a} kW = {hp} ks')
    print (f'{a} ks = {kw} kW')
