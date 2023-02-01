s = (input('Riječ: '))
s = s.replace(' ','').lower()
r = s[::-1]
if s == r:
    print (f'{s} je palindrom')
else: 
    print (f'{s} nije palindrom')

