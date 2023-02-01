tekst = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
tekst = tekst.split()
rijeci = dict()
for rijec in tekst:
    rijec = rijec.strip()
    if not rijec[-1].isalpha():
        rijec = rijec[:-1]
    if rijec not in rijeci:
        rijeci[rijec] = 1
    else:
        rijeci[rijec] += 1
print(rijeci)



