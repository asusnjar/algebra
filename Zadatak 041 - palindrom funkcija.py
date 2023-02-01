rijec = (input('Riječ: '))
rijec = rijec.replace(' ','').lower()

def palindrom(s):
    r = s[::-1]
    return r == s[::-1]

print (palindrom(rijec))
