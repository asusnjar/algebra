import datetime as dt
import locale

locale.setlocale(locale.LC_TIME, 'hr_HR')
danasnji_dan = dt.datetime.now()
print (f'{danasnji_dan.strftime("%A")}')
print (f'{danasnji_dan.strftime("%a")}')
print (f'')
