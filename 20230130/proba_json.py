import json
user = {
    "id" : 1,
    "firstName": "Petar",
    "lastName": "Peric"
}

try:
    with open('20230130\\user_p01.json', 'w') as file_writer:
        json.dump(user, file_writer, indent=4)
except Exception as ex:
    print(f'Dogodila se greška! {ex}')

try:
    with open('20230130\\user_p01.json') as file_reader:
        tekst_json = file_reader.read()
except Exception as ex:
    print(f'Dogodila se greška! {ex}')
dict_json = json.loads(tekst_json)
print(dict_json)
