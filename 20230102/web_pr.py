import urllib.request

url = 'https://www.algebra.hr'
konekcija = urllib.request.urlopen(url)
sadrzaj = konekcija.read().decode()
print(sadrzaj)
