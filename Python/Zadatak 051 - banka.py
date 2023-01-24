from argparse import BooleanOptionalAction
from ast import unaryop
from email.headerregistry import UniqueUnstructuredHeader
from email.quoprimime import unquote
from logging import basicConfig
from os import uname, uname_result
from urllib.parse import unquote_plus


if __name__ == '__main__':
    main()

Program u banci
Funkcionalnosti:
- Izboornik
- Otvaranje računa tvrtke
- Prikaz stanja računa
- Prikaz prometa po računu
- Polog novca na račun
- Podizanje novca s računa
- Izlaz iz programa (pogram se nakon svake akcije vrati na početni izbornik u kojem postoji opcija Izlaz)