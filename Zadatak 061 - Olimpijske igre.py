import datetime as dt
import locale 
from dateutil import tz

locale.setlocale(locale.LC_TIME, 'hr_HR')
otvaranje = dt.date(2021,7,23)
zatvaranje = dt.date(2021,8,8)
danas = dt.date.today()
razlika = danas - otvaranje

#d1 = danas.strftime("%d./%m./%Y")

print(f'Otvaranje {otvaranje.strftime("%d. %B %Y.")} je {otvaranje.strftime("%A")}' )
print(f'Zatvaranje {zatvaranje.strftime("%d. %B %Y.")} je {zatvaranje.strftime("%A")}' )
print(f'Od otvaranja {otvaranje.strftime("%d. %B %Y.")} je prošlo {str(razlika)} dana.' )

tz_ri = tz.gettz('Europe/Rijeka')
termin_rijeka = dt.datetime(2023, 1, 24, tzinfo=tz_ri)
tz_tk = tz.gettz('Asia/Tokio')
termin_tokio = termin_rijeka.astimezone(tz_tk)
tz_ml = tz.gettz('Australia/Melbourne')
termin_mel = termin_rijeka.astimezone(tz_ml)


print(f'Termin u Rijeci počinje u {termin_rijeka.strftime("%A %d.%m.%Y. %H:%M")}')
print(f'Termin u Rijeci počinje u {termin_tokio.strftime("%A %d.%m.%Y. %H:%M")}')
print(f'Termin u Rijeci počinje u {termin_mel.strftime("%A %d.%m.%Y. %H:%M")}')


