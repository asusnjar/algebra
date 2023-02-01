import os

def filePathExists(filePath):
    '''
    Metoda koja vraća True/False o tome postoji li "filePath"
    '''
    return os.path.exists(filePath)

def openFilePathForReading(filePath):
    '''
    Metoda za otvaranje konekcije za čitanje prema datoteci filePath
    '''

    if not filePathExists(filePath):
        return f'Datoteka {filePath} ne postoji!'
    try:
        fileReader = open(filePath)
        return fileReader
    except Exception as ex:
        return f'Dogodila se {ex} greška!' 

def openFilePathForWriting(filePath):
    '''
    Metoda za otvaranje konekcije za čitanje prema datoteci filePath
    '''

    if not filePathExists(filePath):
        return f'Datoteka {filePath} ne postoji!'
    try:
        fileReader = open(filePath, 'w')
        return fileReader
    except Exception as ex:
        return f'Dogodila se {ex} greška!' 

def openFilePathForAppending(filePath):
    '''
    Metoda za otvaranje konekcije za čitanje prema datoteci filePath
    '''

    if not filePathExists(filePath):
        return f'Datoteka {filePath} ne postoji!'
    try:
        fileReader = open(filePath, 'a')
        return fileReader
    except Exception as ex:
        return f'Dogodila se {ex} greška!' 

def writeToFilepathOpenClose(filePath, content):
    '''
    Metoda za pisanje sadržaja varijable content u datoteku.
    '''
    try:
        with open(filePath, 'w') as fileWriter:
            fileWriter.write(content)
    except Exception as ex:
        return f'Dogodila se {ex} greška!'

def writeToFilepathOpenClose(filePath):
    '''
    Metoda za čitanje datoteke.
    '''
    if not filePathExists(filePath):
        return f'Datoteka {filePath} ne postoji!'
    try:
        with open(filePath) as fileReader:
            return fileReader.read()
    except Exception as ex:
        return f'Dogodila se {ex} greška!'

def closeFileConnection(fileConnection):
    '''
    Metoda za zatvaranje koncekcije
    '''
    fileConnection.close()

    
