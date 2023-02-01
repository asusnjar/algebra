try:
    m = int(input('Unesji djeljenik: '))
    n = int(input('Unesji djeljenik: '))
    print(m/n)
except Exception as ex:
    print(f'Ups! {ex}')