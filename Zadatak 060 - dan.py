from datetime import datetime
datum = input('Unesi datum i vrijeme: ')
objekt = datetime.strptime(datum, '%d.%m.%Y. %H:%M')
print(f'{objekt.strftime("%d. %B %Y. ")} je {objekt.strftime("%A")}.')
