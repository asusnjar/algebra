import FileManager
import json

path = "20230130\\users.json"

try:
    with open('20230130\\users.json') as file:
        tekst_json = file.read()
except Exception as ex:
    print(f'Dogodila se greška! {ex}')
dict_json = json.loads(tekst_json)
print(dict_json)
i = 0
while i < len(dict_json)-1:
    print(dict_json[i]["id"])
    print(dict_json[i]["username"])
    print(dict_json[i]["address"]["street"])
    print(dict_json[i]["company"]["bs"])
    i+=1

